#ex243 공이 패들에 닿으면 hit 패들에 안닿고 y축 400좌료를 지나치면 miss(틱텍토로 치면 gameover()함수)
#ball 클래스 안에 gameover()함수 만드시오
# gameover() 함수를 while 1: 아래의 코드에서 실행되게 한다
from tkinter import *
import random
import time

class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        canvas.configure(background='black')
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def gameover(self):
        pos = self.canvas.coords(self.id)
        if pos[1] == 400 and self.y > 0:
            print('miss')
        if self.hit_paddle(pos) == True:
            print('hit')
            self.y = -5

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 5
        if pos[0] <= 0:
            self.x = 5
        if pos[2] >= self.canvas_width:
            self.x = -5
        if pos[3] >= self.canvas_height:
            self.y = -5

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False




class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 :                          #패들의 왼쪽이 0보다 작으면 & 방향
            self.x = 1 #패들 멈춰라
            # self.x = 0                                          #패들을 멈춰라
        elif pos[2] >= self.canvas_width :          #패들의 동쪽이 600보다 크면
            self.x = -1
        self.canvas.move(self.id, self.x, 0)

    def turn_left(self,evt):
        self.x = -5

    def turn_right(self,evt):
        self.x = 5

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

    ball.draw()                 #공 인스턴스의 draw메소드 실행(공이 벽에 부딪혀도 화면 밖으로 나가지 않게)
    ball.gameover()
    paddle.draw()               #패들을 키보드 방향키로 조정하면서 패들이 화면 밖으로 나가지 않게 실행
    tk.update_idletasks()       #tkinter에게 계속 화면을 그리라고 명령
    tk.update()                 #초기화
    time.sleep(0.02)
