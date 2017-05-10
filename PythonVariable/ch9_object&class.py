# ###########################9.1 객체와 클래
# #ex)
# class Car():
#     def __init__(self):         #초기화 하는 함수
#         self.color = 0xFF000    #자동차 색상 (속성)
#         self.wheel_size = 16    #바퀴의 크기 (속성)
#         self.displacement = 2000 #엔진 배기량 (속성)
#     def forward(self):  #전진하는 기능
#         pass
#     def backward(self): #후진하는 기능
#         pass
#     def turn_left(self):    #좌회전
#         pass
#     def turn_right(self):   #우회전
#         pass
#
# if __name__ == '__main__': #메인 모듈일 때 아래 스크립트 실행
#     my_car = Car() #클래스를 인스턴스화 하는 코드 #Car()클래스로 my_car라는 객체 생성
#     print('0x{:02X}'.format(my_car.color)) #my_car에 대한 정보 출력
#     print(my_car.wheel_size)
#     print(my_car.displacement)
#     my_car.forward()    #my_car의 메소드(기능) 호출
#     my_car.backward()
#     my_car.turn_left()
#     my_car.turn_right()
#
# ###########################9.2 클래스의 정의
# # 클래스(자료형) --> 객체(변수)
# # 위의 클래스는 자료형이고 아직 객체가 되지 않았음
# #             ↓ 붕어빵틀    ↓
# #     (속성 : 붕어빵 색깔       붕어빵 (인스턴스, 실체라고 얘기함)
# #             붕어빵 앙금(팥, 슈크림)
# #     기능: 붕어빵이 움직인다고 보고
# #             왼쪽오른쪽으로 가라)
#
# # 코드설명
# # def __init__(self):
# #     1. __init__ ? 객체가 생성될 때 호출되는 메소드로서 객체의 초기화를 담당
# #     2. self ? 메소드의 첫번째 매개변수로서 객체 자신임을 나타냄
# #     3. my_car = Car()? car생성자는 car클래스의 인스턴스를 생성하여 반환
#
# ###########################9.3 __init__()
# #1. __init_-() 메소드 지정안했을 때
# class ClassVar:
#     text_list = [] #클래스의 정의 시점에서 바로 메모리에 할당됨
#     def add(self,text):
#         self.text_list.append(text)
#     def print_list(self):
#         print(self.text_list)
# if __name__ == '__main__':
#     a = ClassVar()  #위에서 만든 붕어빵 틀을 이용해서 a라는 붕어빵을 만듦
#     a.add('a') #a라는 인스턴스(객체)의 add기능을 작동시킴
#                 #a라는 붕어빵에 a(팥)을 넣음
#     a.print_list() #a라는 인스턴스(객체)의 print_list기능을 작동시킴 ['a]
#
#     b = ClassVar() #위에서 만든 붕어빵 틀을 이용해서 b라는 붕어빵을 만든다
#     b.add('b') #b라는 붕어빵에 b(아이스크림)을 넣는다
#
#     b.print_list() #출력 결과로 기대되는 것? ['b']
# # BUT, 결과로 이게 나옴
# # ['a']
# # ['a', 'b']
#
# #ex164) 책 192쪽을 보고 위의 코드에 초기화하는 코드를 추가해서 우리가 예상한 아래의 결과를 출력하시오
# # ['a']
# # ['b']
# #2. __init__() 메소드 지정
# class ClassVar:
#     def __init__(self):
#         self.text_list = []
#     def add(self,text):
#         self.text_list.append(text)
#     def print_list(self):
#         print(self.text_list)
# if __name__ == '__main__':
#     a = ClassVar()
#     a.add('a')
#     a.print_list()
#
#     b = ClassVar()
#     b.add('b')
#
#     b.print_list()
#
# #ex165) 머신러닝 코드 입히기 전인 핑퐁 게임을 파이썬으로 구현하시오
# from tkinter import *
# import random
# import time
#
# class Ball:
#
#     def __init__(self, canvas, paddle, color):
#         self.canvas = canvas
#         self.paddle = paddle
#         self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #공 좌표 및 색깔(oval : object 형태 타입)
#         self.canvas.move(self.id, 245, 100) #공을 캔버스 중앙으로 이동
#         starts = [-3, -2, -1, 1, 2, 3]
#         random.shuffle(starts)
#         #공의 속도
#         self.x = starts[0]
#         self.y = -3
#         self.canvas_height = self.canvas.winfo_height()
#         self.canvas_width = self.canvas.winfo_width()
#         self.hit_bottom = False
#
#     def hit_paddle(self,pos):
#         paddle_pos = self.canvas.coords(self.paddle.id)
#         if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
#             if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
#                 return True
#         return False
#
#     def draw(self):
#         self.canvas.move(self.id, self.x, self.y) #공을 움직이게 하는 부분
#         #공이 화면 밖으로 나가지 않게 해준다
#         pos = self.canvas.coords(self.id)
#         if pos[1] <= 0:
#             self.y = 3
#         if pos[3] >= self.canvas_height: #바닥에 부딪히면 게임오버
#             self.hit_bottom = True
#         if pos[0] <= 0:
#             self.x = 3
#         if pos[2] >= self.canvas_width:
#             self.x = -3
#         if self.hit_paddle(pos) == True: #판에 부딪히면 위로 튕겨올라가게
#             self.y = -3
#
# class Paddle:
#
#     def __init__(self,canvas,color):
#         self.canvas = canvas
#         self.id = canvas.create_rectangle(0,0,100,10,fill=color)
#         self.canvas.move(self.id, 200, 300)
#         self.x = 0
#         self.canvas_width = self.canvas.winfo_width()
#         self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
#         self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
#
#     def draw(self):
#         self.canvas.move(self.id, self.x, 0)
#         pos = self.canvas.coords(self.id)
#         if pos[0] <= 0:
#             self.x = 0
#         elif pos[2] >= self.canvas_width:
#             self.x = 0
#
#     def turn_left(self,evt):
#         self.x = -2
#
#     def turn_right(self,evt):
#         self.x = 2
#
# tk = Tk()
# tk.title("Game")
# tk.resizable(0, 0)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()
# paddle = Paddle(canvas,'blue')
# ball = Ball(canvas, paddle, 'red')
# start = False
# #공을 약간 움직이고 새로운 위치로 화면을 다시 그리며, 잠깐 잠들었다가 다시 시작해라!
# while 1:
#     if ball.hit_bottom == False:
#         ball.draw()
#         paddle.draw()
#     #그림을 다시 그려라! 라고 쉴새없이 명령
#     tk.update_idletasks()
#     tk.update()
#     #시작 전 2초간 sleep
#     if not start:
#         time.sleep(2)
#         start = True
#     time.sleep(0.01)
#
# ###########################9.4 self에 대한 이해
# #ex)
# class InstanceVar:
#     def __init__(self): #자기 자신을 초기화 하겠다
#         self.text_list = [] #클라스의 정의 시점에서 바로 메모리에 할당됨
#     def add(self,text): #자기 자신의 text_list리스트 변수를 가리킴
#         self.text_list.append(text)
#     def print_list(self): #자기 자신의 text_list변수를 가리킴
#         print(self.text_list)
#
# ###########################9.5 정적 메소드와 클래스 메소드
# class Calculator: #객체=속성+기능 기능만 4가지가 있는 클래스
#     @staticmethod   #정적메소드를 선언할 때 사용해야하는 데코레이터
#     def plus(a, b):
#         return a+b
#     @staticmethod
#     def minus(a, b):
#         return a-b
#     @staticmethod
#     def multiply(a, b):
#         return a*b
#     @staticmethod
#     def divide(a, b):
#         return a/b
#
# if __name__ == '__main__':
#     print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7, 4)))
#     print("{0} - {1} = {2}".format(7, 4, Calculator.minus(7, 4)))
#     print("{0} * {1} = {2}".format(7, 4, Calculator.multiply(7, 4)))
#     print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7, 4)))
#
# # Calculator.plus(7, 4) <- 정적 메소드를 호출하는 방법
# #   클래스       함수 : 클래스를 통해 메소드를 호출하고 있음
#
#
# ##########################9.6 클래스 내부에서만 열려 있는 프라이빗 멤버
# #ex) 퍼블릭 멤버로 사용했을 경우
# class Yourclass:
#     pass
# class Myclass:
#     def __init__(self):
#         self.message = 'HELLO'
#     def some_method(self):
#         print(self.message)
#
# obj = Myclass()
# obj.some_method() #HELLO : (프린트 실행하는)메소드를 실행 결과 출력
# print(obj.message) #HELLO : 따로 message라는 변수의 내용을 출력, __message__라고 안써줘도 퍼블릭
#
# # HELLO
# # HELLO
#
# #ex) private멤버로 변경했을 경우
# class Yourclass:
#     pass
# class Myclass:
#     def __init__(self):
#         self.message = 'HELLO'  #public
#         self.__private='private~~' #private
#     def some_method(self):
#         print(self.message)
#         print(self.__private)
#
# obj = Myclass()
# obj.some_method() #HELLO
#                   #private~~
#
# print(obj.message) #HELLO
# print(obj.__private) #에러 나옴:private멤버는 바로 접근할 수 없다

