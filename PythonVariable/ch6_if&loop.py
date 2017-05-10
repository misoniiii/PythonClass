######################################################################
######################   6.1 if
######################################################################
#ex111) 숫자를 물어보게하고 숫자를 입력해서 짝수인지 홀수인지를 출력하는 if문 작성
k = int(input('숫자를입력하세요'))

if k%2 == 0:
    print('짝수')
else:
    print('홀수')

#ex112) 위의 if문의 예제로 mod함수를 생성하시오
#print(mod(10))
#짝수입니다
def mod(val):
    if val%2 == 0:
        return('짝수입니다')
    else:
        return('홀수입니다')

print(mod(10))

#ex113)이름을 물어보게 하고 이름을 입력하면 해당 사원이 고소득자인지 저소득자인지 출력되게 하시오
import pandas as pd
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
k = input('이름 입력')
sal = emp[['sal']][emp['ename'] == k].values[0]

if sal >= 3000:
    print(sal, '고소득자')
elif sal >= 2000:
    print(sal, '적당')
else:
    print(sal, '저소득자')

k = input('이름을 입력하세요')
file = open("/Users/misoni/Desktop/pythondata/emp_comm.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[1] == k:
        if int(emp_list[5]) >= 3000:
            print(emp_list[1], emp_list[5],'고소득자')
        elif int(emp_list[5]) >= 2000:
            print(emp_list[1], emp_list[5],'적당')
        else:
            print(emp_list[1], emp_list[5],'저소득자')



#ex114) 위의 결과를 다시 수행하는데 이름을 소문자로 입력해도 결과가 출력되게 하시오
import pandas as pd
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
k = input('이름 입력')
sal = emp[['sal']][emp['ename'] == k.upper()].values[0]
if sal >= 3000:
    print(sal, '고소득자')
elif sal >= 2000:
    print(sal, '적당')
else:
    print(sal, '저소득자')

#ex115) (알고리즘 문제) 가우스 공식을 1부터 10까지의 숫자합을 출력하시오
#첫번째수를 입력하세요1
#마지막 수를 입력하세요0
#1부터 10까지의 합은 55입니다

start_num = int(input('첫번째 숫자를 입력'))
last_num = int(input('두번째 숫자 입력'))

sum = 0
for i in range(start_num,last_num+1):
    sum += i
print(str(start_num) + '부터 ' + str(last_num) + '까지의 합은 ' + str(sum) + '입니다')

#가우스 공식
start_num = int(input('첫번째 숫자를 입력'))
last_num = int(input('두번째 숫자 입력'))
cnt = last_num - start_num + 1
sum = cnt * (cnt+1) /2
print(round(sum))


#ex116) 위의 문제를 다시 수행하는데 아래와 같이 큰 숫자를 먼저 입력하면 첫번째 입력한 숫자가 두번째 입력한 숫자보다 큽니다라는 메세지가 출력되게 하시오
start_num = int(input('첫번째 숫자를 입력'))
last_num = int(input('두번째 숫자 입력'))
if start_num > last_num:
    print('첫번째 숫자가 두번째 숫자보다 큽니다')
else:
    sum =  last_num* (last_num+1)/2 - (start_num-1)*start_num/2
    print(round(sum))

######################################################################
######################   6.2 for loop
######################################################################
for i in (1,2,3): #튜플
    print(i)
#1
#2
#3
for i in ['a','b','c']: #리스트
    print(i)
#a
#b
#c

for i in 'I am boy': #문자
    print(i)
# I
#
# a
# m
#
# b
# o
# y 공백까지 출력됨

for i in range(0,5):
    print(i)
for i in range(5):
    print(i)

#ex117)구구단 출력
#2x1=2
#2x2==4
#2x3=6

for i in range(1,10):
    print('2x' + str(i) + '=' + str(2*i))

for j in range(2,10):
    for i in range(1,10):
        print(j,'x', i,'=',j*i)
    print('\n')

#ex118)아래의 결과를 출력하시오
#★
#★★
#★★★
#★★★★
#★★★★★
for i in range(6):
    print('★'*i)

#ex119)아래의 결과를 출력하시오
# ★★★★★
# ★★★★
# ★★★
# ★★
# ★
for i in range(6):
    print(' '*(5-i) + '★'*i)

for i in range(5,0,-1):
    print('★'*i)

#ex120)아래와 같이 출력하시오
#마름모
k = int(input('한줄 별 최대 개수'))
for i in range(k*2):
    if i <= k:
        print(' '*(k-i), '★'*i, ' '*(k-i))
    if i > k:
        print(' '*(i-k), '★'*(2*k-i), ' '*(i-k) )


import csv 
file=open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
 emp_csv=csv.reader(file) 
sal_list = [] 
for emp_list in emp_csv: 
    sal_list.append(int(emp_list[5]))
print(sal_list.sort())

#ex121)중첩 for loop를 이용해서 ★로 사각형을 만드세요
#가로의 숫자입력 5
#세로 숫자입력
a = int(input('가로'))
b = int(input('세로'))


for i in range(b):
    print('★'*a)

for j in range(b):
    star = ''
    for i in range(a):
        star += '★'
    print( star)

###무성이 버전
a = int(input('가로'))
b = int(input('세로'))
for i in range(b):
    result =''.join('★' for j in range(a))
    print(result)



# [설명] ['★' for i in range(a)] for loop를 5번 돌려서 별을 다섯개로
#     .join 별다섯개를 모아주는 메서드
# ". result변수를"로





#ex122)구구단을 가로로 출력
# 2x1 = 2 3x1=3 ....
#2x2= 4 ....

for j in range(1,10):
    res = ''
    for i in range(2,10):
        res += (str(i)+'x'+str(j)+'='+str(i* j).rjust(2)).ljust(10)
    print(res)

print('a'.rjust(10,'#'))

#ex123) for loop를 이용해서 power함수를 구현하세요
#밑수를 입력하세요 2
#지수를 입력하세요
#2의 3승은 8 입니다
base = int(input('밑수를 입력하세요'))
exp = int(input('지수를 입력하세요'))

res = 1
for i in range(exp):
    res = res * base
print(base,'의', exp,'승은 ', res,'입니다')


####숫자,문자,공백이 스크립트 안에 얼마나 포함되었는지 확인하는 방법
s = 'some string'
numbers = sum(i.isdigit() for i in s)
words = sum(i.isalpha() for i in s)
spaces = sum( i.isspace() for i in s)

print(numbers)
print(words)
print(spaces)

#
#ex124) 겨울 왕국 대본에는 숫자가 몇개나 있는가
text_file = open("/Users/misoni/Desktop/pythondata/winter.txt",'r',encoding='CP949')
lines = text_file.readlines()
total = 0
for s in lines:
    print(s)
    numm = sum( i.isdigit() for i in s)
    print(numm)
    total += numm
print(total)

#ex125) 겨울왕국에 공백,알파벳 숫자도 아닌 (특수문자) 가 몇개나 포함되어있는지 확인
s= 'some string23'
print(len(s)) #공백도 나옴

text_file = open("/Users/misoni/Desktop/pythondata/winter.txt",'r',encoding='CP949')
lines = text_file.readlines()
tot1 = 0
tot2 = 0

for s in lines:
    numm = sum( i.isdigit() for i in s)
    alpha = sum( i.isalpha() for i in s)
    space = sum( i.isspace() for i in s)
    cnt = len(s)
    tot1 += cnt
    tot2 += (numm + alpha + space)
print(tot1 - tot2)



##while loop
#문법
## while 조건 :
#실행문
print('몇번 반복할까요')
limit = int(input('반복할 횟수를 입력하세요'))
count = 0
while count < limit:
    count = count + 1
    print ( '{0}회 반복'.format(count))


#ex216)숫자를 물어보게 하고 숫자를 입력하면 해당 숫자만큼 아래와 같은 그림이 그려지게 하시오(while loop)
#숫자를 입력하세요(트리모양인디)
 #      ★
 #     ★★
 #    ★★★
 #   ★★★★
 #  ★★★★★
 # ★★★★★★
num = int(input('숫자 입력하세요'))

cnt = 0
while cnt <= num:
    cnt =   cnt + 1
    print(' '*(num-cnt),'★'* cnt) # cnt 1부터
    if cnt == num:
        break


cnt = 0
while cnt < num:
    cnt =   cnt + 1
    print(' '*(num-cnt),'★'* cnt) # cnt 1부터


#ex127) 팩토리얼을 while loop로 구현사이ㅗ
#팩토리얼 숫자를 입력하세요 5
#120입니다
num = int(input('팩토리얼 숫자를 입력하세요'))
cnt = 0
res = 1
while cnt < num:
    cnt = cnt + 1
    print(cnt)
    res = res * cnt
    print(res)
print(res,'입니다')



#ex128) log함수를 파이썬으로 구현하시오
#밑수를 입력하시오 2
#진수를 입력하시오 16
#로그값은 4입니다
a = int(input('밑수를 입력하시오'))
b = int(input('진수를 입력하시오'))

cnt = 0
while b  >= a :
    cnt +=  1
    b /=  a
print('로그값은 ',cnt,'입니다')


#ex129)(공채에서 가장 많이 나오는 알고리즘 문제
#두수를 입력받아서 최대 공약수를 구하시오
#첫번째 수를 입력하세요 24
#두번째 수를 입력하세요 18
#6 입니다
#while loop + 유클리드 호제
a = int(input('첫번째 수를 입력'))
b = int(input('두번째 수를 입력'))
if a >= b:
    while a%b != 0 :
       a = a%b #나머지
       a, b = b ,a
    print(b)
else:
    a, b = b ,a
    while a%b != 0 :
       a = a%b #나머지
       a, b = b ,a
    print(b)

#ex130) 최대공약수를 알고 싶은 2개의 숫자를 입력하세요 24 18
#6입니다
num = int(input('수를 입력하세요'))
b = int(input('두번째 수를 입력'))
if a >= b:
    while a%b != 0 :
       a = a%b #나머지
       a, b = b ,a
    print(b)
else:
    a, b = b ,a
    while a%b != 0 :
       a = a%b #나머지
       a, b = b ,a
    print(b)


num = input('수를 입력하세요')

num= "18 24 36"
a = num.split()[0]
b = num.split()[1]
c =

import re

import re
p = re.compile('[0-9]+')
res = p.findall("18 24 36 100 20 34 50")
res = map(lambda x: int(x), res)
print(res)
res.sort(reverse=True)
print(res)
alph = ['a','b','c','d','e','f','g']
dic_list = dict()

for i in range(len(res)):
    dic_list[alph[i]] = res[i]

print(dic_list)


######################################################################
######################   6.4 continue& break
######################################################################
for i in range(10):
    if i%2 == 1:
        continue #홀수는 출력되지 않도록
    print(i)

#ex131) 숫자를 1부터 10까지 출력하는데 중간에 5는 나오지 않게 하시오
for i in range(1,11):
 if i == 5:
     continue
 print(i)

i =0
while(True): # 무한 루프를 돌리겠다
    i = i + 1
    if i == 1000:
        print('i가 {0}이 됨, 반복문 중단'.format(i))
        break  #1000일때 종료
    print(i)

#ex132)함수를 생성하는데 아래와 같이 숫자를 넣어서 실행하면 해당 숫자만큼 숫자가 세로로 출력되게 하시오
#print(break_func(10)) #10이 loop문을 중단시킬 숫자
#####선생님#######################
def break_func(val):
    i= 1
    while 1:
        print(i)
        if i == val:
            break
        i += 1
    return ''  #return값을 안정해주면 none이 나옴
print(break_func(10))

#ex133) 위의 함수를 수정해서 결과가 아래와 같이 가로로 출력되게 하시오
#print(break_func(10))
# 1 2 3 4 5 6 7 8 9 10
def break_func2(val):
    res = ''
    i = 1
    while 1:
        res += str(i) + ' '
        if i == val:
            break
        i += 1
    print(res)
    return ''
print(break_func2(10))

#6장에서 배운 if문과 loop문을 정리하는 문제
#pandas를 이용해서 1.기본문법 2. 연산자 3.서브쿼리 4. 조인
#pandas를 이용하지 않고 조인
##1.for loop문을 중첩해서 ㅜㄴ제해결
##2.딕셔너리 데이터 타입을 이해(mit코드에서도 중요하게 쓰임)

#ex134)아래와 같이 딕셔너리 형태의 데이터를 만들고 출력하시오
# 파이썬 데이터구조 3가지 1.리스트 2. 튜풀 3. 딕셔너리(키와 값으로 구성)
emp_dic = {'mgr':'7788','sal':'1100','deptno':'20', 'comm':'0',
           'job':'CLERK','hiredate':'1983-01-15','empno':'7876',
           'ename':'ADAMS'}
print(emp_dic)
print(emp_dic['mgr'])

#ex135) 6장에서 배운 for loop를 이용해서  emp2.csv를 읽어와서 emp_dic이라는 딕셔너리 데이터 유형을 만드시오
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
emp_csv = csv.reader(file)
emp = [] # 비어있는 리스트 변수 선언
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )

