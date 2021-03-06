from tkinter import *

import random
import time
import csv

EMPTY = 0
PADDLE_HEIGHT = 360
PADDLE_MOVE = [-10, 10]

START = 3
END = 4


class Ball:
    def __init__(self,canvas,paddle,color,announceterm,saveterm,winval=10,loseval = -1):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # 공 크기 및 색깔

        self.canvas.move(self.id, 245, 200)  # 공을 캔버스 중앙으로 이동
        starts = [-3, 3]  # 공의 속도를 랜덤으로 구성하기 위해 준비한 리스트
        random.shuffle(starts)  # starts 리스트 중에 숫자를 랜덤으로 골라서
        self.x = starts[0]  # 처음 공이 패들에서 움직일때 왼쪽으로 올라갈지 오른쪽으로 올라갈지 랜덤으로 결정되는 부분
        self.y = -3  # 처음 공이 패들에서 움직일때 위로 올라가는 속도
        self.canvas_height = self.canvas.winfo_height()  # 캔버스의 현재 높이를 반환한다.(공이 화면에서 사라지지 않기위해)
        self.canvas_width = self.canvas.winfo_width()  # 캔버스의 현재 넓이를 반환한다.(공이 화면에서 사라지지 않기위해)
        self.hit_bottom = False
        self.values = {}
        self.epsilon = 0.1  # 랜덤율
        self.alpha = 0.99  # 망각계수
        self.learning = True
        self.cycle_data = []
        self.wincount = 0
        self.losecount = 0
        self.gamecount = 0
        self.winval = winval  # 성공 보상치
        self.loseval = loseval
        self.announceterm = announceterm  # 게임 횟수 프린트 텀
        self.saveterm = saveterm  # csv 저장 텀

        # csv 파일에서 gamecount / values 불러옴
        # self.loadcsv()

#위에 init함수에서 self.epsilon = 0.1으로 잡아놨음
#PADDLE_MOVE =[-10,10]
    def action(self):
        r = random.random()
        if r < self.epsilon:
            direction = self.randomChoice() #randomChoice : 0 or 1을 랜덤으로 고르는 함수
        else:
            direction = self.greedyChoice()
        x = PADDLE_MOVE[direction]
        #print(x)                #부딪히면서 10,-10,10,10,-10....이 계속 나옴
        # 머신러닝을 위한 한 사이클 내 이동 데이터 저장
        self.cycle_data.append(self.keystate(direction))
        # 이동/그리기
        self.paddle.move(x)
        self.paddle.draw()


    # 이동 방향 랜덤으로 지정
    def randomChoice(self):
        rand = random.choice([0, 1])
        key = self.keystate(rand)
        if key not in self.values:
            self.add(key)
        return rand


    # 이동 방향 Greedy로 지정
    def greedyChoice(self):
        val_left = self.keystate(0)
        #print('val_left ',val_left)     #val_left  (130.0, (417.0, 54.0), (3, 3), 0)
        val_right = self.keystate(1)
        #print('val_right ', val_right)  #val_right  (130.0, (417.0, 54.0), (3, 3), 1)
        #val_stop = self.keystate(2)  # 패들무브 두번째 요소 -> 0


        if self.lookup(val_left) > self.lookup(val_right) :
            return 0
        elif self.lookup(val_left) < self.lookup(val_right) :
            return 1
        else:
            return random.choice([0, 1])


    def add(self, key):
        self.values[key] = 0


    def lookup(self, key):
        if key not in self.values:
            # print(key)
            self.add(key)
        return self.values[key]


    def hit_paddle(self, pos):  # 패들에 공이 튀기게 하는 함수
        paddle_pos = self.canvas.coords(self.paddle.id)
        # 공의 x좌표가 패들의 너비 안에 있는지 / 공 바닥이 패들 윗면에 닿아 있는지
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
                and pos[3] == PADDLE_HEIGHT:
            return True
        return False


    # 공을 패들로 받았는지 여부 출력(True/False)
    def is_paddle_hit(self):
        return self.hit_paddle(self.canvas.coords(self.id))


    def draw(self):
        # 볼의 현재 좌표를 출력해준다. 공 좌표( 좌상단 x,y좌표 / 우하단 x,y좌표 )
        pos = self.canvas.coords(self.id)
        # [ 255,29,270,44]

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y = -3

        self.canvas.move(self.id, self.x, self.y)  # 공을 움직이게 하는 부분
        # 공이 화면 밖으로 나가지 않게 해준다


    def keystate(self, movement):
        paddle_pos = self.canvas.coords(self.paddle.id)
        ball_pos = self.canvas.coords(self.id)
        # paddle 위치(좌측 x좌표), 공의 좌상단 x/y좌표, 공의 좌우/상하 속도(방향), paddle을 좌/우 중 어느 쪽으로 움직이는지
        return (paddle_pos[0], (ball_pos[0], ball_pos[1]), (self.x, self.y), movement)


    # 사이클 시작 : 1, 사이클 종료 : -1, 해당 없음 : 0
    def cyclestate(self):
        pos = self.canvas.coords(self.id)
        if pos[3] == PADDLE_HEIGHT: #pos[3]:우측하단 y 좌표 현재 패들위치가 360지점
            if self.y == -3:        #공이 위로 올라가는데(-3) 패틀위치 360 지점을 지나가면 start리턴
                return START
            elif self.y == 3:       #공이 아래로 내려오는데(3) 360지점으 지나가면 END
                return END
        return 0                    #공이 start~end 동안에만 패들이 움직임 ????