# ##########################9.7 상속
#ex1)
# class Father:
#     def base_method(self):
#         print('hello~')
# class Child(Father):
#     pass
#
# father = Father()
# father.base_method() #hello~
#
# child = Child()
# child.base_method() #hello ~
#
# ex2) __init__ 메소드를 실행하는데 부모와는 다르게 자식에 message라는 속성이 없어서 상속 시키고 싶을 때
# class Father:
#     def __init__(self):
#         print('hello~')
#         self.message = 'Good mornig'
# class Child(Father):
#     def __init__(self):
#         print('hello~i am child')
#
# child = Child() # hello~i am child
# father = Father()
# print(father.message)       # hello~
#                             # Good mornig
#
# #print(child.message) 안나옴!
#
#
# # #이걸 해결해주기 위해
# class Father:
#     def __init__(self):
#         print('hello~')
#         self.message = 'Good mornig'
# class Child(Father):
#     def __init__(self):
#         Father.__init__(self) #파이썬은 암묵적인 것을 싫어하고 명시적인 것을 좋아함
#         print('hello~i am child')
# #프로그래머가 명시적으로 클래스의 초기화 메소드를 호출해주기는 원함
#
# child = Child()
# father = Father()
#
# print(father.message)  # hello~
#                        # hello~i am child
#                        # hello~
# print(child.message) #Good morning

