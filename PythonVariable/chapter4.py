# -*- coding: utf-8 -*-
#####Chap4. 데이터 다루기

# ex1) 위의 d 리스트 변수에서 1000을 출력하시오
d = [1000, 2000, 3000, 4000]
print(d[0])

# ex2) d리스트 변수안에 있는 요소들을 하나씩 출력하시오
d = [1000, 2000, 3000, 4000]
for i in d:  # 변수명
    print(i)

for i in range(100):
    print(i)  # 0~99까지 100개 출력됨
    # 설명: 파이썬은 세미콜론을 사용하지 않고 그냥 콜론 사용
    # 반드시 콜론을 써줘야하는 문법
    ##IF, WHILE LOOP, FOR LOOP, def 함수 생성 시 사용

# ex3) a라는 리스트변수에 아래의 내용을 담고 출력하시오
a = ['7839', 'KING', 'PRESIDENT', '0', '1981-11-17', '5000', '', '10']
print(a)

# ex4)a라는 변수안에 잇는 요소들을 끄집어 내서 출력하시오
for i in a:
    print(i)

# ex5) a 리스트 변수에서 7839만 출력하시오
print(a[0])

##len함수
a = ['7839', 'KING', 'PRESIDENT', '0', '1981-11-17', '5000', '', '10']
cnt = len(a)
print(cnt)

# none(오라클의 null)

# ex6) 카페에서 파이썬 수업자료에 emp2.csv를 내려받아 D드라이브 밑에 data라는 폴도에 다운받고 아래와 같이 수행
import csv  # csv모듈(아나콘다 내장) inport

file = open("D:\data\emp2.csv", 'r')  # r:  read
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list)
# ex7)위의 결과에서 사원번호만 출력하시오
import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[0])

# ex8)이름과 월급을 출력하시오
import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5])

# ex9) 위의 14개 리스트 변수 요소의 개수를 아래와 같이 출력하시오
# 결과
# 8
# 8(14개)
import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(len(emp_list))

# ex10)이름과 이름의 길이를 아래와 같이 출력하시오
import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], len(emp_list[1]))

# ex11) 사원번호, 이름, 월급 출력
import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[0], emp_list[1], emp_list[5])

# ex12) 이름과 연봉을 출력하시오
# csv에서 불러오는 데이터는 기본적으로 문자라서 변환을 해줘야함
import csv

file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], int(emp_list[5]) * 12)


# ex13)이름과 커미션을 출력하는데 커미션이 none이면 0으로 출력하시오
def ifnull(var, val):
    if var is '':
        return val
    return var


import csv

file = open("D:\data\emp_comm.csv", 'r')
emp_comm_csv = csv.reader(file)
for emp_list in emp_comm_csv:
    print(emp_list[1], ifnull(emp_list[6], 0))


# ex14)이름, 월급+커미션 출력
def ifnull(var, val):
    if var is '':
        return val
    return var


import csv

file = open("D:\data\emp_comm.csv", 'r')
emp_comm_csv = csv.reader(file)
for emp_list in emp_comm_csv:
    print(emp_list[1], int(emp_list[5]) + int(ifnull(emp_list[6], 0)))

# ex15) 이름과 직업을 출력하는데 소문자로 출력하시오
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1].lower(), emp_list[2].lower())

# ex16) MIT TTT 코드이해를 위해 중요한 기초 문제
# 이름을 출력하는데 이름의 첫번째 철자만 출력하고, 소문자로 출력하시오
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0].lower())

# ex17)이름을 출력하는데 이름의 두번째 철자부터 마지막까지 소문자로 출력
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][1:].lower())

slicing = ['01234567890', 'abcdefghi', '0123abcdefghi']
print(slicing[0:][1])


# ex18)이름의 첫번째 첫자는 대문자로 출력하고 나머지는 소문자로 출력하시오
def initcap(val):
    return val[0].upper() + val[1:].lower()


import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(initcap(emp_list[1]))

# ex19) 이름의 첫번째 철자부터 세번째 철자까지 출력되게 하시오

import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0:3])


# ex20)이름의 첫번째 철자부터 세번째 철자가 출력되게 하는데 substr함수를 만들어서 출력되게 하시오
def substr(var, num1, num2):
    return var[num1 - 1:num2]


file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(substr(emp_list[1], 1, 3))

# ex21)이름과 월급을 출력하는데 월급을 출력할 때 0대신에 *를 출력하시오
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5].replace('0', '*'))

# ex22)이름과 월급을 출력하는데 월급을 출력할 대 0~2를 *로 출력하시오
# [re 정규식함수]
# sub(pattern,repl, string)
# string에서 pattern과 일치하는 부분에 대해서 repl로 교체
import re  # 정규식 모듈 import
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], re.sub('[0-2]', '*', emp_list[5]))