print(emp)

#ex136) emp딕셔너리 변수에서 이름만 출력하시오
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
emp_csv = csv.reader(file)
emp = [] # 비어있는 리스트 변수 선언
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )
for emp_dic in emp:
    print(emp_dic['ename'])

#ex137)이름,월급,직업 출력
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
emp_csv = csv.reader(file)
emp = [] # 비어있는 리스트 변수 선언
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )
for emp_dic in emp:
    print(emp_dic['ename'],emp_dic['sal'],emp_dic['job'])

#ex138) dept.csv읽어서 딕셔너리 구조로 저장하고 아래와 같이 수행하면 deptno, dname, loc이 출력되게 하시오
#print(dept_dic['deptno'],...
import csv
file = open("/Users/misoni/Desktop/pythondata/dept.csv",'r')
dept_csv = csv.reader(file)
dept = []
for i in dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'loc':i[2] } )
for dept_dic in dept:
    print(dept_dic['deptno'], dept_dic['dname'],dept_dic['loc'])

#완전판
# ex139) emp.scv와 dept.csv를 각가 읽어와서 emp_dic, dept_dic 딕셔너리 자료형으로 만드는 스크립트를 하나로 합치시오
import csv
emp_file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
dept_file = open("/Users/misoni/Desktop/pythondata/dept.csv",'r')
emp_csv = csv.reader(emp_file)
dept_csv = csv.reader(dept_file)
emp = []
dept = []
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )

