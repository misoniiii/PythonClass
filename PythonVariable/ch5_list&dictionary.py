
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

emp_list = ['a','b']
k= int(input('번호 입력 1번은 추가, 2번 제거, 3번 개수, 4번은 종료'))
while k !=  4:
    if k == 1 :
        emp_list.append(input('추가할 요소 입력'))
        k= int(input('번호 입력 1번은 추가, 2번 제거, 3번 개수, 4번은 종료'))
    elif k == 2:
        emp_list.remove(input('제거할 요소 입력'))
        k= int(input('번호 입력 1번은 추가, 2번 제거, 3번 개수, 4번은 종료'))
    elif k == 3:
        print(len(emp_list))
        k= int(input('번호 입력 1번은 추가, 2번 제거, 3번 개수, 4번은 종료'))
    elif k == 4:
        break


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


#ex83) 직업이 salesman인 사원들의 이름,월급,직업 출력
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
result = emp[['ename','sal']][emp['job']=='SALESMAN']
print(result)

import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
result = emp[emp['job']=='SALESMAN']
print(result) #특정열을 지정해주지 않으면 저넻 열 출력

#ex84)월급이 3000이상인 사원들의 이름,월급 출력
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
result = emp[['ename','sal']][emp['sal']>=3000]
print(result)

#ex85)위의 결과를 다시 출력하는데 월급이 낮은 사원부터 출력
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
result = emp[['ename','sal']][emp['sal']>=3000].sort_values('sal',ascending=True)
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

########0419
#######pandas

import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
empresult = emp [ ['ename','sal']]
print(empresult)

import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
empresult = emp #모든 열이 다 나옴
print(empresult)

#ex90) 직업이 salesman인 사원들의 이름,월급, 직업 출력
#pandas이용
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
empresult = emp [['ename','sal','job']][emp['job']=='SALESMAN']
print(empresult)

#pandas 이용하지 않고
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if ( emp_list[2] == 'SALESMAN'):
        print(emp_list[1],emp_list[5],emp_list[2])


#ex91)직업이 salesman,analyst인 사원들의 이름,월급,직업 출력
#pandas
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
empresult = emp[['ename','sal','job']][emp['job'].isin(['SALESMAN','ANALYST'])]
print(empresult)

#pandas이용x
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if  emp_list[2] in ['SALESMAN','ANALYST']:
        print(emp_list[1],emp_list[5],emp_list[2])

#ex92)직업이 salesman,analyst이 아닌 사원들의 이름,월급,직업 출력
#pandas
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
empresult = emp[['ename','sal','job']][~emp['job'].isin(['SALESMAN','ANALYST'])]
print(empresult)

