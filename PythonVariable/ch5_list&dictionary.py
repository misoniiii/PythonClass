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

