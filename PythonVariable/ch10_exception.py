def my_power():
    x = input('분자 숫자를 입력하세요')
    y = input('분모 숫자를 입력하세요')
    return int(x)/int(y)

print(my_power())

#ex179) 위의 코드에 예외처리 코드를 입혀서 분모로 0을 입력하면 0으로는 나눌 수 없습니다 라는 메세지가 출력되게 하시오
def my_power():
    try:
        x = input('분자 숫자를 입력하세요')       #문제가 없을 경우 실행할 코드
        y = input('분모 숫자를 입력하세요')
        return int(x)/int(y)

    except:
        print('0으로 나눌 수 없습니다')          #문제가 생겼을 때 실행할 코드

print(my_power())

#ex180) 이름을 물어보게하고 이름ㅇ르 입력하면 해당 사원의 월급이 출력되는 함수를 생성하시오
import csv
file = open('/Users/misoni/Desktop/pythondata/emp2.csv','r')

def find_sal():
    val = input('이름을 입력하세요')
    for i in csv.reader(file):
            if val.upper() == i[1]:
                return( i[5])

print(find_sal())


#ex179)위의 코드에 exception코드를 입혀서 없는 사원이름을 입력하면 해당 사원은 없습니다라는 메세지가 출력되게 하시오
import pandas as pd

def find_sal():
    try:
        emp=pd.DataFrame.from_csv('/Users/misoni/Desktop/pythondata/emp2.csv')
        name = input('해당 사원을 입력하세요')
        sal = emp[['sal']][emp[ename] == name.upper()].values[0]
        return sal
    except:
        print('해당 사원이 없습니다')
print(find_sal())


#ex180)이름을 물어보게하는데 일므을 입력하지 않으면 다시 질문을 하게하시오
import pandas as pd

def find_sal():
    emp=pd.DataFrame.from_csv('/Users/misoni/Desktop/pythondata/emp_col.csv')
    name =''
    while name == '':
        name = input('해당 사원을 입력하세요')
    sal = emp[['sal']][emp['ename'] == name.upper()].values[0]
    return sal

print(find_sal())

#ex181)위의 코드를 수정해서 없는 사원명을 입력하면 해당 사원은 없습니라고 출력되게 하시오
import pandas as pd

def find_sal2():
    try:
        emp = pd.read_csv('/Users/misoni/Desktop/pythondata/emp2.csv')
        name =''
        while name == '':
            name = input('해당 사원을 입력하세요')
        sal = emp[['sal']][emp['ename'] == name.upper()].values[0]
        return sal

    except:
        print('해당 사원은 없습니다')

print(find_sal2())

#ex182) 직업을 물어보게 하고 직업을 입력하면 해당 직업의 토탈월급이 출력되게 하시오
#아무것도 입력하지 않으면 계속 물어보게 하고 잘못된 직업명을 입력하면 해당직업은 없습니다라는 메세지가 출력되게 하시오

import pandas as pd
def find_sal3():
    try:
        emp= pd.read_csv('/Users/misoni/Desktop/pythondata/emp_col.csv')
        job = ''
        while job == '':
            job = input('해당 직업을 입력하세요')
        tot_sal = emp['sal'][emp['job'] == job ].sum()
        return tot_sal
    except:                                 #except처리가 안되고 0 (max인경우 nan으로 출력 사용자정의 예외처리로 해결
        print('해당 직업은 없습니다')
print(find_sal3())


####10.3 복수개의 except절 사용하기
#예외 처리를 여러개를 나열할 수 있다
#예제
def my_power():
    try:
        x = input('분자 숫자를 입력하세요')
        y = input('분모 숫자를 입력하세요')
        return int(x)/int(y)

    except ZeroDivisionError as err:
        print('0으로 나눌 수 없습니다',err)
    except :
        print('다른 예외 입니다')

print(my_power())


###10.4 try절을 무사히 실행하면 만날 수 있는 else
try:
    실행할 코드 블럭
except:
    예외처리 코드 블럭
else:
    except

#ex183)이름을 물어보게하고 해당 사원의 월급일 출력되게 하는데 이름이 없으면 해당 사원은 없습니다 라는 메세지가 나오게 하고
#만약 있어서 성공했다면 월급추출에 성공했습니다라는 메세지가 출력되게 하시오
import pandas as pd

