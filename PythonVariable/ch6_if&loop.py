##################■ 6.1 if문       P.126
#
# if 조건:                           "조건이 True이면 실행되고 False이면 실행X"
# 실행문
# elif 조건2:
# 실행문
# elif 조건3:
# 실행문
# else:
# 실행문
#
# * 조건이 False로 평가되는 경우 (p.118)
# False
# None
# 0
# 비어있는 순서열: '' ,  ()  , []
# 비어있는 딕셔너리:   {}




#문제111. 숫자를 물어보게 하고 숫자를 입력해서 짝수인지 홀수인지를 출력하는 if문을 파이썬 코드로 작성하시오.

a=int(input('숫자를 입력하세요'))

if a%2==0:
    print('해당 숫자는 짝수입니다.')
else:
    print('헤당 숫자는 홀수입니다.')




#문제112. 위의 if문의 예제로 mod함수를 생성하시오.

print(mod(10))
짝수입니다.


def mod(var):
    if var%2==0:
        return '해당 숫자는 짝수입니다.'
    else:
        return '헤당 숫자는 홀수입니다.'

a=int(input('숫자를 입력하세요'))

print(mod(a))




#문제113. 이름을 물어보게 하고 이름을 입력하면 해당 사원이 고소득자인지, 저소득자인지 출력되게 하시오.

import csv

def judge(sal):
    if a>=3000:
        return '고소득자입니다.'
    elif a>=2000:
        return '적당합니다.'
    else:
        return '저소득자입니다'

file = open("D:\data\emp.csv",'r')

emp_csv = csv.reader(file)
ename = input('이름을 입력하세요.')

for emp_list in emp_csv:
    if ename == emp_list[1]:
        sal = int(emp_list[5])
        print(judge(sal))


#pandas 이용:

import pandas as pd

a=input('이름을 입력하세요')
emp = pd.read_csv("D:\emp.csv")
sal = emp[['sal']][emp['ename']==a.upper()].values[0]

if sal>=3000:
    print('고소득자입니다.')
elif sal>=2000:
    print('적당합니다.')
else:
    print('저소득자입니다')



#뮨재114. 위의 문제를 다시 수행하되 이름을 소문자로 입력해도 결과가 출력되게 하시오.

import pandas as pd

a=input('이름을 입력하세요')
b=a.upper()
emp = pd.read_csv("D:\emp.csv")
sal = emp[['sal']][emp['ename']==b].values[0]

if sal>=3000:
    print('고소득자입니다.')
elif sal>=2000:
    print('적당합니다.')
