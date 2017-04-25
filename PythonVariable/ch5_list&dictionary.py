#ex71) emp_list라는 비어있는 리스트 변수를 선언한 후, input명령어를 이용해서 emp_list라는 리스트변수에 요소 추가 구문을 통해 추가하시오
#emp_list 리스트에 추가할 요소를 입력하세요~ a
#a
emp_list=[]
k=input('emp_list에 추가할 요소를 입력하세요')
emp_list.append(k)
print(emp_list)

#ex72)emp_list에 추가된 요소를 삭제하는 코드를 구현하시오
#emp_list에 삭제할 요소를 입력하세요
k=input('emp_list에 추가할 요소를 입력하세요')
emp_list.remove[k]
print(emp_list)

#ex73)emp_list에 요소를 추가,삭제하고 개수를 확인하는 코드를 구현하는데 아래와 같이 실행되게 하시오
#emp_list에 요소를 추가하려면 1번,삭제하려면 2번,개수 확인은 3번을 누르세요
#추가할 요소를 입력하세요
#삭제할 요소를 입력하세요
#emp_list 요소의 개수가 출력
emp_list=['a','b']
print(emp_list)

k = int(input('emp_list에 요소를 추가하려면 1번,삭제하려면 2번,개수 확인은 3번을 누르세요'))

if k == 1 :
    emp_list.append(input('추가할 요소를 입력하세요'))
    print(emp_list)
elif k == 2:
    emp_list.remove(input('삭제할 요소를 입력하세요'))
    print(emp_list)
elif k == 3:
    print(len(emp_list)) #or count(emp_list)
    print(emp_list)

#ex74)리스트 메소드 중에 sort를 이용해서 월급을 출력할 때 높은것부터 출력될 수 있도록 하시오
#1.sal_list = [] 비어있는 리스트에 emp_list[5]를 for loop로 담아냄
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv",'r')
emp_csv = csv.reader(file)

sal_list=[]

for emp_list in emp_csv:
    sal_list.append(emp_list[5])
print(sal_list)

################################################용은
import csv

#sorted 함수에서 비교 대상으로 사용할 대상 리턴
#int(data[5]) : int로 형변환한 월급

def salCheck(data):
    return int(data[5])

file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=True, key=salCheck)

for i in emp_list_sorted:
    print(i)

#ex75) 이름,월급을 출력하는데 abcd순서대로 출력되게 하시오
import csv
def salCheck(data):
    return data[1]

file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=False, key=salCheck)

for i in emp_list_sorted:
    print(i)

#ex76) 직업이 salesman인 사원들의 이름, 입사일,직업을 출력하는데 가장 최근에 입사한 사원부터 출력
def salCheck(data):
    return data[4]

import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=True, key= salCheck)

for i in emp_list_sorted:
    if i[2] == 'SALESMAN':
        print(i[1],i[2],i[4])

#ex77) emp리스트에서 최대 월급을 출력
#hint] sal_list 리스트 변수에 (emp_list[5]월급)을 채워넣는다
#2. sal_list에서 최대값 출력
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
sal_list = []
for emp_list in emp_csv:
    sal_list.append(int(emp_list[5]))
print(sal_list)
print(max(sal_list))

#ex78)emp_list에서 월급읠 평균값을 출력
###################내꺼
import csv

def avg(var):
    return round(sum(var)/len(var))

file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
sal_list=[]
for emp_list in emp_csv:
    sal_list.append(int(emp_list[5]))
print(max(sal_list), avg(sal_list))


##################명학쓰
import csv

file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
sal_list = []
sumsal = 0
cnt = 0
for i in emp_csv:
    cnt +=  1
    sumsal += int(i[5])
print(sumsal/cnt )

#ex79)emp+list에서 직업이 salesman인 사원들 중 최대 월급을 출력하시오
import csv

file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
sal_list=[]
for i in emp_csv:
    if i[2] == 'SALESMAN':
        sal_list.append(int(i[5]))

print('SALESMAN', max(sal_list))