# class Father:
#     def __init__(self):
#         print('hello~')
#         self.message = 'Good mornig'
# class Child(Father):
#     def __init__(self):
#         super().__init__()
#         #father.__init__(self)
#         print("hello~ i am child")
#
# child = Child()
# print(child.message)

#다중상속
# class father1:
#     def func(self):
#         print('지식')
# class father2:
#     def func(self):
#         print('지혜')
# class child(father1,father2):
#     def childfunc(self):
#         father1.func(self)
#         father2.func(self)
#
# objectchild=child()
# objectchild.childfunc() #지식
#                         #지혜
# objectchild.childfunc() #지식 #물려받은 순서대로 나옴

# #다중상속 -- 다이아몬드 상속
# class grandfather:
#     def __init__(self):
#         print('튼튼한 두팔')
# class father1(grandfather):
#     def __init__(self):
#         grandfather.__init__(self)
#         print('지식')
# class father2(grandfather):
#     def __init__(self):
#         grandfather.__init__(self)
#         print('지혜')
# class grandchild(father1,father2):
#     def __init__(self):
#         super().__init__()
#         print('자기만족도가 높은 삶')
#
# grandchild=grandchild()
#
# # 튼튼한 두팔
# # 지식
# # 튼튼한 두팔
# # 지혜
# # 자기만족도가 높은 삶
# # 다이아몬드 상속을 받았더니 팔이 4개가 되어버렸다
#
# #ex166) 다시 팔이 2개가 되게 하시오(앞에서 배운 키워드를 사용하면 됨)
# class grandfather:
#     def __init__(self):
#         print('튼튼한 두팔')
# class father1(grandfather):
#     def __init__(self):
#         super().__init__()
#         print('지식')
# class father2(grandfather):
#     def __init__(self):
#         super().__init__()
#         print('지혜')
# class grandchild(father1,father2):
#     def __init__(self):
#         super().__init__()
#         print('자기만족도가 높은 삶')
#
# grandchild=grandchild()