else:
    print('저소득자입니다'




# 문제115. (알고리즘 문제) 가우스 공식으로 1부터 10까지의 숫자의 합을 출력하세요.
#
# 첫번쨰 수를 입력하세요.1
# 마지막 수를 입력하세요.10
# 1부터 10까지의 합은 55입니다.


start = int(input('첫번째 숫자를 입력하세요.'))
end = int(input('마지막 숫자를 입력하세요.'))

result = ((start+end)/2)*(end-start+1)

print(start,'부터',end,'까지 숫자의 합은',result,'입니다')




#문제116.위의 문제를 다시 수행하는데 아래와 같이 큰 숫자를 먼저 입력하면 첫 번째 입력한 숫자가 두번째 입력한 숫자보다 큽니다. 라는 메세지가 출력되게 하시오.


def sum(start,end):
    if start > end:
        return '첫번째 입력한 숫자가 두번째 입력한 숫자보다 큽니다.'
    else:
        result = ((start+end)/2)*(end-start+1)
        return result

start = int(input('첫번째 숫자를 입력하세요.'))
end = int(input('마지막 숫자를 입력하세요.'))


print(sum(start,end))



# ■ 6.2 for loop문
#
# 문법: for 반복변수 in 순서열:
# 실행문          ↑
#                     리스트,튜플,문자열,딕셔너리

for i in (1,2,3):       #튜플
print(i)

for i in [1,2,3]:       #리스트
print(i)

for i in 'python is love':   #문자열
print(i)

for i in range(0,5):
print(i)
for i in range(5):
print(i)
for i in range(1,10,2):    #1부터 10까지 나오는데 간격을 2로
print(i)



문제117. 구구단 2단을 출력하시오.

for i in range(1,10):
    print('2 x',i,'=',2*i)


문제118. 아래의 결과를 출력하시오.
★
★★
★★★
★★★★
.
.
★★★★★★★★★★


pattern ='★'
star ='★'

for i in range(1,11):
    print(pattern)
    pattern += star

or

star ='★'
for i in range(1,11):
    print(i*star)


참고 파이썬 튜닝??
예제 1 : 문자열 붙이기1   (이 코드는 시간이 존나 많이 걸린다)
s = ''
for k in range(100000):
       s += 'spam'           s는 100000개의 스펨을 갖게된다

예제 1 : 문자열 붙이기2   (다른 방법...좀 낫다함)
t = []
for k in range(100000):
     t.append('spam')
s = ''.join(t)

출처: http://200315193.tistory.com/267 [quatre의 블로그]

출처: <http://200315193.tistory.com/267>





문제119. 아래와 같이 출력하시오.
★★★★★★★★★★

.
.
★★★★
★★★
★★
★


star ='★'
pattern = ''

for i in range(10,0,-1):
    pattern = i*star
    print(pattern)



문제120. 아래와 같이 출력하시오.


pattern = ''

for i in range(1,11):
    if i <= 5:
        pattern = (' '*(5-i)+'★'*i)
        print(pattern)
    else:
        pattern = (' '*(i-5)+'★'*(10-i))
        print(pattern)
print('a')





star ='★  '
space = ' '
pattern = ''

for i in range(1,11):
    if i <= 5:
        pattern = (space*2*(5-i))+star*(i)+(space*2*(5-i))
        print(pattern)
        print()
    else:
        pattern = (space*2*(i-5))+star*(10-i)+(space*2*(i-5))
        print(pattern)
        print()



문제121. 중첩 for loop문을 이용해서 ★로 사각형을 만드시오.

가로의 숫자를 입력하세요~ 5
세로의 숫자를 입력하세요~ 5

★★★★★
★★★★★
★★★★★
★★★★★
★★★★★

width=int(input('가로의 숫자를 입력하세요'))
height=int(input('세로의 숫자를 입력하세요'))

pattern=''
for i in range(height):
    for j in range(width):
        pattern +='★ '
    print(pattern)
    pattern=''


무성이 버전 문제121번
a=int(input('가로의 숫자를 입력하세요'))
b=int(input('세로의 숫자를 입력하세요'))

for i in range(b):
result = ''.join('★' for i in range(a))

print(result)


설명:
('★' for i in range(5))   #for loop문을 5번 돌려서 ★를 5개로 만들어라
join    ★5개를 모아주는 메소드
''.    result변수를 ''로





문제122. 구구단을 가로로 출력하시오.
2 x 1=2   3 x 1 =3     ...........9 x 1=9
.
.

for i in range(1,10):
    ans=''
    for j in range(2,10):
        ans = ans + str(j) +'X'+ str(i) + '=' + str(j*i)+' '
    print(ans)

밑은 정렬 예쁘게

for i in range(1,10):
    ans=''
    for j in range(2,10):
        ans += (str(j) +'X'+ str(i) + '=' + str(j*i)).ljust(8)
    print(ans)                                                           ↑
                                                                               정렬 lpad(ans,10,' ')와 같음


문제123. for loop문을 이용해서 power함수를 구현하시오.

밑수를 입력하세요.  2
지수를 입력하세요. 3
2의 3승은 8입니다.


a=int(input('밑수를 입력하세요'))
n=int(input('지수를 입력하세요'))

result=1

for i in range(n):
    result*=a
print(a,'의',n,'승은',result,'입니다')



■ 숫자, 문자, 공백이 스크립트 안에 얼마나 포함되었는지 확인하는 방법
s = 'some string'

numbers =sum(i.isdigit() for i in s)
words=sum(i.isalphs() for i in s)
space=sum(i.isspace() for i in s)
print(numbers)
print(words)
print(space)



문제124. 겨울왕국 대본에는 숫자가 몇 개나 있나?

step1)  먼저 대본의 줄마다 뽑아서 출력해봄
winter = open("D:\data\winter.txt","r")
lines = winter.readlines()
total = 0
for i in lines:
    print(i)


winter = open("D:\data\winter.txt","r")
lines = winter.readlines()
total = 0
for i in lines:
    total += sum(c.isdigit() for c in i)
print(total)


문제125. 겨울왕국에 특수문자가 몇 개나 포함되어져 있는지 확인하시오.