####tuple
a = (1,2,3)
print(type(a))

b=1,2,3
print(type(b))

####
# select * from ttt_data
# where learning_order in (
#                             select max(learning_order) from ttt_data
#                             where player = 1
#                             and c1 = 1 and c2 = 2 and c3 = 1 and c4 = 2 and c7 = 1 and c9 = 2
#                             and c5+c6+c8 = 1
#                             group by c5, c6, c8
#                         )
#     and player = 1;
#
# 123
# 456
# 789

#ex81) mit_ttt를 파이썬에서 출력
file= open("/Users/misoni/Desktop/pythondata/mit_ttt.txt",'r')
for i in file:
    line = i.strip("\n")
    mit_ttt = line.split(",")
    print(mit_ttt)

#ex82) pandas 모듈을 이용해서 사원 테이블에서 최대 월급을 출력하시오
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
print( emp['sal'].max())

result = emp[['ename','sal']][emp['sal']>=3000].sort_value
# 열 행
print(result)




#ex86) 부서번호가 20번인 사원들의 최대 월급을 출력하시오
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")

result = emp['sal'][emp['deptno']==20].max()

print(result)

#ex87) 직업, 직업별 토탈월급 출력
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")

result = emp.groupby('job')['sal'].sum()

print(result)

#ex88)부서번호, 부서번호 별 평균 월급을 출력
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")

result = emp.groupby('deptno')['sal'].mean()

print(result)

#ex89)아래의 결과를 pandas로 구현
import pandas as pd
ttt= pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/mit_ttt2.csv")
print(ttt)
result1 = ttt[ ( ttt['PLAYER']==1) &
               (ttt['C1'] == 1) &
                (ttt['C2'] == 2) &
                (ttt['C3'] == 1) &
                (ttt['C4'] == 2) &
                (ttt['C7'] == 1) &
                (ttt['C9'] == 2) &
                (ttt['C5']+ ttt['C6']+ ttt['C8'] == 1) ]
result2 = result1.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max()
print(result2)

#문제90. 직업이 SALESMAN인 사원들의 이름, 월급, 직업을 출력하시오
#pandas 이용
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename','sal','job']][emp['job']=='SALESMAN']

print(empresult)

#pandas 이용X
import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[2]=='SALESMAN':
        print(emp_list[1], emp_list[5],emp_list[2])



# ■ 기타 비교 연산자   -- 다른 산술 연산자들은 기본문법과 같음
#
# 오라클     VS           파이썬 기본    VS     파이썬 pandas 모듈
#
# between..and
# (>=)  and (<=)
# [(emp['sal']>=1000) & (emp['sal']<=3000)]
# in
# in
# emp['job'].isin
# is null
# ==''
# emp['comm'].isnull()
# like
# [0:1]
# apply 함수 +  lambda표현식



# 문제 91. 직업이 SALESMAN, ANALYST인 사원들의 이름과 월급, 직업을 출력하시오.
# pandas 모듈 이용:
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename','sal','job']][emp['job'].isin(['SALESMAN','ANALYST'])]

print(empresult)


# pandas 모듈 이용하지 않았을 때:
# import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[2] in ('SALESMAN','ANALYST'):
        print(emp_list[1], emp_list[5],emp_list[2])



# 문제92. 직업이 SALESMAN, ANALYST가 아닌 사원들의 이름, 월급, 직업을 출력하시오.
# pandas 모듈 이용:  힌트: pandas에서는 not을 ~로 표시

import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename','sal','job']][~emp['job'].isin(['SALESMAN','ANALYST'])]

print(empresult)

# pandas 모듈 이용하지 않았을 때:

import csv

file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[2] not in ('SALESMAN','ANALYST'):
        print(emp_list[1], emp_list[5],emp_list[2])



# 문제93. 커미션이 null인 사원들의 이름, 커미션을 출력하시오.
# pandas 모듈 이용:
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp_comm.csv")
empresult = emp[['ename','comm']][emp['comm'].isnull()]

print(empresult)


