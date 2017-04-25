###############################8.1 모듈이란
#모듈 생성 예
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


from PythonVariable.ch8_module import *

print(plus(1, 2))

#ex159) 오전에 만들었던 준호의 최대공약수 구하는 함수를 모듈화 하시오
#3개의 함수 스크립트 --> junho.py라는 이름으로 저장
#def gcdtwo(a,b):. def gcd(a):, def list(*n): )
# 새로운 창에서
# import gcd_junho
# gcd_junho.list(1000,500,250,100,25,5)


if _name_=="_main_":


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


##############8.3 모듈 찾는 방법
#방금 만든 calculator모듈의 위치는 우리가 직접 지정한 위치에 저장되어있었고 calc_test.py에서 calculator모듈을 불러올 수 있었음
#sys라는 모듈(random함수를 포함하고 있는 모듈)은 어디에 있는지
#파이썬은 import를 만나면 아래와 같은 순서로 모듈 파일을 찾아나선다
# 1. 파이썬 인터프리터 내장 모듈
# 2. sys.path에 정의되어 있는 디렉토리 탐색
#sys모듈은 파이썬의 내장 모듈

import sys
print(sys.builtin_module_names)

#sys.path의 내용을 출력해서 파이썬이 어떻게 모듈을 탐색해 나가는지 확인
import sys
for path in sys.path:
    print(path)

#ex161) 혜승이가 sys모듈의 random함수를 이용해서 구현해 낸 원주율 구하는 코드를 실행해보시오