def find_sal():
    try:
        emp= pd.read_csv('/Users/misoni/Desktop/pythondata/emp_col.csv')
        name = ''
        while name == '':
            name= input( '이름 입력하세요')
        sal =  emp['sal'][emp['ename'] == name.upper()].values[0]
        return sal
    except Exception as err:
        print('해당 사원은 없습니다')
    finally:
        print('월급 추출에 성공')
print(find_sal())


#ex184) 방금 사용한 else를 이용해서 아래의 나눈값을 출력되게 하는데 두수를 물어보게하고 나눈 값을 출력할 때 정상적으로 나눠지면
#나눈값을 잘 추출했습니다가 출력되게 하고 0으로나누면 0으로 나눌 수 없습니다가 출력되게 하시오

#분자를 입력하세요 10 #분자입력 10
#분모를 입력하세요 2  #분모를 입력 0
# 5입니다          #0으로 나눌 수 없습니다
# 나눈 값을 잘 추출했습니다

import pandas as pd

def find_sal():
    try:
        x = int(input('분자를 입력'))
        y = int(input('분모를 입력'))
        print(x/y)

    except ZeroDivisionError as err:
        print('0으로 나눌 수 없습니다')
    else:                           # 정상수행될때
        print('정상적으로 출력되었습니다')


print(find_sal())

############10.5 어떤 일이 있어도 반드시 실행되는 finally
#ex)예제
#  try:
#      실행할 코드 블럭
# except:
#     예외처리 코드 블럭
# finally:
#     실행할 코드가 성공/실패 여부 상관없이 무조건 실행

def find_sal():
    try:
        emp=pd.DataFrame.from_csv('/Users/misoni/Desktop/pythondata/emp_col.csv')
        name = ''
        while name =='':
            name = input('해당 사원을 입력하세요')
        sal = emp[['sal']][emp['ename'] == name.upper()].values[0]
        print(sal)
    except Exception as err:
        print('해당 사원이 없습니다')
    finally:
        print('저는 무조건 수행됩니다')
print(find_sal())

###########10.6 exception클래스
#파이썬의 모든 예외 형식은 base exception 클래스로부터 상속 받는 예외 형식이
#예제
def my_power():
    try:
        x = input('분자 숫자를 입력하세요')
        y = input('분모 숫자를 입력하세요')
        print( int(x)/int(y))
    except Exception as err:
        print("예외가 발생했습니다")

    except ZeroDivisionError as err:
        print("0으로 나눌 수 없습니다")

my_power()

#NotImplementedError 예외 사항 테스트
class bird:
    def fly(self):
        raise NotImplementedError
class eagle(bird):
    pass

eagle=eagle()
eagle.fly()

#ex185) eagle.fly()를 실행할 때 에러가 안나고 very fast라는 말이 출력될 수 있도록 오버라이딩 하시오
class bird:
    def fly(self):
        raise NotImplementedError
class eagle(bird):
    def fly(self):                          ### init? 아닌가
        print("very fast")

eagle=eagle()
eagle.fly()

#########10.7 사용자 정의 예외처리
#파이썬 입장에서 봤을 때는 오류가 아닌데 프로그래머가 이건 오류이다라고 raise문을 써서 예외처리하는 경우를 말함
#ex)
# def 함수명:
#     #실행코드
#     if 어떤 조건:
#         raise Exception('예외가 발생 ')
#     else:
#       return 변수명

#ex186) 이름을 입력하면 월급을 출력하는 함수를 만드는데 월급이 3000이상인 사원들은 해당 사원의 월급을 볼 수 없습니다라는 에러 메세지가 출력되게 하시오
import pandas as pd
def find_sal():
    emp = pd.read_csv('/Users/misoni/Desktop/pythondata/emp_col.csv')
    name = input('이름을 입력하세요')
    sal = emp['sal'][emp['ename'] == name.upper()].values[0]
    if sal >= 3000:
        raise Exception('해당사원의 월급을 볼 수 없습니다')
    else:
        return sal
print(find_sal())


import csv
def find_sal():
    file = open('/Users/misoni/Desktop/pythondata/emp_col.csv','r')
    name = input('이름을 입력하세요')
    for i in csv.reader(file):
        if i[1] == name.upper():
            if int(i[5]) >= 3000:
                raise Exception('해당사원의 월급을 볼 수 없습니다')
            else:
                return i[5]

print(find_sal())


