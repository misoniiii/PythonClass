######################################################################
######################   7.1 함수 생성
######################################################################
# def 함수이름(매개변수):
#     실행문
#     결과

#ex
def my_abs(arg):
    if (arg < 0 ):
        result = arg * -1
    else:
        result = arg
    return result

print(my_abs(-5))

#ex146) 아래와 같이 이름을 입력해서 함수를 실행하면 해당사원의 부서위치가 출력되게 하시오
#print( find_loc('SMITH'))
#dallas
import pandas as pd
def find_loc(val):
    emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
    dept = pd.read_csv("/Users/misoni/Desktop/pythondata/dept.csv")
    result = pd.merge(emp,dept,on='deptno')
    result2 = result[['loc']][result['ename'] == val]
    return result2

print(find_loc('SMITH'))

#ex147) 미분계수를 구하는 함수를 생성하는데 x가 -2일때의 기울기(미분계수)를 구하시오
#2x^2+1
def diff(x):
    h = 0.00001
    return 2*(pow((x+h),2)-pow((x-h),2))/(2*h)

print(diff(-2))
###############################7.2 기본값 매개변수와 키워드 매개변수
def print_string(text,count=1): #디폴트값을 원할때는 ' = 값' 써주면 됨
    for i in range(count):
        print(text)
    return ''
print_string('안녕하세요')
print_string('안녕하세요',3) #함수 생성시 print(text)로 해줘야  count만큼 나옴(none안나오게 하려면 return ''으로)

#ex149) 아래와 같이 이름만 넣으면 소속팀과 직위가 출력되는 함수를 생성하시오
# print_inform(name='장경원')
# 이름=장경원
# 소속팀=머신러닝팀
# 직위 = 팀원 (매개변수)
# print_inform(name='장경원',position='팀장')

def print_inform(name,position='팀원',team='머신러닝팀'):
    print('name = {0}'.format(name) )
    print('position = {0}'.format(position))
    print('team = {0}'.format(team))

print_inform('장경원')
print_inform('장경원','팀장')

###############################7.3 가변 매개변수
def merge_string(*text_list):
    result = ''
    for s in text_list:
        result += s + ' '
    return result

merge_string('아버지가','방에','들어가신다')

# ◼︎ 파이썬에서 *가 쓰이는 경우
# 1. 가변 매개변수
# 2. 리스트 변수 내의 요소들을 뽑아낼 때-->mit코드

######################################################################
######################  7.4 매개변수로 함수를 사용하는 경우
######################################################################

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / 2*h

def function_1(x): #2x^2 +1 함수 생성
    return 2*pow(x,2)+1

print ( numerical_diff( function_1, -2 ) ) # 이해가 안가영 function_1(x)에 x에 뭘 넣어줘야하지 않나

#ex148) 함수 f(x) = x^2-x+5 함수의 x가 -2일때 미분계수를 구하시오
def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / 2*h

def function_1(x): #2x^2 +1 함수 생성
    return pow(x,2)-x+5

print ( numerical_diff( function_1, -2 ) )

#함수 종료의미로 retrun을 사용하는 경우
def stop_func(num):
    for i in range(1,num+1):
        print('숫자 {0}을 출력합니다'.format(i))
        if i == 5:
            retrun #리턴 뒤에 아무것도 안적어주면 함수 종료 #break랑 뭐가 다른가
stop_func(10)

#ex151)아래와 같이 숫자를 입력하고 함수를 실행하면 숫자가 세로로 출력되게 하시오
#print_something(1,2,3,4,5) #얼마든지 숫자를 쓸 수 있어야함

def print_someting(*num_list):
    for i in num_list:
        print(i)
    return

print_someting(1,2,3,4,5,6,7,8,9) #이건 왜 none이 안나오지->오홍 함수라서 print일때만


###############################7.5 함수 안의 변수 함수 밖의 변수
#로컬변수 선언
def scope_test():
    a=1 #함수 내에서 사용하는 변수(로컬변수
    print('a:{0}'.format(a))

a=0
scopt_test()
print('a:{0}'.format(a))


#ex152) 위의 스크립트에서 마지막 scope_test()를 실행했을 때 a가 1이 아니라 0이 출력이 되려면 scope_test()함수를 생성할 때 어떻게 생성해야 했는가
#글로벌 변수 선언
def scope_test():
    global a #글로벌 변수로 선
    a = 1 #함수 내에서 사용하는 변수(로컬변수
    print('a:{0}'.format(a))

a= 0
scopt_test()
print('a:{0}'.format(a)) #a:0



def  scope_test():
             global a
             a = 1   # 함수 내에서 사용하는 변수(로컬변수)
             print ('a : {0}'.format(a) )
a = 0
scope_test()
print ('a : {0}'.format(a) )


###############################7.6 재귀함수
#재귀함수는 함수내에서 다시 자신을 호출한후 그 함수가 끝날 때 까지 함수 호출이후의 명령문이 수행되지 않는다

def some_func(count):
    if count > 0:
        print(count) #쌓는 거
        some_func(count-1)
    print(count) # 빼내는 거

print(some_func(10))

#10 ---> call하고 기다림->기다림이 끝나면 print10
#9 --->call하고 기다림 -> 기다림이 끝나면 print9
#                                         (3)
#                                  print1 (2)
#0 ---->함수 호출 끝                  print0 (1)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# None

#ex153) 10!를 재귀함수로 구현해서 출력하시오
#print(factorial2(10))
#10*9*8*7*6*5*4*3*2*1
def factorial(num):                         #10
    if num > 1:
        return factorial(num-1) * num       #10-1=9
    elif num == 1:
        return 1

print(factorial(5))

#10*9*8*7*6*5*4*3*2*1
#               <----


def factorial(num):
    if num > 1:
        num *= factorial(num-1)
    return num

print(factorial(5))

#ex154)16과 20의 최대공약수를 출력하는데 재귀함수를 이용해서 구현하시오
print(find_gcd(20,16))

def find_gcd(num1, num2):
    c = num1%num2
    if num2%c == 0:
        print(c)
    else:
        find_gcd(num2, c)
print(find_gcd(24,36))

#ex155)인자값을 3개 받아서 최대 공약수를 출력하시오(재귀함수 구현
#print(find(20,16,4))
#최대공약수는 4입니다

# 오답
# def gcd(n1, n2, n3):
#     res = n1%n2%n3
#     if res != 0:
#         res = n1%n2%n3
#         return gcd(n2,n3,res)
#     else:
#         return n3
#
# print(gcd(1000,700,72))