# pandas 모듈 이용하지 않았을 때:

import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[6]=='':
        print(emp_list[1], emp_list[6])



# 문제94. 커미션이 null이 아닌 사원들의 이름, 커미션을 출력하시오.
pandas 모듈 이용:              파일은 emp.csv로!
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp_comm.csv")
empresult = emp[['ename','comm']][~emp['comm'].isnull()]   #또는 .notnull()

print(empresult)


# pandas 모듈 이용하지 않았을 때:
import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[6]!='':
        print(emp_list[1], emp_list[6])



# D deptno 1 empno ename c job hiredate sal comm
# emp.csv 파일은 위와 같이 index가 있었다.
#
#
#
# 문제95. 월급이 1000에서 3000사이인 사원들의 이름과 월급을 출력하시오.
# pandas 모듈 이용:
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename','sal']][(emp['sal']>=1000) & (emp['sal']<=3000)]

print(empresult)



# pandas 모듈 이용하지 않았을 때:

import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    sal = int(emp_list[5])
    if sal>=1000 and sal<=3000:
        print(emp_list[1], emp_list[5])



# 문제96. 이름의 첫 글자가 S로 시작하는 사원들의 이름을 출력하시오.
# pandas 모듈 이용:
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename']][emp['ename'].apply(lambda x:x[0]=='S')]
                      # apply함수 안의 x는  ename 을 받아옴
print(empresult)

# * lambda 표현식이란?
# "여러줄의 코드를 딱 한 줄로 만들어주는 인자"

def plus(x,y):
return x+y
print(plus(10,20))

# 위의 코드를 lambda 표현식으로 표현하면?
print( (lambda x,y:x+y)(10,20) )

# pandas 모듈 이용하지 않았을 때:
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    if emp_list[1][0]=='S':
        print(emp_list[1])


# cf) lambda 표현식 사용한 예시들
mod = lambda x,y:x%y
print(mod(5,2))

sum = lambda x1,x2,y:x1+x2+y
print(sum(1,2,3))



# 문제97. 위의 문제 96번을 lambda 표현식을 쓰지 말고 함수를 직접 생성해서 수행하시오.

def firstAlIsS(var):
    if var[0]=='S':
        return var
    return ''

import csv

file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    answer = firstAlIsS(emp_list[1])
    if answer!='':
        print(answer)


# --lambda표현식 사용

import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename']][emp['ename'].apply(lambda x:x[0]=='S')]

print(empresult)




# 문제98. 이름의 끝글자가 'T'로 끝나는 사원들의 이름을 출력하시오.

import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp[['ename']][emp['ename'].apply(lambda x:x[len(x)-1]=='T')]

print(empresult)




# ■ group 함수를 이용한 결과 출력을 pandas를 이용했을 때와 이용하지 않았을 때를 비교

# * pandas의 기본 문법:
# emp 데이터 프레임 [열] [행]
            ↓
emp [ ['sal'] ] [emp['job'] =='SALESMAN']

# 그룹함수 -->  max, min, sum, mean, count
#                                                                 ↓
emp [ ['sal'] ] [emp['job'] =='SALESMAN'].max()   #직업이 SALESMAN인 사원들 중 최대월급
emp.groupby('job')['sal'].max()   #직업별 최대월급을 출력

# ANALYST CLERK MANAGER PRESIDENT 3000 13ØØ 2975 5ØØØ



# 문제99. 직업, 직업별 최대월급을 출력하는데 직업 SALESMAN은 제외하고 출력하시오.

import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
emp2 = emp[['job','sal']][emp['job'] !='SALESMAN']  #emp2에다 salesman뺀 데이터를 담고
empresult = emp2.groupby('job')['sal'].max()     #그 안에서 작업

print(empresult)



# 문제100.  부서번호, 직업, 부서번호별 직업별 토탈월급을 출력하시오.

# SQL> select job, deptno, sum(sal)
# from emp
# group by deptno,job;
#
# 파이썬  pandas를 이용해서:

