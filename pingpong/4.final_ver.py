# ##핑퐁게임을 구현하기 위해 필요한 클래스 3가지
# 1. 캔버스 클래스
#     -캔버스 크기, 색깔
# 2. 공 클래스
#     - init
#         1. 공의 크기, 색깔
#         2. 게임이 시작할 때 공의 첫 위치
#         3. 게임이 시작할 때 공이 움직이는 방향(랜덤으로)
#         4. 게임이 시작할 때 공이 위로 움직이는 속도
#         5. 공이 화면에에서 사라지지 않도록 필요한 정보를 모으는 코드
#
#     - 공을 움직이게 하는 함수
#         : 공은 사람이 아닌 스스로 움직임
#         : init함수에서 공이 시작할 때 위로 움직이게 해주고 그 이후부터는 벽에 부딪혔을 때 화면 밖으로 나가지 않게 해줌
#     - 공이 패들에서 튀기게 하는 함수
#         : 패들의 현재 위치를 알아내서 공의 위치가 패들의 위치안으로 들어오면 True를 리턴하는 코드
#
# 3. 패들 클래스
#     - init함수
#     - 패들을 움직이는 함수
#     - 패들이 화면 밖으로 안나가게 하는 함수

from tkinter import *
import random
import time


# ball = Ball(canvas, paddle, 'white') 밑에서 인스턴스화 하는거 이해하기 쉬우려고 가져옴
class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #공의 모양 #서  남   동   북
        canvas.configure(background='black')
        self.canvas.move(self.id, 245, 100) #캔버스 시작 위치
                            #공자신 x     y

        starts = [-3, -2, 1, 1, 2, 3]
        random.shuffle(starts) #랜덤으로 섞어서 첫번째 요소를 x축에 담겠다
        self.x = starts[0]
        self.y = -3 # 음수면 위로 올라감

        self.canvas_height = self.canvas.winfo_height() #캔버스 높이
        #print('높이',self.canvas_height)   #500
        self.canvas_width = self.canvas.winfo_width()   #캔버스 너비
        #print('너비',self.canvas_width)    #600 #밑에서 canvas =에서 정해준거임
        self.hit_bottom = False #바닥에 닿으면 게임 끝나는 코드를 구현하기 위해서 쓰는 변수( 나중에 True로 바꿔줄거임)
###################################################################################
#####################   ex232) 공이 키보드의 방향기로 움직이게 하려면?(paddle init함수 참고)
###################################################################################
# 1)ball 클래스 init함수에 self.canvas.bind_all함수 추가
# 2)ball 클래스에 turn_left, turn_right 함수 추가
# 3)ball 클래스 draw함수에 self.canvas.bind_all함수 추가

###################################################################################
#####################   ex233) 공이 위아래로도 움직일 수 있도록 코드 추가
###################################################################################
        # self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        # self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<Key>',self.turn_up)
        # self.canvas.bind_all('<KeyPress-Down>',self.turn_down)



    # def turn_left(self,evt):
    #     self.x = -9
    #
    # def turn_right(self,evt):
    #     self.x = 9
    #
    def turn_up(self,evt):
        self.y = -9
    #
    # def turn_down(self,evt):
    #     self.y = 9
###################################################################################
#####################   ex233) 공이 패들 영역안으로 들어오면 멈추고 패들과 함께 이동하도록 하시오
###################################################################################

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)  # 패들의 위치를 조회하는 코드
        #print(paddle_pos)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            #공의 오른쪽 > 패들의 왼쪽 and 공의 왼쪽 < 패들 오른쪽
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            #공 위 > 패들 아래            and 공 아래  < 패들 위
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) # 공을 움직이는 함수
                            #공   공의 x방향(좌우), 공의 y 방향(위아래)
        pos = self.canvas.coords(self.id)
        # self.canvas.bind_all('<KeyPress-Left>',self.turn_left) #키보드 방향키 '<-'를 누르면 turn_left라는 함수 실행
        # self.canvas.bind_all('<KeyPress-Right>',self.turn_right) #키보드 방향키 '->'를 누르면 turn_rightt라는 함수 실행
        # self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        # self.canvas.bind_all('<KeyPress-Down>',self.turn_down)

        if pos[1] <= 0: #남 ( 천장이 0 이니까 천장보다 위에 있는건 - 얌)
            self.y = 3
        if pos[3] >= self.canvas_height: #북
            #self.hit_bottom = True         ########################################이거가 왜 pass랑 똑같지?
            self.y = -3         #바닥이랑 만나면 튀어오르게 하는 코드
            print('miss')
        if pos[0] <= 0: #서
            self.x = 3
        if pos[2] >= self.canvas_width: #동
            self.x = -3
        if self.hit_paddle(pos) == True: # 아래서 정한 공이 패들위치안으로 들어가면(True) 위로 튀어올라라
            self.y = -5
            self.x = 3    ########################################모르겠아
            print('hit')




class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)    #패들의 크기와 색깔
        self.canvas.move(self.id, 200, 400)                         #패들을 움직이게 하는 함수
                                                                    #x축 200, y축 400에 패들 고정
        self.x = 0              #패들이 게임시작할 때 움직이지 말라고 속도 0 으로 고정
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()               #패들이 화면밖으로 나가지 않도록 지
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)      #방향키 작동 시 함수 실행
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)

#패들이 화면 밖으로 가지 않도록!
    def draw(self):

        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 and self.x < 0 :                          #패들의 왼쪽이 0보다 작으면 & 방향
            return
            # self.x = 0                                          #패들을 멈춰라
        elif pos[2] >= self.canvas_width and self.x > 0:          #패들의 동쪽이 600보다 크면
            return
            #self.x = 0                                          #패들을 멈춰라 ( 이건 자동으로 움직였을때만 먹음)
            #키보드를 눌렀을 때는 turn_left 함수가 작동된 것 ? 이게 무슨말이야
            #그래서 강력한 게 필요함 return!
        self.canvas.move(self.id, self.x, self.y)

    def turn_left(self,evt):
        self.x = -9

    def turn_right(self,evt):
        self.x = 9

    def turn_up(self,evt):
        self.y = -9

    def turn_down(self,evt):
        self.y = 9



tk = Tk()
tk.title("Game")

tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas,'white')
ball = Ball(canvas, paddle, 'white')

while 1:

    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)