winter = open("D:\data\winter.txt","r")
lines = winter.readlines()
total = 0
for i in lines:
    length = len(i)
    alnum = sum(c.isalnum() for c in i)
    space = sum(c.isspace() for c in i)
    total += length - alnum - space
print(total)



■ while loop문

문법: while 조건 :
      실행문

예제:   print('몇 번 반복할까요?')
 limit = int(input('반복할 횟수를 입력하세요.'))
count = 0

while count < limit:
count += 1
print('{0}회 반복'.format(count))


문제126. 숫자를 물어보게 하고 숫자를 입력하면 해당 숫자만큼 아래와 같은 그림이 그려지게 하시오.   while loop로

숫자를 입력하세요. 4
            ★
          ★★
         ★★★
       ★★★★

num = int(input('숫자를 입력하세요'))
cnt=1
while cnt<=num:
    print(' '*(num-cnt)+'★'*cnt)
    cnt+=1



문제127. 퍅토리얼을 while loop문으로 구현하시오.

팩토리얼 숫자를 입력하세요~  5
120 입니다.

n = int(input('팩토리얼 숫자를 입력하세요.'))
result = 1
while n>0:
    result *= n
    n-=1

print(result,'입니다.')


문제128. log함수를 파이썬으로 구현하시오.

밑수를 입력하시오.
지수를 입력하시오.


a=int(input('밑수를 입력하시오.'))
b=int(input('진수를 입력하시오.'))

value = 1
n = 0
while value < b:
    value *= a
    n += 1
print('로그값은',n,'입니다.')



문제129. (공채에서 가장 많이 나오는 알고리즘 문제) 두 수를 입력받아서 최대공약수를 구하시오.  (while loop문 + 유클리드 호제법)

첫번째 수를 입력하세요. 24
두번째 수를 입력하세요. 18
6 입니다.

a = int(input('첫번째 수를 입력하세요.'))
b = int(input('두번째 수를 입력하세요.'))

if b>a:
    temp=b
    b=a
    a=temp

while a%b!=0:
    r=a%b
    a=b
    b=r

print(b,'입니다.')


문제130(마지막 문제)  최대공약수를 알고 싶은 두 개의 숫자를 입력하세요. ~ 24 18
6입니다.

numbers = input('최대공약수를 알고 싶은 두 수를 입력하세요.')

ab = numbers.split(' ')

a = int(ab[0])
b = int(ab[1])

if b>a:
    temp=b
    b=a
    a=temp

while a%b!=0:
    r=a%b
    a=b
    b=r

print(b,'입니다.')



■ mit 공대 머신러닝 코드를 이해하기 위한 문법?
format함수
for loop문
함수 생성한느 방법
자료형 - 리스트, 튜플, 딕셔너리
if문
몬테카를로 알고리즘
탐욕 알고리즘
수학 공식
self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)



■ 6.4 continue와 break

- continue문
 "반복문이 실행되는 동안 특정 코드블럭은 실행하지 않고 다른 코드 블럭만 실행되게 할 때 사용하는 문법"

예제 설명:
for i in range(10):
    if i%2==1:
        continue;
    print(i)                  #짝수만 출력
설명: i%2==1이면 continue다음의 반복문은 실행시키지 말고 반복문 처음으로 돌아가라)

문제131.  숫자를 1부터 10까지 출력하는데 중간에 5는 나오지 않게 하시오.

for i in range(1,11):
    if i==5:
        continue
    print(i)


■ break문
"루프를 중단시키는 역할을 하는 문법"

예제 :    i = 0
    while(True) :       #무한 루프 돌리겠다
i = i+1
if i==1000:
print('i가 {0}이 됌. 반복문을 중단합니다.'.format(i))
break
    print(i)



예제2:
i = 0
while (True):
    i = i+1
    if i==1000:
        print('i가 {0}이 됌. 반복문을 중단합니다.'.format(i))
        break
print(i)





문제132. 함수를 생성하는데 아래와 같이 숫자를 넣어서 실행하면 해당 숫자만큼 숫자가 세로로 출력되게 하시오.

prinf(break_fun(10))    #10이 loop를 중단시킬 숫자
1
2
3
.
.
10


def break_fun(var):
    for i in range(1,var+1):
        print(i)
        if i==var:
            break
    return ' '

print(break_fun(10))