#self.cycle_data =[]
#values 딕셔너리의 정보 : 208 303 342 3 -3 0 : 1.01106933 (한번 공이 올라갔다가 내려왔을 때 까지의 학습데이터 )
    # 결과 학습
    def backup(self, newVal, idx):                          # newVal = -1 or 1 이 들어감 , idx = 324-1
        if idx >= 0 and self.learning:
            prevVal = self.values[self.cycle_data[idx]]     # 한사이클 돌았을 때 마지막 행 바로 전(323) 학습데이터의 가중치를 preval에 넣겠음
            self.values[self.cycle_data[idx]] += self.alpha * (newVal - prevVal)
            # print("key : {0}, val : {1}".format(self.cycle_data[idx],self.values[self.cycle_data[idx]]))
            self.backup(newVal * self.alpha, idx - 1)


    # 게임 끝났을 시 학습 및 cycle_data 초기화
    def gameover(self):
        if self.learning:
            # paddle로 받았으면 1, 못 받았으면 -1
            if self.is_paddle_hit():
                result_value = self.winval # winval : hit이면 1, miss면 -1
                self.wincount += 1
            else:
                result_value = self.loseval
                self.losecount += 1
            self.backup(result_value, len(self.cycle_data) - 1) # 전체 한판에 대한 학습데이터 중 맨 마지막 하나 빼줌
                                                                # (맨 마지막에 hit/miss했다는 정보는 다음번 학습때 중요하지 않음
                                                                # 고시 합격생한테 연필, 방석 뭐썼음? ... 합격증 받았음(합/불) 정보를 빼줌
            self.gamecount += 1

            # saveterm마다 csv 저장
            if self.gamecount % self.saveterm == 0:
                self.writecsv()
            if self.gamecount % self.announceterm == 0:
                print("cycle count : {0}".format(ball.gamecount))
        self.cycle_data.clear()


    def winnerval(self, winner):
        if winner == 'hit':
            return 1
        elif winner == 'miss':
            return -1
        else:
            return 0


    # 게임 결과 csv로 저장
    def writecsv(self):
        try:
            # Values 저장
            Fn = open("/Users/misoni/Desktop/pythondata/pong_value.csv", 'w', newline='')
            writer = csv.writer(Fn, delimiter=',')
            writer.writerow([self.gamecount])  # 첫줄에 학습 게임 횟수 저장
            keys = self.values.keys()
            for key in keys:
                writer.writerow([key[0],  #패들의 x좌표
                                 key[1][0], #공의 x좌표
                                 key[1][1], #공의 y좌표
                                 key[2][0], #공의 좌우방향
                                 key[2][1], #공의 상하방향
                                 key[3],    #패들 무브(1or 0)
                                 ball.values[key] #가중치
                                 ])
            Fn.close()

            # 성공/실패 횟수 저장
            Fn = open("/Users/misoni/Desktop/pythondata/pong_score.csv", 'a', newline='')
            writer = csv.writer(Fn, delimiter=',')
            writer.writerow([self.wincount, self.losecount, self.gamecount]) #gameover에서 쓰였던 변수 hit되면 wincnt +1, miss면 losecnt +1, gamecnt : 전체 게임 건수

            Fn.close()
            # 승률의 변화를 확인하기 위해 일정 판수마다 카운트 리셋
            self.wincount = 0
            self.losecount = 0

            print("save data in cycle {0}.".format(self.gamecount))
        except Exception as e:
            print('save data failed in cycle {0}.\nError Type : {1}'.format(self.gamecount, type(e).__name__))


    def loadcsv(self):
        try:
            Fn = open("/Users/misoni/Desktop/pythondata/pong_value.csv", 'r')
            self.gamecount = int(Fn.readline().split(',')[0])  # 첫 줄의 학습 게임 횟수 불러오기
            reader = csv.reader(Fn, delimiter=',')
            for key in reader:
                self.values[(
                int(float(key[0])), (int(float(key[1])), int(float(key[2]))), (int(float(key[3])), int(float(key[4]))),
                int(float(key[5])))] = float(key[6])
            print('Load Success! Start at cycle {0}'.format(self.gamecount))
        except Exception:
            print('Load Failed!')


