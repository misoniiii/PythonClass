#4/25
######################중첩 gcd#####################################
def gcdtwo(a,b):                    # 두 수의 최대공약수를 출력
                                    # 분모가 0일경우 에러가 발생하므로 0인 경우를 따로 생각
    if min(a,b) == 0:               # 0과 A의 최대공약수는 무조건 A 이기 떄문에
        return max(a,b)             # 두 수중 최소값이 0인경우 두 수중 맥스값으로 최대공약수 출력
    return gcdtwo(b,a%b)            # 0이 아닌경우에 대해 유클리드호제법으로 재귀

def gcd(a):                         # 여러 수 중에서 최대공약수를 출력하는 알고리즘
    b=gcdtwo(max(a),min(a))         # 여러 수 중 두수를 뽑아서 최대공약수를 구하고
                                    # 다른 두수를 뽑아서 최대공약수를 구하고를 반복해서
    a.remove(min(a))                # 마지막에 남는 최대공약수가 전체의 최대공약수인 점을 이용
    a.remove(max(a))                # 정렬할 필요가 없게 전체 수에서 최대, 최소값을 뽑아서
                                    # 최대공약수를 구하는데 계산에 사용한 수는 제거하고
    a.append(b)                     # 위에서 구한 최대공약수를 리스트에 추가
    if max(a)==min(a):              # 위 과정을 재귀를 통해 반복하면 최대공약수만 2개 남는데
        print('최대공약수는 : ',a[0])  # 그경우에서 재귀를 종료하고 최대공약수를 출력
    else:
        gcd(a)


def list(*n):                       # 가변 매개변수로 데이터를 여러개 입력받으면
                                    # 튜플 형태이기 때문에 데이터 변경이 불가능
    a = []                          # 리스트를 생성하고 데이터 변경이 가능하도록
    for i in n:                     # 튜플 데이터를 잘라서 리스트에 입력
        a.append(i)
    gcd(a)                          # 최종적으로 생성한 리스트 변수를
                                    # 위에 생성한 최대공약수 함수에 입력해서 최대공약수 계산

if _name_=="_main_": #모듈을 불러올 때 이 문장 이후의 문장은 수행되지 않는다


######################탐욕쓰#####################################
def coinGreedy(money, cash_type):
    def coinGreedyRecursive(money, cash_type, res, idx):
        if idx >= len(cash_type): #화폐 다 사용 시 종료
            return res

        dvmd = divmod(money,cash_type[idx]) #divmond(362,100) => (3,62)
        res[cash_type[idx]] = dvmd[0]       #res[100] = 3
        return coinGreedyRecursive(dvmd[1],cash_type,res,idx+1)

    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬
    return coinGreedyRecursive(money,cash_type,{},0)

    #coinGreedyRecursive(362,[100,50,1],res,0) => 1 res= {}
    #coinGreedyRecursive(62,[100,50,1],res,1) => 2 res = {100:3}
    #coinGreedyRecursive(12,[100,50,1],res,2) => 3 res = {100:3, 50:1}
    #coinGreedyRecursive(0,[100,50,1],res,3) => 4 res ={100:3, 50:1, 1:12}


money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for key in res:
    print('{0}원 : {1}개'.format(key,res[key]))


######################표준편차#####################################
    #ex160)표준편차를 출력하는 함수를 모듈화 시켜서 다른 실행창에서 아래와 같이 실행하면 실행되게 하시오
# import std
# std.stddev(2.3, 1.7, 1.4, 0.7, 1.9)
import math

def stddev(*args):
    def mean():  # 평균구하는 함수
        return sum(args) / len(args)
    def variance(m):  # 분산을 구하는 함수
        total = 0
        for arg in args:
         total += (arg - m) ** 2  # (2.3-1.6)   + (1.7-1.6) + ......
        return total / (len(args) - 1)

    v = variance(mean())
    return math.sqrt(v)

#if __name__=="__main__":
 print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))



 ############4/26
 #ex165) 머신러닝 코드 입히기 전인 핑퐁 게임을 파이썬으로 구현하시오
from tkinter import *
import random
import time

class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #공 좌표 및 색깔(oval : object 형태 타입)
        self.canvas.move(self.id, 245, 100) #공을 캔버스 중앙으로 이동
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        #공의 속도
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) #공을 움직이게 하는 부분
        #공이 화면 밖으로 나가지 않게 해준다
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height: #바닥에 부딪히면 게임오버
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(pos) == True: #판에 부딪히면 위로 튕겨올라가게
            self.y = -3