# ##########################9.8 오버라이딩
# class grandfather:
#     def __init__(self):
#         print('튼튼한 두팔')
# class father2(grandfather):
#     def __init__(self):
#         print('지혜')
#
# father2 = father2()
# #지혜 <-오버라이드 되어서 지혜만 나옴
#
# #그런데 지혜도 중요하지만 건강도 중요하므로 할아버지의 건강도 물려받고 싶다면
# class grandfather:
#     def __init__(self):
#         print('튼튼한 두팔')
# class father2(grandfather):
#     def __init__(self):
#         super().__init__()
#         print('지혜')
# father2 = father2()
# # 튼튼한 두팔
# # 지혜
#
# # super() 에 대하려
# # 1. super()를 이용하면 부모 클래스의 멤버에 접근할 수 있다
# # 2. super()를 이용하면 부모 클래스 명이 변경되어도 일일이 코드를 고치는 수고를 덜 수 있다
# # 3. super()를 사용하면 죽음의 다이아몬드 상속을 피할 수 있다
#
# ##########################9.9 데코레이터
# #파이썬 함수의 특징
# #1. 함수에 할당할 수 있다
# #ex)
# def greet(name):
#     return "Hello {}".format(name)
#
# greet_someone = greet #함수를 변수에 할당 (어떻게 보면 함수 이름 바뀐 것 처럼 쓰임)
# print( greet_someone("scott"))
#
# #2. 다른 함수 내에서 정의할 수 있다
# def greeting(name):
#     def greet_message():
#         return 'Hello'
#     return "{} {}".format(greet_message(), name)
#
# print(greeting("scott"))
#
# #3. 함수의 인자매개변수로 전달할 수 있다
# def greet(name):
#     return "Hello {}".format(name)
# def change_name_great(func):
#     name="King"
#     return func(name)
#
# print(change_name_great(greet))
# #4. 함수의 반환값이 될 수 있음
# def greet(name): #이름을 넣으면 Hello를 앞에 붙여
#     return "Hello {}".format(name)
#
# def uppercase(func): #함수 매개변수로 받음(함수의 리턴값을 받아서 대문자로 출력해라
#     def wrapper(name): #대문자로 출력할는 기능에 충실한 함
#         result = func(name)  #greet("scott") ->Hello scott
#         return result.upper() #HELLO SCOTT
#     return wrapper
#
# new_greet = uppercase(greet)
# print(new_greet("scott"))
#
#ex167) 아래와 같이 이름을 입력하고 함수를 실행하면 해당하는 사원의 직업이 소문자로 출력되는 함수를 생성하시오
#함수1. 이름을 입력했을 때 직업이 출력되는 함수
#함수2. 문자를 입력했을 때 소문자로 출력하는 함수
#new_greet = lowercase(find_job)
#print( new_find_job('SCOTT'))

# import csv
# file = open('/Users/misoni/Desktop/pythondata/emp2.csv','r')
#
# def lowercase(func):
#     def wrapper(name):
#         result = func(name)
#         return result.lower()
#     return wrapper
#
# def find_job(name):
#
#     for i in csv.reader(file):
#         if name == i[1]:
#             return i[2]
#
# new_find_job = lowercase(find_job)
# print(new_find_job("SCOTT"))
#
# #1) print(new_find_job("SCOTT")
# #2) def find_job(name) :  name: SCOTT ->return값이 ANALYST
# #3) def lowercase(func):
# #   return wraapper  -->wrapper함수 실행
# #  --> def wrapper(name) : name: SCOTT
# #           result = func(SCOTT) ANALYST
# #           return result.lower() analyst
# # --->analyst값 반환
# # print(new_find_job("SCOTT") -> analyst
#
# #데코레이터 표현법을 보기 전에 먼저 데코레이터와 같은 역할을 하는 함수 생성
# class Greet(object):
#     current_user = None                 #current_user라는 변수 속성을 선언
#     def set_name(self,name):
#         if name == 'admin':             #name에 admin이라는 문자가 들어오면
#             self.current_user = name    #current_user에 admin이라는 문자를 담고
#         else:                           #admin이 아니라면 권한이 없다는 에러를
#             raise Exception('권한 없으요') #발생시키는 함수
#
#     def get_greeting(self,name):        #name이라는 매개변수에서 admin이
#         if name == 'admin':             #입력됐다면
#             return "Hello {}".format(self.current_user)
#                                         #Hello와 current_user를 리턴하는 함수
# #실행방법:
# greet = Greet()
# greet.set_name('admin')
# print(greet.get_greeting('admin'))
#
#
# # greet.set_name('scott')
# # print(greet.get_greeting('scott'))
#
# #ex168) 위의 코드에서 중복적으로 사용되는 코드를 떼어내서 함수로 생성하시오(중복되는 코드 admin이 맞는지 확인하는 코드
# def is_admin(user_name):
#     if user_name != 'admin':
#         raise Exception('권한이 음슴')
#
# class Greet(object):
#     current_user = None
#     def set_name(self,name):
#         is_admin(name)
#         self.current_user = name
#
#     def get_greeting(self,name):
#         is_admin(name)
#         return "Hello {}".format(self.current_user)
#
#                                         #Hello와 current_user를 리턴하는 함수
# #실행방법:
# greet = Greet()
# greet.set_name('admin')
# print(greet.get_greeting('admin'))
#
#
# greet.set_name('scott')
# print(greet.get_greeting('scott'))