문제133. 위의 함수를 수정해서 결과가 아래와 같이 가로로 출력되게 하시오.
print(break_fun(10))
1 2 3 4 5 6 7 8 9 10

def break_fun(var):
    result = ''
    for i in range(1,var+1):
        result += str(i)+' '
        if i==var:
            break
    return result

print(break_fun(10))



6장을 정리하는 문제들

■ 6장에서 배운 내용 if문과 loop문을 정리하는 문제

 * pandas를 이용해서 1. 판다스 기본문법
                    2. 판다스의 연산자
         3. 판다스 이용해서 서브쿼리
         4. 판다스 이용해서 조인

* pandas를 이용하지 않고 조인
for loop문을 중첩해서 문제를 해결
딕셔너리 데이터 타입을 이해(MIT 코드에서도 중요하게 쓰인다)


문제134. 아래와 같이 딕셔너리 형태의 데이터를 만들고 출력하시오.

* 파이썬 데이터 구조 3가지 :      1. 리스트    2. 튜플    3. 딕셔너리(키와 값으로 구성된
자료형)                                                   [ 와 ]           ( 와 )                      { 와 }

emp_dic={'mgr':'7788','sal':'1100','deptno':'20','comm':'0','job':'CLERK','hiredate':'1983-01-15',
'empno':'7876','ename':'ADAMS'}

emp_dic
out [27]: comm' : 'deptno' : empno ename '20', '7876', ' ADAMS ' ' hiredate '1983 01-15' 'job': mgr ' 'sal'. 'CLERK', '7788' '1100'}

emp_dic['mgr']



문제135. 6장에서 배운 for loop를 이용해서 emp2.csv를 읽어와서 emp_dic라는 딕셔너리 데이터 유형을 만드시오.

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
emp=[]

for emp_list in emp_csv:
    emp.append({'empno':emp_list[0],'ename':emp_list[1],'job':emp_list[2],
               'mgr':emp_list[3],'hiredate':emp_list[4],'sal':emp_list[5],
               'comm':emp_list[6],'deptno':emp_list[7]})

print(emp)

# 딕셔너리 안에는 append가 없어서 바로 딕셔너리에 for loop로 한꺼번에 넣을 수 없음.
그래서 위와 같이 리스트 변수 안에 딕셔너리 변수를 담아준 것임



문제136. emp 딕셔너리 변수에서 이름만 출력하시오.
그동안에는 emp_list변수에서 ename에 해당하는 부분을 출력해왔다면 지금은
emp_dic변수에서 ename에 해당하는 부분을 출력하는 것이다.

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
emp=[]
emp_dic={}         #얘 안 써줘도 똑같이 나옴
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0],'ename':emp_list[1],'job':emp_list[2],
               'mgr':emp_list[3],'hiredate':emp_list[4],'sal':emp_list[5],
               'comm':emp_list[6],'deptno':emp_list[7]})
for emp_dic in emp:
    print(emp_dic['ename'])

KING BLAKE CLARK JONES MARTIN ALLEN TURNER JAMES WARD FORD SMITH SCOTT ADAMS MILLER


문제137. 이름, 월급, 직업을 출력하시오.
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
emp=[]

for emp_list in emp_csv:
    emp.append({'empno':emp_list[0],'ename':emp_list[1],'job':emp_list[2],
               'mgr':emp_list[3],'hiredate':emp_list[4],'sal':emp_list[5],
               'comm':emp_list[6],'deptno':emp_list[7]})

for emp_dic in emp:
    print(emp_dic['ename'],emp_dic['sal'],emp_dic['job'])


문제138. dept.csv를 읽어서 딕셔너리 데이터 구조로 저장하고 아래와 같이
수행하면 deptno, dname, loc가 출력되게 하시오.
print( dept_dic['deptno'], dept_dic['dname'], dept_dic['loc'] )

import csv

file = open("D:\data\dept.csv","r")
dept_csv = csv.reader(file)

dept=[]

for dept_list in dept_csv:
    dept.append({'deptno':dept_list[1],'dname':dept_list[2],'loc':dept_list[3]})
for dept_dic in dept:
    print(dept_dic['deptno'],dept_dic['dname'],dept_dic['loc'])



문제139. emp.csv와 dept.csv를 각각 읽어와서 emp_dic, dept_dic 딕셔너리 자료형으로
만드는 스크립트를 하나로 합치시오.