# ex23)이름과 이름의 길이 출력
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    print(emp_list[1], len(emp_list[1]))

# ex24)아래의 split함수의 예제를 수행해보시오
file = 'a b c d e f g'
print(file.split(' '))  # 공백으로 분리해서 리스트 생성

# ex25) 아래의 file변수의 요소들을 리스트변수로 담아내서
# 두번째 요소인 b만 출력
file = 'a b c d e f g'
print(file.split(' ')[1])

# ex26)겨울왕국 대본을 공백을 구분으로 누고 나눠서 리스트 변수로 저장되게 하시오
file = open("D:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:
    print(winter_list.split(' '))

# ex27) 위의 스크립트를 이용해서 겨울왕국 각 리스트 변수 안에 단어가 몇개가 있는지 아래와 같이 출력되게 하시오

file = open("D:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')
    print(len(a))

# ex28)위의 숫자들을 다 더한 값을 출력하시오
sum = 0
file = open("d:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')
    sum = sum + len(a)
print(sum)

# ex29)겨울왕국에서 elsa가 몇번 나오는지 확인
# 예제
a = 'Hello'
b = a.count('l')
print(b)

sum = 0
file = open("d:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')
    sum = sum + a.count('Elsa')
print(sum)

# ex30)emp.csv에서 14개의 리스트 변수 중에 5번째 요소(월급) 부분만 담아서 리스트 변수로 아래와 같이 생성하시오
# append()
# [5000,2850,5450,......,1300]
# ex)
a = [1, 2, 3]
b = a.append(4)
print(a)

# ex)
b = []
b.append(1)
b.append(2)
b.append(3)
print(b)

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
b = []
for emp_list in emp_csv:
    b.append(int(emp_list[5]))
print(max(b))

# ex31)겨울왕국 대본을 단어별로 출력하시오
# ['anna','elsa','She','YOu']
# ['anna','elsa','She','YOu','ORDERS']
#       for loop            for loop
# txt-------------->list변수-------------> 하나의 단어
# ex)하나의 단어
a = ['anna', 'elsa', 'She', 'YOu']
for i in a:
    print(i)

file = open("d:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:  # file:스크립트
    a = winter_list.split(' ')  # 면 리스트가 나옴
    print(a)
    for word in a:  # 리스트일 때  for 돌리면
        print(word)  # 단어가 나옴

# ex32)31번의 결과르 하나의 리스트로 만드시오
b = []
file = open("d:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:  # 스크립트-->리스트변수
    a = winter_list.split(' ')

    for word in a:  # 리스트변수 ->단어만 추출
        b.append(word)
print(b)

# ex33)출력된 단어들 중에 \n은 잘라내시오
b = []
file = open("d:\data\겨울왕국_대본.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')

    for word in a:
        no_n = word.strip('\n')
        print(b.append(no_n))
print(b)


# ex34) rpad함수를 생성하고 아래와 같이 실행되게 하시오
# 월급을 출력할때 전체 10자리를 잡고 남은 왼쪽에 *를 채워넣으시오
def rpad(var, num, val):
    for _ in range(num - len(var)):
        var = var + val
    return (var)


def lpad(var, num, val):
    for _ in range(num - len(var)):
        var = val + var
    return (var)


file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], lpad(emp_list[5], 10, '*'))


########4/17
# ex35)instr함수를 파이썬으로 구현하시오
def instr(word, target):
    for i in range(0, len(word)):
        if word[i] == target:
            return i + 1


# ex36)이름, 이름에 M자가 몇번째 자리에 있는지 출력하시오
import csv


def instr(word, target):
    for i in range(0, len(word)):
        if word[i] == target:
            return i + 1


file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], instr(emp_list[1], 'M'))  # 대문자 조심쓰

# ex37)이름,월급,보너스를 출력하는데 보너스는 월급의 15퍼센트로 출력하시오
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], round(int(emp_list[5]) * 0.15))

# ex38) 위의 결과르 다시 출력하는데 컬럼명도 출력되게 하시오
import csv

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
print('이름', '월급', '보너스')
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], round(int(emp_list[5]) * 0.15))

# ex39)위의 결과를 다시 출력하는데 소숫점이하는 안나오고 반올림 되게 하시오
# ex40) 보너스를 출력할 때 소숫점 이하를 trunc를 써서 잘라내시오
import csv
import math

file = open("d:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
print('이름', '월급', '보너스')
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], math.trunc(int(emp_list[5]) * 0.15))

# ex41)input명령어를 이용해서 숫자를 입력받아 해당 숫자가 짝수인지 홀수인지 출력되게 하시오
a = input('첫번째 숫자 입력')
b = input('두번째 숫자 입력')