#pandas이용x
import csv
file = open("/Users/misoni/Desktop/pythondata/emp2.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if  emp_list[2] not in ['SALESMAN','ANALYST']:
        print(emp_list[1],emp_list[5],emp_list[2])

#ex93)커미션이 null인 사원들의 이름과 커미션 출력 ############################################안나와
#pandas모듈 이용
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[['ename','comm']][emp['comm'].isnull()]
print(empresult)
#pandas이용 안했을 때
import csv
file = open("/Users/misoni/Desktop/pythondata/emp_comm.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[6] =='':
        print(emp_list[1],emp_list[6])

#ex94) 커미션이 null이 아닌 사원들의 이름,커미션 출력
#판다스
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[ ['ename','comm']][~emp['comm'].isnull()]
print(empresult)

#not null도 가능
#판다스 이용x
import csv
file = open("/Users/misoni/Desktop/pythondata/emp_comm.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[6] !='':
        print(emp_list[1],emp_list[6])

#ex95)월급이 1000에서 3000사이인 사원들의 이름,월급을 출력하시오
#pandas
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[ ['ename','sal']][ (emp['sal'] >= 1000) & (emp['sal'] <= 3000) ]
print(empresult)

#pandas x
import csv
file = open("/Users/misoni/Desktop/pythondata/emp_comm.csv", "r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if (int(emp_list[5])>= 1000) & (int(emp_list[5]) <= 3000):
        print( emp_list[1], emp_list[5])

#ex96)이름의 첫글자가 s로 시작하는 사원들의 이름 출력
#pandas
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[['ename', 'sal']][emp['ename'].apply(lambda x:x[0] == 'S') ]
print(empresult)

#lambda표현식!
def hap(x,y):
    return x+y
print(hap(10,20))

#위의 식을 lambda표현식으로 표현하면
print ( (lambda x,y: x+y)(10,20) )
#pandas x

#ex97)위의 96번 문제를 lambda표현식 쓰지말고 함수를 직접 생성해서 수행
###진우쓰
def p97(z) :
    if z[0] == 'S' :
        return True
    return False

import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[['ename','sal']][emp['ename'].apply(p97)]
print(empresult)

#ex98)이름의 끝글자가 T로 끝나는 사원들의 이름을 출력(lambda 표현식 사용해서 구현)
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[['ename', 'sal']][emp['ename'].apply(lambda x:x[-1] == 'T') ]
print(empresult)

## ◼︎◼ group 함수를 이용한 결과 출력을 pandas로 이용했을 때와 비교
#emp[['sal']][emp['job']=='SALESMAN']
#그룹함수: max, min, sum, mean, count
#emp[['sal']][emp['job']=='SALESMAN'].max()
#직업이 salesman인 사원들의 월급중에서 최대값
emp.groupby('job')['sal'].max()
#직업별 최대 월급 출력

#ex99) 직업,직업별 최대 월급을 출력하는데 직업이 salesman은 제외하고 출력
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp[['job', 'sal']][emp['job'] != 'SALESMAN' ]
print(type(empresult)) #<class 'pandas.core.frame.DataFrame'>
print(empresult.groupby('job')['sal'].max())

#ex100) 부서번호, 직업, 부서번호별 직업별 토탈월급을 출력하시오
# select deptno, job, sum(sal)
#   from emp
#   group by deptno, job;

#pandas
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col_comm.csv")
empresult = emp.groupby(['deptno','job'])['sal'].sum()
print(empresult)

#pandas를 이용해서 오라클 서브쿼리 구현 방법
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

# #ex101)jones보다 더 많은 월급을 받는 사원들의 이름과 월급 출력
# select ename, sal
#   from emp
#   where sal > (select sal from emp where ename = 'JONES')
#pandas
import pandas as pd
emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
#jones의 월급을 jonesal이라는 변수에 담는 코드
jones_sal = emp[['sal']][emp['ename'] == 'JONES'].values[0]
print(emp[['sal']][emp['ename'] == 'JONES'].values[0])
print(type(jones_sal))
#<class 'pandas.core.frame.DataFrame'> data.franme은 테이블같은 구조! ->  index sal 이렇게 나옴
#.values[0]하면 [2975] 출력됨 <class 'numpy.ndarray'> 숫자형 배열로 바뀜
#jonessal이라는 변수를 이용해 jonessal변수 안에 있는 값보다 더 큰 월급을 받는 사원들의 이름,월급을 출력하는 코드
print(jones_sal)
result = emp[['ename','sal']][emp['sal'] > jones_sal[0]] #왜 0을 붙여야하는지 모르겠음##################################
print(result)


#ex102)scott의 직속상사 이름을 출력하시오
# select ename
#   from emp
#   where empno = (select mgr from emp where ename = 'SCOTT')
import pandas as pd
#emp = pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/emp_col.csv") 안대유!!
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
#csv불러올 때 index도 같이 나오게 하는 거
scottmgr = emp[['mgr']][emp['ename'] == 'SCOTT' ].values[0]
result = emp[['ename']][emp['empno'] == scottmgr[0]]
print(result)

#ex103)관리자인 사원들의 이름을 출력하시오
import pandas as pd
emp = pd.read_csv("/Users/misoni/Desktop/pythondata/emp_col.csv")
result = emp[['ename']][emp['empno'].isin(emp['mgr'])]
print(result)

#ex104) 컬럼 c5,c6,c8이 남아있을 때 어떤수가 가장 좋은 수인가?######################################안대잉
#엔트로피 -->어떤 컬럼이 가장 중요한 컬럼인가
#인생을 살아보니 내가 어떠한 결정을 하는게 좋았따
#머신러 게임을 진행해가는 동안 즉 과정 중에 중요한 컬럼을 알아내는 것
#살면서 바로바로 어떤 선택을 해야할 때 가장 좋은 선택을 알려줌
# select * from ttt_data
# where learning_order in ( select max(learning_order) from ttt_data
#                             where player=1
#                             and c1=1 and c2=2 and c3= 1 and c4=2
#                             and c5+c6+c8 =1
#                             group by c5,c6,c8)
# and player = 1 ;

import pandas as pd
ttt= pd.DataFrame.from_csv("/Users/misoni/Desktop/pythondata/mit_ttt2.csv")
result1 = ttt[ ( ttt['PLAYER']==1) &
               (ttt['C1'] == 1) &
                (ttt['C2'] == 2) &
                (ttt['C3'] == 1) &
                (ttt['C4'] == 2) &
                (ttt['C7'] == 1) &
                (ttt['C9'] == 2) &
                (ttt['C5']+ ttt['C6']+ ttt['C8'] == 1) ]
result2 = result1.groupby(['C5','C6','C8'])['LEARNING_ORDER'].max().values
#values만 써도 됨
print(result2)

result3 = ttt[ttt['LEARNING_ORDER'].isin(result2) ]
print(result3)




##############################################################5.3 dictionary
dic = {}
dic['python']='www.python.org'
dic['apple']='www.apple.com'
dic['ms']='www.microsoft.com'
print(dic)

#print(dic)
#{'python': 'www.python.org', 'apple': 'www.apple.com', 'ms': 'www.microsoft.com'}

dic['apple'] #'www.apple.com'
dic.keys() #dict_keys(['python', 'apple', 'ms'])
dic.values() #dict_values(['www.python.org', 'www.apple.com', 'www.microsoft.com'])
dic.pop('apple') #apple 요소 삭제
dic.clear() #전체 다 삭제
print(dic) #{}

#ex105) 딕셔너리 자료형을 이용해서 주어가 0, 명사가 2, 동사가 1로 한글과 영문을 저장하시오
dic = {}
dic['나는'] = ('I',0)
dic['소년'] = ('boy',2)
dic['이다'] = ('am',1)
dic['피자'] = ('pizza',2)
dic['먹는다'] = ('eat', 1)


#한글 어순 : s + o + v
#영어 어순 : s + v + o

#ex106) 한글을 물어보게하고 한글을 입력하면 영어로 번역하는 프로그램을 파이썬으로 작성하시오
#번역할 한글을 입력하세요 ~ 나는 소년입니다
# I am boy
########진우 코딩
dic = {}
dic['나는'] = ('I', 0)
dic['소년'] = ('boy', 2)
dic['이다'] = ('am', 1)
dic['피자를'] = ('pizza', 2)
dic['먹는다'] = ('eat', 1)
print(dic) #{'나는': ('I', 0), '소년': ('boy', 2), '이다': ('am', 1), '피자': ('pizza', 2), '먹는다': ('eat', 1)}

result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ') #단어 쪼개기
print(input_list) #['나는', '소년', '이다']
for i in range(len(input_list)) : #i : 0
    for j in input_list :         #j : 나는
        if dic[j][1]==i :         # dic['나는'][1] == 0
                                  # dic['나는'] = ('I',0)
            result = result + dic[j][0] + ' ' #dic['나는'][0]
                                               # I
print(result)

#ex107) 카페에서 smt감성어 사전을 내려 받아 csv파일을 파이썬에서 불러오시
import csv
file = open("/Users/misoni/Desktop/pythondata/smt_dic_original.csv",'r',encoding='CP949')
smt_csv = csv.reader(file)
for smt_list in smt_csv:
    if smt_list[0] != '':
  # if smt_list[0:1] != ['','']
        print(smt_list[0:5])


#ex108) smt감성에 사전에서 1,3,5,요소만 출력
import csv
file = open("/Users/misoni/Desktop/pythondata/smt_dic.csv",'r',encoding='CP949')
smt_csv = csv.reader(file)
for smt_list in smt_csv:
    print(smt_list[1],smt_list[3],smt_list[4])

#ex109) smt감성어 사전에서 1번째요소를 key로하고 3번째 요소를 딕셔너리변수의 0번째 4번째요소를 딕셔너리변수의 4요소로 지정해서 smt_dic이라는 딕셔너리 자료형 변수를 생성
#smt_dic ={}
#smt_cid['짧다']=('short',1)
#smt_dic['참을성']=('patient',2)
import csv
smt_dic={}
file = open("/Users/misoni/Desktop/pythondata/smt_dic.csv",'r',encoding='CP949')
smt_csv = csv.reader(file)
for smt_list in smt_csv:
    smt_dic[smt_list[1]] = (smt_list[3],smt_list[4])

print (smt_dic['경솔'])

#ex110)무성이가 만든 감성어 사전과 진우가 만든 번역기를 이용해서 한글 영문 번역기를 완성 시키시오
#0 동사 1 주어 0 명사 2
import csv
smt_dic={}
file = open("/Users/misoni/Desktop/pythondata/smt_dic.csv",'r',encoding='CP949')
smt_csv = csv.reader(file)
for smt_list in smt_csv:
    smt_dic[smt_list[1]] = (smt_list[3],smt_list[4]) #3:영번역 #4:smt
    smt_dic[smt_list[2]] = (smt_list[3],smt_list[4]) #3:영번역 #4:smt
#smt_list
# 0  1  2 3 4
#-1 나는 나 I 0

#'나는':('I',0)
#'나' : ('I',0)

result = ''
input_kor = input('입력하세요. 우리는 게으르다:')
input_list = input_kor.split(' ')
print(input_list)
for i in range(len(input_list)) :
    for j in input_list :
        if int(smt_dic[j][1])==i :
            result = result + smt_dic[j][0] + ' '
print(result)


