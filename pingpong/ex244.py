# 스페이스바 누르면 시작하도
from tkinter import *
import random
import time

class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                                   #  서  남  동  북
        canvas.configure(background='black')
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)

        self.canvas.bind_all('<space>', self.start)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False  # 바닥에 닿으면(True) 게임 끝나는 코드
        self.isMiss = False

    def start(self,evt):
        self.x = random.sample(range(-5,6),1)
        self.y = 5
    def turn_left(self,evt):
        self.x = -9
    def turn_right(self,evt):
        self.x = 9
    def turn_up(self,evt):
        self.y = -9
        self.x = random.sample(range(-3,4),1)
    def turn_down(self,evt):
        self.y = 9
    def gameover(self):
        pos = self.canvas.coords(self.id)
        if self.hit_paddle(pos) == True :
            print('hit')
        elif pos[3]>=400 and self.y >= 0 and self.isMiss == False:
            self.isMiss = True
            print('miss')
        elif self.y< 0 and pos[3]>400 :
            self.isMiss = False

    def gameover(self):
        pos = self.canvas.coords(self.id)
        if pos[1] < 400 < pos[3] and self.isMiss == False and self.y > 0:
            self.isMiss = True
            print('miss')
        elif pos[1] > 400 or pos[3] < 400:
            self.isMiss = False


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 5
        if self.hit_paddle(pos) == True:
            self.y = -5
        if pos[0] <= 0:
            self.x = 5
        if pos[3] >= self.canvas_height:
            self.y = -5
        if pos[2] >= self.canvas_width:
            self.x = -5
        if self.hit_paddle(pos) == True:
            self.y = -(5+ abs(paddle.y))


    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False


class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,200,10,fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)

    def draw(self):

        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 and self.x <0:
            self.x = 9
            return
        elif pos[2] >= self.canvas_width and self.x > 0:
            self.x = -9
            return
        self.canvas.move(self.id, self.x, self.y)

    def turn_up(self,evt):
        self.y = -9
    def turn_down(self,evt):
        self.y = 9
    def turn_left(self,evt):
        self.x = -9
    def turn_right(self,evt):
        self.x = 9

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
    ball.gameover()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)