# #ex169) 이름을 넣어서 함수를 실행하면 해당 사원의 월급이 출력되게 하는 함수를 생성하는데 king만 월급을 볼 수 있게 하고
# #king이 아닌 다른 사원들은 권한이 없다면서 볼 수 없게 에러가 나게 하시
# import csv
# file = open('/Users/misoni/Desktop/pythondata/emp2.csv','r')
#
#
# def is_admin(user_name):
#     if user_name != 'KING':
#         raise Exception('요놈 KING만 볼 수 있느니라')
#
# class Find_sal(object):
#     current_user= None
#     def set_name(self,name):
#         is_admin(name)
#         self.current_user = name
#
#     def get_sal(self, name):
#         is_admin(name)
#         for i in csv.reader(file):
#             if i[1] == name:
#                 return i[5]
#
# find_sal = Find_sal()
# find_sal.set_name('KING')
# print(find_sal.get_sal('KING'))

# #ex170) 위에 is_admin(name)이라는 함수를 사용해서 코드가 더 좋아졌다
# #하지만 데코레이터를 쓰면 더 좋은 코드가 될 수 있다
# #데코레이터를 써서 구현하시오(ex168코드 이용)
#
# #데코레이터 생성(구문 외우기) #뭐가 잡히는 지 디버깅해서 프린트 해볼 것
# def is_admin(func):
#     def wrapper(*arg, **kwargs): # *: 리스트의 가변 매개변수
#                                  # ** :딕셔너리 가변 매개변수
#         if kwargs.get('name') != 'admin':
#             raise Exception('권.한.없.음')
#         return func(*arg, **kwargs)
#     return wrapper
# #
# class Greet(object):
#     current_user = None
#     @is_admin
#     def set_name(self,name):
#         self.current_user = name
#     @is_admin
#     def get_greeting(self,name):
#         return "Hello {}".format(self.current_user)
#
# greet =Greet()
# greet.set_name(name='admin')
# print(greet.get_greeting(name='admin'))
#
#
# #ex171) ex169코드를 데코레이터 함수를 이용해서 더 좋게 개선하시오
# # find_sal = find.sal()
# # find_sal.set_name(name='scott')
# # print(find_sal.get_sal(name='scott'))
#
# import csv
# file = open('/Users/misoni/Desktop/pythondata/emp2.csv','r')
#
#
# def is_admin(func):
#     def wrapper(*arg, **kwargs):
#         if kwargs.get('name') != 'KING':
#             raise Exception('권한이 없습니다')
#         return func(*arg, **kwargs)
#     return wrapper
#
# class Find_sal(object):
#     current_user= None
#     @is_admin
#     def set_name(self,name):
#         self.current_user = name
#     @is_admin
#     def get_sal(self, name):
#         for i in csv.reader(file):
#             if i[1] == name:
#                 return i[5]
#
# find_sal = Find_sal()
# #find_sal.set_name(name = 'KING') #name 을 써주면 name이 딕셔너리 키가 되어서
#                                 # def is_admin에서 **kargs(딕셔너리 매개변수)로 들어감
# find_sal.set_name( 'KING')
# print(find_sal.get_sal(name ='KING'))
#