import csv

file1 = open("D:\data\emp2.csv",'r')
file2 = open("D:\data\dept.csv","r")
emp_csv = csv.reader(file1)
dept_csv = csv.reader(file2)
emp=[]
dept=[]
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0],'ename':emp_list[1],'job':emp_list[2],
               'mgr':emp_list[3],'hiredate':emp_list[4],'sal':emp_list[5],
               'comm':emp_list[6],'deptno':emp_list[7]})

for dept_list in dept_csv:
    dept.append({'deptno':dept_list[1],'dname':dept_list[2],'loc':dept_list[3]})

emp
dept


문제140. emp와 dept라는 딕셔너리 자료구조를 만드는 스크립트와 중첩 for loop문을
이용해서 emp와 dept를 join 시켜서 ename과 loc를 출력하시오.

import csv

file1 = open("D:\data\emp2.csv",'r')
file2 = open("D:\data\dept.csv","r")
emp_csv = csv.reader(file1)
dept_csv = csv.reader(file2)
emp=[]
dept=[]
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0],'ename':emp_list[1],'job':emp_list[2],
               'mgr':emp_list[3],'hiredate':emp_list[4],'sal':emp_list[5],
               'comm':emp_list[6],'deptno':emp_list[7]})

for dept_list in dept_csv:
    dept.append({'deptno':dept_list[1],'dname':dept_list[2],'loc':dept_list[3]})

                                                        #오라클 join 중 "nested loop 조인 방법"
for e in emp:
    for d in dept:                             #오라클은 C언어로 만들어짐
        if e['deptno']==d['deptno']:
            print(e['ename'],d['loc'])



문제141. 부서위치가 DALLAS인 사원들의 이름과 부서위치를 출력하시오.

import csv

file1 = open("D:\data\emp2.csv",'r')
file2 = open("D:\data\dept.csv","r")
emp_csv = csv.reader(file1)
dept_csv = csv.reader(file2)
emp=[]
dept=[]
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0],'ename':emp_list[1],'job':emp_list[2],
               'mgr':emp_list[3],'hiredate':emp_list[4],'sal':emp_list[5],
               'comm':emp_list[6],'deptno':emp_list[7]})

for dept_list in dept_csv:
    dept.append({'deptno':dept_list[1],'dname':dept_list[2],'loc':dept_list[3]})

for e in emp:
    for d in dept:
        if e['deptno']==d['deptno'] and d['loc']=='DALLAS':
            print(e['ename'],d['loc'])


문제142. 위의 스크립트를 이용해서 join함수를 생성하시오.

print(join(emp, 'ename', dept,'loc',deptno))
                                                                 ↑
                                                    얘로 조인해라

def join(table1,col1,table2,col2,joincol):
    for i in table1:
        for j in table2:
            if i[joincol]==j[joincol]:
                print(i[col1],j[col2])
    return ''

print(join(emp,'ename',dept,'loc','deptno'))


문제143. pandas를 이용해서 이름,부서위치를 출력하시오.

import pandas as pd

emp = pd.read_csv("D:\data\emp.csv")
dept = pd.read_csv("D:\data\dept.csv")

result = pd.merge(emp,dept,on='deptno')
print(result[['ename','loc']])

1 2 3 4 5 6 7 8 9 10 11 12 13 ename KING CLARK MILLER BLAKE MARTIN ALLEN TURNER JAMES WARD JONES FORD SMITH SCOTT ADAMS NEW NEW NEW loc YORK YORK YORK CHICAGO CHICAGO CHICAGO CHICAGO CHICAGO CHICAGO DALLAS DALLAS DALLAS DALLAS DALLAS

문제144. 부서위치가 DALLAS인 사원들의 이름, 부서위치를 출력하시오.
pandas로 수행한다.

import pandas as pd

emp=pd.read_csv("D:\data\emp.csv")
dept=pd.read_csv("D:\data\dept.csv")

result = pd.merge(emp,dept,on='deptno')
print(result[['ename','loc']][result['loc']=='DALLAS'])

9 10 11 12 13 ename JONES FORD SMITH SCOTT ADAMS loc DALLAS DALLAS DALLAS DALLAS DALLAS


문제145. 이름, 부서위치를 출력하는데 아래와 같이 outer join을 구현하시오.

select e.ename, d.loc
from emp e, dept d
where e.deptno=d.deptno(+);