import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
empresult = emp.groupby(['deptno','job'])['sal'].sum()

print(empresult)

# 10 20 30 CLERK MANAGER PRESIDENT ANALYST CLERK MANAGER CLERK MANAGER SALESMAN 13ØØ 2450 5ØØØ 19ØØ 2975 950 2850 56ØØ



# 어제 머신러닝 TTT 서브쿼리만 파이썬으로 구현해봤는데 이제 전체 구현해보자
#
# ■ pandas이용해서 오라클 서브쿼리 구현하는 방법
#
# 문제101. JONES보다 더 많은 월급을 받는 사원들의 이름, 월급을 출력하시오.
#
# select ename, sal
# from emp
# where sal > (select sal
#             from emp
# where ename='JONES')
#

# pandas로 구현  1. jones의 월급 구해서 변수에 담기 2.pandas
#
# JONES 월급 구하기
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
JONES_SAL = emp[['sal']][emp['ename']=='JONES']
print(type(JONES_SAL))         # type이 어떤 값이 아니라 pandas dataframe 으로 나옴
# 이것은 테이블같은 것. 테이블이면 형변환이 안 되므로
# 값이어야 함. 이렇게 해주는 것이 values


emp = pd.DataFrame.from_csv("D:\data\emp.csv")
JONES_SAL = emp[['sal']][emp['ename']=='JONES'].values[0]   #숫자형 리스트로 바뀜
print(type(JONES_SAL))

import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
JONES_SAL = emp[['sal']][emp['ename']=='JONES'].values[0]
empresult = emp[['ename','sal']][emp['sal']> JONES_SAL[0]]

print(empresult)


# 설명: 그냥  JONES_SAL하면 length가 안 맞는다고 나옴.
#
#
#
# 문제102. SCOTT의 직속상사 이름을 출력하시오.
# SQL> select ename from emp
# where empno = (select mgr
#                    from emp
# where ename='SCOTT'
#

# 아래처럼 하면 나온다는데 단체로 empno에러남.
import pandas as pd

emp = pd.DataFrame.from_csv("D:\data\emp.csv")
mgr = emp[['mgr']][emp['ename']=='SCOTT'].values[0]
empresult = emp[['ename']][emp['empno']==mgr[0]]

print(empresult)


emp=pd.read_csv("D:\emp.csv")  #로 바꿈( 인덱스 없어도 되게 하는 것)


import pandas as pd
emp=pd.read_csv("D:\emp.csv")
mgr = emp[['mgr']][emp['ename']=='SCOTT'].values[0]
print(mgr)
empresult = emp[['ename']][emp['empno']==mgr[0]]

print(empresult)




# 문제103. 관리자인 사원들의 이름을 출력하시오.
# pandas로:

import pandas as pd

emp=pd.read_csv("D:\emp.csv")     #index 없어도 걍 불러오기 되게 하는 방법
mgr = emp[['mgr']].values
empresult = emp[['ename']][emp['empno'].isin(emp['mgr'])]

print(empresult)



# 문제104. 컬럼 c5,c6,c8이 남아있을 때 어떤 수가 가장 좋은 수인가?
# (어제 마지막 문제에 서브쿼리 부분만 추가)
# 엔트로피  -- 어떤 컬럼이 가장 중요한 컬럼인가?
# 머신러닝  -- 게임진행 과정 중 중요한 컬럼은?


import pandas as pd

ttt = pd.DataFrame.from_csv("D:\data\mit_ttt2.csv")

a= ttt[ (ttt['PLAYER']==1) &
        (ttt['C1'] ==1) &
        (ttt['C2'] ==2) &
        (ttt['C3'] ==1) &
        (ttt['C4'] ==2) &
        (ttt['C7'] ==1) &
        (ttt['C9'] ==2) &
        (ttt['C5'] +ttt['C6']+ttt['C8']==1)]
result = a.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max()

b = []
for i in result:
    b.append(i)

result3 = ttt[ttt['LEARNING_ORDER'].isin(b)]
print(result3)