# ex172) gun이라는 인스턴스를 생성하기 위해서 gun() 클래스를 생성하시오
# gun = Gun() #총 설계도로 총을 실체화시킴
# gun.charge(10) #총알 10발 충전
# gun.shot(3)
# 탕
# 탕
# 탕
# 7발 남았습니다
# gun.print() #현채 총알이 얼마나 남았는지 확인
# 7발 남았습니다
#
# 클래스 = 변수  + 기능
#         총알   충전,쏘기,프린트

# class Gun():
#     def __init__(self):
#         self.bullet = 0
#
#     def charge(self,num): #장전하는 기능
#         self.bullet = num
#
#     def shoot(self,num): #쏘는 기능
#         for i in range(num):
#             if self.bullet > 0:
#                 print('탕!')
#                 self.bullet -= 1
#
#             elif self.bullet == 0:
#                 print('총알이 없습니다 장전하세요')
#                 break
#
#     def print(self):   #출력하는 기능
#         print( '{}발 남았습니다'.format(self.bullet))
#
# gun = Gun()
# gun.charge(10)
# gun.shoot(3)
# gun.print()

# #ex2) 클래스를 사용하는 이유
# #-딕셔너리를 사용하는 경우
# student = {'name':'김인호','year':2, 'class':3, 'student_id':35}
# print ('{}, {}학년 {}반 {}번'.format(student['name'],student['year'],student['class'],student['student_id']) )
#
# #결과 : 김인호, 2학년 3반 35번
#
# #-클래스 사용하는 경우
# class Student(object):
#     def __init__(self,name,year,class_num, student_id):
#         self.name = name
#         self.year = year
#         self.class_num =class_num
#         self.student_id =student_id
#
#     def introduce_myself(self):
#         return '{}, {}학년 {}반 {}번'.format(self.name, self.year, self.class_num, self.student_id)
#
# student = Student('김인호',2,3,35)
# print( student.introduce_myself() )
#
# #ex173) 위의 student 클래스를 다시 실행하는데 self를 빼고 실행해보시오
# class Student(object):
#     def __init__(self,name,year,class_num, student_id):
#         self.name = name
#         self.year = year
#         self.class_num =class_num
#         self.student_id =student_id
#
#     def introduce_myself(): #self가 없습니다
#         return '{}, {}학년 {}반 {}번'.format(self.name, self.year, self.class_num, self.student_id)
#
# student = Student('김인호',2,3,35)
# print( student.introduce_myself() )

#ex173) 자기 자신이 인스턴스의 메소드 인자에 전달된다는 것이 어떤것인지 인스턴스를 통하지 않고
# 바로 클래스의 introduce_myself를 직접 호출해서 확인하시오
# class Student(object):
#     def __init__(self,name,year,class_num, student_id):
#         self.name = name
#         self.year = year
#         self.class_num =class_num
#         self.student_id =student_id
#
#     def introduce_myself(self):
#         return '{}, {}학년 {}반 {}번'.format(self.name, self.year, self.class_num, self.student_id)
#
# student_1 = Student('김인호',2,3,35) #실체화된 인스턴스
# print( student_1.introduce_myself() )    #인스턴스 통해서 출력 ,자기자신(student_1)이 introduce_myself(self)에 쏙 들어감
# print( Student.introduce_myself(student_1)  ) #클래스를 통해서 출력 introduce_myself(self)에 매개변수 넣는데가 있길래 직접 넣어줌
#
#
# ###Static method
# class Gun():
#     def __init__(self):
#         self.bullet = 0
#
#     def charge(self,num): #장전하는 기능
#         self.bullet = num
#
#     def shoot(self,num): #쏘는 기능
#         for i in range(num):
#             if self.bullet > 0:
#                 print('탕!')
#                 self.bullet -= 1
#
#             elif self.bullet == 0:
#                 print('총알이 없습니다 장전하세요')
#                 break
#
#     def print(self):   #출력하는 기능
#         print( '{}발 남았습니다'.format(self.bullet))
#
# gun1 = Gun()
# gun1.charge(10)
# gun1.shoot(3)
# gun1.print()
#
# gun2 = Gun()
# gun2.charge(10)
# gun2.shoot(6)
# gun2.print()
#
# #설명 : gun1총과 gun2총은 서로 별개의 총
# #같은 설계도를 사용했지만 별개의
# #별개의 총이 맞는지 확인해 본다
#
# print(gun1)
# print(gun2)
#
# # <__main__.Gun object at 0x10206bcc0>
# # <__main__.Gun object at 0x10206bd30>
# #메모리 주소가 서로 다름
#
# print(gun1.__class__)
# print(gun2.__class__)
# # <class '__main__.Gun'>
# # <class '__main__.Gun'>
# #설계도는 같음