class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -2

    def turn_right(self,evt):
        self.x = 2

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas,'blue')
ball = Ball(canvas, paddle, 'red')
start = False
#공을 약간 움직이고 새로운 위치로 화면을 다시 그리며, 잠깐 잠들었다가 다시 시작해라!
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    #그림을 다시 그려라! 라고 쉴새없이 명령
    tk.update_idletasks()
    tk.update()
    #시작 전 2초간 sleep
    if not start:
        time.sleep(2)
        start = True
    time.sleep(0.01)

###버블정렬
a = [10,5,8,9,20]
#      0 1 2 3 4

def insert_order(a):
    for i in range(len(a)-1):    # range(4)   --> i = 0    , i = 1       , i = 2
        for j in range(i+1):      # range(1)   --> j = 0, 1 , j = 0, 1, 2 , j = 0, 1, 2, 3
            if a[j]>=a[i+1]:
                temp = a[i+1]
                for k in range(i+1,j,-1) :
                   a[k] = a[k-1]
                a[j] = temp
    return a

###4/27
class grandfather:
    def __init__(self):
        print('튼튼한 두팔')
class father2(grandfather):
    def __init__(self):
        print('지혜')

father2 = father2()
#지혜 <-오버라이드 되어서 지혜만 나옴

#그런데 지혜도 중요하지만 건강도 중요하므로 할아버지의 건강도 물려받고 싶다면
class grandfather:
    def __init__(self):
        print('튼튼한 두팔')
class father2(grandfather):
    def __init__(self):
        super().__init__()
        print('지혜')
father2 = father2()
# 튼튼한 두팔
# 지혜

# super() 에 대하려
# 1. super()를 이용하면 부모 클래스의 멤버에 접근할 수 있다
# 2. super()를 이용하면 부모 클래스 명이 변경되어도 일일이 코드를 고치는 수고를 덜 수 있다
# 3. super()를 사용하면 죽음의 다이아몬드 상속을 피할 수 있다

#4/28
class onlyadmin(object): #함수에 들어가는 매개변수의 문자열을 받아서
    def __init__(self,func):    #대문자로 변환해주며 함수를 실행하는 클래스
        self.func = func

    def __call__(self,*arg,**kwargs): #클래스 자체는 결과값을 리턴하지 않지만 __call__ 을 쓰면 특정 메소드를 쓰지 않아도 결과값이 나옴
        name = kwargs.get('name').upper()
        self.func(name)
@onlyadmin
def greet(name):
    print("Hello {}".format(name))

greet(name = 'Scott') #Hello Scott

#ex176)위의 onlyadmin데코레이터를 활용해서 find_job이라는 함수를 강력하게 하시오
#@only_admin
#find_job(name='scott')
#당신의 직업은 ANALYST입니다
#1) import csv 버전

class onlyadmin(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        name = kwargs.get('name').upper()  # 함수에 들어가는 매개변수의 문자열을 받아서 대문자로 변환해주며
        return self.func(name)  # 처음의 함수를 실행하는 클래스

@onlyadmin
def find_job(name):
    import csv
    for emp_list in csv.reader(open('C:\data\emp.csv','r')):
        if emp_list[1] == name:
            return "당신의 직업은 {} 입니다.".format(emp_list[2])

print(find_job(name='king'))



#2) import pandas 버전
class onlyadmin(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        name = kwargs.get('name').upper()  # 함수에 들어가는 매개변수의 문자열을 받아서 대문자로 변환해주며
        return self.func(name)  # 처음의 함수를 실행하는 클래스

@onlyadmin
def find_job(name):
    import pandas as pd
    emp = pd.read_csv('C:\data\emp.csv')
    emp_result = emp['job'][emp['ename'] == name].values[0]
    return "당신의 직업은 {} 입니다.".format(emp_result)
print(find_job(name='king'))


2017년 4월 26일 수요일
오후 1:54

iterator는 next() 메소드로 데이터를 순차적으로 호출하는 object이다.

for i in range(5):
    print (i)

#range()로 생성된 list가 iterable하기 때문에 순차적으로 member들을 불러서 사용 가능했한 경우임

x = [1,2,3]
next(x)

type(x) # <class 'list'>

x = [1,2,3]
y=iter(x)
print(type(y))

print(next(y))
print(next(y))
print(next(y))