for i in dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'loc':i[2] } )

#print(emp)
#print(dept)

#ex140) emp와 dept라는 딕셔너리 자료구조를 만드는 스크립트와 중첩 for loop문을 이용해서 emp와 dept를 조인시켜서 ename 과 loc를 출력
############위의 스크립트
import csv
emp_file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
dept_file = open("/Users/misoni/Desktop/pythondata/dept.csv",'r')
emp_csv = csv.reader(emp_file)
dept_csv = csv.reader(dept_file)
emp = []
dept = []
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )

for i in dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'loc':i[2] } )


for e in emp:#14건 이므로 14번 ㅣoop
    for d in dept: #4번이므로 14건에 대해 각각 4번씩 ㅣoop
        if e['deptno'] == d['deptno']: #딕셔너리
            print( e['ename'],d['loc'])
#nested loop조인 방법

#ex141) 부서위치가 DALLAS인 사원들의 이름과 부서위치 출력
import csv
emp_file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
dept_file = open("/Users/misoni/Desktop/pythondata/dept.csv",'r')
emp_csv = csv.reader(emp_file)
dept_csv = csv.reader(dept_file)
emp = []
dept = []
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )

for i in dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'loc':i[2] } )

for e in emp:
    for d in dept:
        if (e['deptno'] == d['deptno']) &  (d['loc'] == 'DALLAS'):
             print(e['ename'],d['loc'])