#-->둘은 메모리 주소값을 가지고 있어서 같은 클래스를 쓰는 서로 별개의 오브젝트라는 것을 확인함

# #ex174) gun class의 메소드들을 static method들로 변경해서 다시 총을 쏘시오
# class Gun1(): #static method
#     bullet = 0
#     @staticmethod
#     def shoot(num):
#         for i in range(num) :
#             if Gun1.bullet>=1 :
#                 print('탕!')
#                 Gun1.bullet -= 1
#             elif Gun1.bullet == 0 :
#                 print('총알이 없습니다!')
#                 break
#     @staticmethod
#     def charge(num):
#         Gun1.bullet = num
#         print('{} 발이 장전되었습니다.'.format(num))
#     @staticmethod
#     def print():
#         print('{} 발 남았습니다.'.format(Gun1.bullet))
#
# class Gun2():
#     def __init__(self):
#         self.bullet = 0
#     def shoot(self, num):
#         for i in range(num) :
#             if self.bullet>=1 :
#                 print('탕!')
#                 self.bullet -= 1
#             elif self.bullet == 0 :
#                 print('총알이 없습니다!')
#                 break
#     def charge(self, num):
#         self.bullet = num
#         print('{} 발이 장전되었습니다.'.format(num))
#     def print(self):
#         print('{} 발 남았습니다.'.format(self.bullet))
#
#
# print('Gun1 class\n')
# print('gun0')
# gun0 = Gun1()
# gun0.charge(10)
# gun0.shoot(3)
# gun0.print()
#
# print('\ngun1')
# gun1 = Gun1()
# gun1.shoot(3)
# gun1.print()
#
# print('\nGun2 class\n')
# print('gun2')
# gun2 = Gun2()
# gun2.charge(10)
# gun2.shoot(3)
# gun2.print()
#
# print('\ngun3')
# gun3 = Gun2()
# gun3.charge(10)
# gun3.shoot(3)
# gun3.print()
#
#
# #ex175) static method로 선언한 클래스를 이용해서 인스턴스화 한 두개의 총이 쏘는 메소드(shoot)가 서로 같은 메모리를 쓰는지 확인하시오
# print(gun0.shoot) # <function Gun1.shoot at 0x102061510>
# print(gun1.shoot) # <function Gun1.shoot at 0x102061510> #static method
# #--->같은 메모리 사용
# print(gun2.shoot) # <bound method Gun2.shoot of <__main__.Gun2 object at 0x10206bfd0>>
# print(gun3.shoot)   # <bound method Gun2.shoot of <__main__.Gun2 object at 0x10206bf60>>
# #-->다른 메모리 사용