# ■ 5.3 딕셔너리 변수 (p. 110)
#
# 딕셔너리 자료형은 key 와 value를 조합해서 사용하는 자료형

# 예) dic = {}
#        dic['파이썬'] = 'www.python.org'
#                    ↓                          ↓
#                   key                      value
#
#        dic['애플'] = 'www.apple.com'
#


dic={}
dic['파이썬'] = 'www.python.org'
dic['애플'] = 'www.apple.com'
dic['마이크로소프트']='www.microsoft.com'

print(dic)    #그냥 dic써도 나옴
print(dic['애플'])
print(dic.keys())
print(dic.values())
#
# 결과:
# ' www.python . org ' www.micmDsoft . com ' } www.apple . com dict ' www.apple . com 'D [ 'www.python . org 'www.apple . com ' ' www.microsoft . com ' ] )
#

dic.pop('애플')  #애플인 요소를 삭제
dic.clear()    #전체 요소 삭제



# 문제 105. 딕셔너리 자료형을 이용해서 주어 0, 동사가 1, 명사 2 로 해서 한글과 영문을
# 저장하시오.

dic = {}
dic['나는'] = ('I',0)
dic['소녀'] = ('girl',2)
dic['이다'] = ('am',1)
dic['피자'] =  ('pizza',2)
dic['먹는다'] =  ('eat',1)

# dic   쳐서 다 들어갔나 확인
#
#
# 한글 어순: 나는 소녀입니다.  (주어 + 명사 + 동사)
# 영어 어순: i am a girl   (주어+동사+명사)
#
#
#
# 문제106. 한글을 물어보게 하고 한글을 입력하면 영어로 번역하는 프로그램을 파이썬으로 작성하시오.(어순만 변경해서)
#
# 번역할 한글을 입력하세요.  나는 소녀입니다.
# I am girl
#
# 카페: 한글을 영어로 번역하려면?
#
# #i
# #j      나는 0    --->   I 출력
#          소년 0    --->   패스
#          이다 0    --->   패스
#
dic = {}
dic['나는'] = ('I', 0)
dic['소년'] = ('boy', 2)
dic['이다'] = ('am', 1)
dic['피자를'] = ('pizza', 2)
dic['먹는다'] = ('eat', 1)
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)) :
    for j in input_list :
        if dic[j][1]==i :
            result = result + dic[j][0] + ' '
print(result)



# 문제107. SMT용 감성어 사전을 내려받아 csv파일을 파이썬에서 불러오시오.

import csv

file = open("D:\data\smt_dic.csv",'r')
smt_csv = csv.reader(file)

for smt_list in smt_csv:
    print(smt_list)




# 문제108.  문제107에서 0~4번째 요소만 출력하시오.

import csv

file = open("D:\data\smt_dic.csv",'r')
smt_csv = csv.reader(file)

for smt_list in smt_csv:
    if smt_list[0]!='':
        print(smt_list[0],smt_list[1],smt_list[2],smt_list[3],smt_list[4])




# 문제109. smt감성어 사건의 1번째 요소를 key로 하고 3번째 요소를 딕셔너리 변수의
# 0번째 요소로 하고 4번쨰 요소를 딕셔너리 변수의 4번째 요소로 지정해서 smt_dic 이라는 딕셔너리 자료형 변수를 생성하시오

import csv

smt_dic={}
file = open("D:\data\smt_dic.csv",'r')
smt_csv = csv.reader(file)

for smt_list in smt_csv:
    smt_dic[smt_list[1]]=(smt_list[3],smt_list[4])

print(smt_dic)



# 문제110. 무성이가 만든 감성어 사전과 진우가 만든 번역기를 이용해서 한글 영문 번역기를 완성시키시오.

import csv

smt_dic={}
file = open("D:\data\smt_dic.csv",'r')
smt_csv = csv.reader(file)

input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')

result = ''

for i in range(len(input_list)) :
    for j in input_list :
        if dic[j][1]==i :
            result = result + dic[j][0] + ' '
print(result)
 