class Paddle:
    def __init__(self, canvas, y_loc, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # 패들의 높이와 넓이 그리고 색깔

        self.canvas.move(self.id, 200, y_loc)  # 패들 사각형을 200,300 에 위치
        self.x = 0  # 패들이 처음 시작할때 움직이지 않게 0으로 설정
        self.canvas_width = self.canvas.winfo_width()  # 캔버스의 넓이를 반환한다. 캔버스 밖으로 패들이 나가지 않도록
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)  # 왼쪽 화살표 키를 '<KeyPress-Left>'  라는 이름로 바인딩
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)  # 오른쪽도 마찬가지로 바인딩한다.

    def draw(self):
        pos = self.canvas.coords(self.id)
        # print(pos)
        if pos[0] <= 0 and self.x < 0:  # 패들의 위치가 왼쪽 끝이고, 이동하려는 방향이 왼쪽이면 함수 종료(이동 안 함)
            return
        elif pos[2] >= self.canvas_width and self.x > 0:  # 패들의 위치가 오른쪽 끝이고, 이동하려는 방향이 오른쪽이면 함수 종료
            return
        self.canvas.move(self.id, self.x, 0)


        # 패들이 화면의 끝에 부딪히면 공처럼 튕기는게 아니라 움직임이 멈춰야한다.
        # 그래서 왼쪽 x 좌표(pos[0]) 가 0 과 같거나 작으면 self.x = 0 처럼 x 변수에 0 을
        # 설정한다.  같은 방법으로 오른쪽 x 좌표(pos[2]) 가 캔버스의 폭과 같거나 크면
        # self.x = 0 처럼 변수에 0 을 설정한다.

    def turn_left(self, evt):  # 패들의 방향을 전환하는 함수
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def move(self, x):
        self.x = x


'''
LYE
1. cyclestart 함수 추가(공이 딱 패들의 높이를 지나 위로 출발하는 시점에 True)
2. 캔버스 높이 및 공/패들 시작점 조정(y 좌표가 3의 배수로 떨어지게)
'''

if __name__ == '__main__':
    tk = Tk()  # tk 를 인스턴스화 한다.
    tk.title("Game")  # tk 객체의 title 메소드(함수)로 게임창에 제목을 부여한다.
    tk.resizable(0, 0)  # 게임창의 크기는 가로나 세로로 변경될수 없다라고 말하는것이다.
    tk.wm_attributes("-topmost", 1)  # 다른 모든 창들 앞에 캔버스를 가진 창이 위치할것을 tkinter 에게 알려준다.

    canvas = Canvas(tk, width=500, height=450, bd=0, highlightthickness=0)
    # bg=0,highlightthickness=0 은 캔버스 외곽에 둘러싼
    # 외곽선이 없도록 하는것이다. (게임화면이 좀더 좋게)
    canvas.pack()  # 앞의 코드에서 전달된 폭과 높이는 매개변수에 따라 크기를 맞추라고 캔버스에에 말해준다.
    tk.update()  # tkinter 에게 게임에서의 애니메이션을 위해 자신을 초기화하라고 알려주는것이다.
    paddle = Paddle(canvas, PADDLE_HEIGHT, 'blue')

    # announceterm : 현재 count 출력 term, saveterm : csv에 저장하는 term
    ball = Ball(canvas, paddle, 'red', announceterm=500, saveterm=1000) #announceterm: 게임하고 있다고 표시 saveterm마다 csv를 저장하게끔
    start = False
    # 공을 약간 움직이고 새로운 위치로 화면을 다시 그리며, 잠깐 잠들었다가 다시 시작해 ! "
    is_cycling = False

    while 1:
        ball.draw()

        c_state = ball.cyclestate() #cyclestate()값은 start(3), end(4) ,0 임
        #print(c_state) # 0 0 0 0 0 0 0 3 0 0 0 0 0 0 4
        if c_state == END:
            # print('END')
            ball.gameover()
            is_cycling = False #한판다 돌았으면
        if c_state == START or ball.is_paddle_hit(): #스타트거나 or 공이 패들에 맞으면
            # print('START')
            is_cycling = True  # 다시 시작하면

        if is_cycling:          #트루면 작동해라 ( 볼 액션 함수 안에 패들을 움직이는 함수가 있음 --> 패들 움직임은 스타트부터 앤드까지 )
            ball.action()

        tk.update_idletasks()  # 우리가 창을 닫으라고 할때까지 계속해서 tkinter 에게 화면을 그려라 !
        tk.update()  # tkinter 에게 게임에서의 애니메이션을 위해 자신을 초기화하라고 알려주는것이다.

        #10만번 학습 후에 정상 속도로 플레이 시작(학습 결과 반영됨)
        if ball.gamecount > 5000:
            time.sleep(0.005)  # 무한 루프중에 100분의 1초마다 잠들어라 !