# ################9.10 마법의 __call__메소드
# #ex1)
# class Sample(object):
#     def __init__(self):
#         print('생성하면 바로 실행')
# sample = Sample()
#
# #ex2)
# class Sample2(object):
#     def __call__(self):
#         print('인스턴스에 괄호를 붙이면 실행')
# sample2 = Sample2()
# sample2() #인스턴스는 함수가 아닌데 함수처럼 호출하기 위해 __call__이라는 메소드 정의
#
# # 클래스의 인스턴스를 함수처럼 호출하기 위해서
# # 클래스의 __call__이라는 매직 메소드를 정의
# #이 원리를 이용해서 클래스를 데코레이터로 구현할 수 있다
# #어제 우리가 데코레이터로 구현한 건 클래스가 아니라 함수였음
#
# #클래스를 데코레이터로 구현하는 예제
# from functools import wraps
#
# class onlyadmin(object): #함수에 들어가는 매개변수의 문자열을 받아서
#     def __init__(self,func):    #대문자로 변환해주며 함수를 실행하는 클래스
#         self.func = func
#
#     def __call__(self,*arg,**kwargs): #클래스 자체는 결과값을 리턴하지 않지만 __call__ 을 쓰면 특정 메소드를 쓰지 않아도 결과값이 나옴
#         name = kwargs.get('name').upper()
#         self.func(name)
# @onlyadmin
# def greet(name):
#     print("Hello {}".format(name))
#
# greet(name = 'Scott') #Hello Scott
#
#
# #ex176)위의 onlyadmin데코레이터를 활용해서 find_job이라는 함수를 강력하게 하시오
# #@only_admin
# #find_job(name='scott')
# #당신의 직업은 ANALYST입니다
# #1) import csv 버전
#
# class onlyadmin(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         name = kwargs.get('name').upper()  # 함수에 들어가는 매개변수의 문자열을 받아서 대문자로 변환해주며
#         return self.func(name)  # 처음의 함수를 실행하는 클래스
#
# @onlyadmin
# def find_job(name):
#     import csv
#     for emp_list in csv.reader(open('C:\data\emp.csv','r')):
#         if emp_list[1] == name:
#             return "당신의 직업은 {} 입니다.".format(emp_list[2])
#
# print(find_job(name='king'))
#
#
#
# #2) import pandas 버전
# class onlyadmin(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         name = kwargs.get('name').upper()  # 함수에 들어가는 매개변수의 문자열을 받아서 대문자로 변환해주며
#         return self.func(name)  # 처음의 함수를 실행하는 클래스
#
# @onlyadmin
# def find_job(name):
#     import pandas as pd
#     emp = pd.read_csv('C:\data\emp.csv')
#     emp_result = emp['job'][emp['ename'] == name].values[0]
#     return "당신의 직업은 {} 입니다.".format(emp_result)
# print(find_job(name='king'))


# ############################9.11 for문으로 순회할수 있는 객체만들기
# for i in range(5):
#     print (i)
#
# #range()로 생성된 list가 iterable하기 때문에 순차적으로 member들을 불러서 사용 가능했한 경우임
#
# x = [1,2,3]
# next(x)
#
# type(x) # <class 'list'>
#
# x = [1,2,3]
# y=iter(x)
# print(type(y))
#
# print(next(y))
# print(next(y))
# print(next(y))
#

#
# ############################9.12 추상 기반 클래스
# from abc import ABCMeta, abstractmethod #파이썬은 추상클래스르 제공하지 않아서 import받아야함
#
# class Animal(object):
#     __metaclass__ = ABCMeta #추상 클래스로 선언
#
#     @abstractmethod #추상 메소드 선언
#     def bark(self):
#         pass #비어있는 메소드, 중요한 메소드
#
# class Cat(Animal):
#     def __init__(self):
#         self.sound = '야옹'
#     def bark(self):
#         return self.sound
#
#
# class Dog(Animal):
#     def __init__(self):
#         self.sound = '멍멍'
#     def bark(self):
#         return self.sound
#
# cat = Cat()
# dog = Dog()
#
# print(cat.bark()) #야옹
# print(dog.bark()) #멍멍

#ex177)음료(beverage)라는 추상 클래스를 생성하고 아메리카노와 카페라테 클래스를 자식 클래스로 구성하시오

from abc import ABCMeta, abstractmethod #파이썬은 추상클래스르 제공하지 않아서 import받아야함

class Beverage(object):
    __metaclass__ = ABCMeta #추상 클래스로 선언

    @abstractmethod #추상 메소드 선언
    def buy(self):
        pass #비어있는 메소드, 중요한 메소드

class Americano(Beverage):
    def __init__(self):
        self.cost= '$3.5'
    def buy(self):
        return self.cost


class Cafelatte(Beverage):
    def __init__(self):
        self.cost = '$4'
    def buy(self):
        return self.cost

ame = Americano()
latte = Cafelatte()

print(ame.buy())
print(latte.buy())