result = int(a) + int(b)  # 문자형일 경우 연결 연산자., 숫자형 변환 해줘야함!!
print(result)

c = int(input('숫자 입력하세요'))  # 매번 써줘야 하니까 여기다가
if c % 2 == 0:  # % 나머지
    print('짝수')
else:
    print('홀수')

# ex42) power함수를 이용해서 아래의 프로그램을 구현사시오
# 숫자를 입력하세요! 2
# 숫자를 입력하세요! 3
# 8입니다
a = int(input('밑을 입력하세요'))
b = int(input('지수를 입력하세요'))

print(pow(a, b))

# ex43) 오늘 날짜를 출력하시오
import datetime

today = datetime.date.today()
print(today)

#
from datetime import date

print(date.today())

# ex44) 오늘부터 세달뒤의 날짜를 출력하시오
from datetime import date
from dateutil.relativedelta import relativedelta

result = date.today() + relativedelta(months=+3)
print(date.today())
print(result)

#ex45) 이름, 입사일, 입사한 날짜에서 3달 후의 날짜를 출력하시오!
import datetime

from datetime import date
from dateutil.relativedelta import relativedelta
import csv
file=open("d:\data\emp2.csv",'r')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a=datetime.datetime.strptime(emp_list[4],'%Y-%m-%d')
    print(emp_list[1],emp_list[4],a+relativedelta(months=+3))

#ex46) (오라클 last_day / 파이썬 monthrange) 올해 2월달의 마지막 날짜를 출력하시오!
from calendar import monthrange
print(monthrange(2017,2))

#ex47) 오늘부터 요번달 말일까지 총 몇일 남았는지 출력하시오!
from datetime import date
from dateutil.relativedelta import relativedelta
from calendar import monthrange
#print(monthrange(2017,4)[1])
#print(date.today().day)
print(monthrange(2017,4)[1]-date.today().day)

#ex48) 오늘이 무슨 요일인지 출력하시오!
import datetime
day=datetime.datetime.today().weekday()
print(day)

#ex49) 이름, 입사한 요일을 출력하시오! (next_day vs 사용자 정의 함수)
import datetime
import csv
file=open("d:\data\emp2.csv",'r')
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a=datetime.datetime.strptime(emp_list[4],'%Y-%m-%d')
    print(emp_list[1],days[a.weekday()])

#ex50) 오늘 날짜에서 하루를 더한 날짜가 어떻게 되는가?
import datetime
print(date.today() + datetime.timedelta(days=1))

#ex51) 아래와 같이 실행될 수 있는 사용자 정의 함수를 생성하시오!
#next_day(date.today(),1)

def next_day(val1, val2):
    return(val1+datetime.timedelta(days=val2))
print(next_day(date.today(),1))

#ex52) 아래와 같이 실행될 수 있는 사용자 정의 함수를 생성하시오! (next_day vs 사용자 정의 함수)
s = ‘2017-0417’
d = datetime.datetime.strptime(s, ‘%Y-%m-%d’)
print(d)

print(next_day(‘2017-04-17’,1))


#다시해야함
#ex53) 아래와 같이 수행하면 지정된 날짜에서 돌아오는 요일의 날짜가 출력되게 하시오!
#b=[‘월요일’,’화요일’,’수요일’,’목요일’,’금요일’,’토요일’,’일요일’]
#화요일에 b 리스트 변수에서 몇 번째 요소인지를 출력하려면?

dic={}
dic[‘월요일’]= 0
dic[‘화요일’]= 1
dic[‘수요일’]= 2
dic[‘목요일’]= 3
dic[‘금요일’]= 4
dic[‘토요일’]= 5
dic[‘일요일’]= 6

def next_day(val1,val2):
    dic={}
    dic[‘월요일’]=0
    dic[‘화요일’]=1
    dic[‘수요일’]=2
    dic[‘목요일’]=3
    dic[‘금요일’]=4
    dic[‘토요일’]=5
    dic[‘일요일’]=6
    c=dic[val2]
   d=datetime.datetime.strptime(val1,’%Y-%m-%d’)
   return(d+datetime.timedelta(days=c))

print(next_day(‘2017-04-17’,’화요일’))


#ex54) 이름, 입사한 날짜부터 오늘까지 총 몇일 근무했는지 출력하시오!
from datetime import date
import datetime
import csv
file=open(“d:\data\emp2.csv”,’r’)
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a=datetime.datetime.strptime(emp_list[4],’%Y-%m-%d’).date()
    print(emp_list[1], date.today()- a)

#date.today().toordinal())

#ex55)input명령어와 if를 이용한 문제
#if문을 사용해서 사원번호가 7788번인 사원의 이름과 월급을 출력하시오
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[0]) == 7788:
        print(emp_list[1],emp_list[5])