#ex142)위의 스크립트를 이용해서 조인함수를 생성하시오
#print( join (emp,'ename,dept,'loc','deptno') )
# KING NEW YORK
# BLAKE CHICAGO
# CLARK NEW YORK
# JONES DALLAS
# MARTIN CHICAGO
# ALLEN CHICAGO
# TURNER CHICAGO
# JAMES CHICAGO
# WARD CHICAGO
# FORD DALLAS
# SMITH DALLAS
# SCOTT DALLAS
# ADAMS DALLAS
# MILLER NEW YORK
import csv
emp_file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
dept_file = open("/Users/misoni/Desktop/pythondata/dept.csv",'r')
emp_csv = csv.reader(emp_file)
dept_csv = csv.reader(dept_file)
emp = []
dept = []
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2], 'mgr': i[3],
           'hiredate':i[4],'sal':i[5],'comm':i[6],
           'deptno':i[7] } )

for i in dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'loc':i[2] } )


def join(t1,col1,t2,col2,col):
    for i in t1:
        for j in t2:
            if i[col] == j[col]:
                print( i[col1], j[col2])
                #return( i[col1], j[col2] ) #('KING', 'NEW YORK')
print( join (emp,'ename',dept,'loc','deptno') )

##중첩루프를 사용하려면 딕셔너리를 사용

#ex143)pandas를 이용해서 ename, loc출력
import pandas as pd
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
dept = pd.read_csv("/Users/misoni/Desktop/pythondata/dept.csv")

result = pd.merge(emp,dept,on='deptno')
print(result[['ename','loc']])

#ex144)부서위치가 dallas인 사원들의 이름 부서위치 출력(pandas)
#pandas[열][행]
import pandas as pd
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
dept = pd.read_csv("/Users/misoni/Desktop/pythondata/dept.csv")

result = pd.merge(emp,dept,on='deptno')
print(result[['ename','loc']][result['loc'] == 'DALLAS'])

#ex145) 이름, 부서위치를 출력하는데 아래와 같이 outer join을 구현하시오
# select e.ename, d.loc
#   from emp e, dept d
#  where e.deptno = d.deptno(+) #(+) null 반대쪽은 정보
import pandas as pd
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
dept = pd.read_csv("/Users/misoni/Desktop/pythondata/dept.csv")

result = pd.merge(emp,dept,on='deptno', how ='right')
print(result[['ename','loc','deptno']][result['loc'] == 'BOSTON'])