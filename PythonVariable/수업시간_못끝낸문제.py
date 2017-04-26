#4/25
######################중첩 gcd#####################################
def gcdtwo(a,b):                    # 두 수의 최대공약수를 출력
                                    # 분모가 0일경우 에러가 발생하므로 0인 경우를 따로 생각
    if min(a,b) == 0:               # 0과 A의 최대공약수는 무조건 A 이기 떄문에
        return max(a,b)             # 두 수중 최소값이 0인경우 두 수중 맥스값으로 최대공약수 출력
    return gcdtwo(b,a%b)            # 0이 아닌경우에 대해 유클리드호제법으로 재귀

def gcd(a):                         # 여러 수 중에서 최대공약수를 출력하는 알고리즘
    b=gcdtwo(max(a),min(a))         # 여러 수 중 두수를 뽑아서 최대공약수를 구하고
                                    # 다른 두수를 뽑아서 최대공약수를 구하고를 반복해서
    a.remove(min(a))                # 마지막에 남는 최대공약수가 전체의 최대공약수인 점을 이용
    a.remove(max(a))                # 정렬할 필요가 없게 전체 수에서 최대, 최소값을 뽑아서
                                    # 최대공약수를 구하는데 계산에 사용한 수는 제거하고
    a.append(b)                     # 위에서 구한 최대공약수를 리스트에 추가
    if max(a)==min(a):              # 위 과정을 재귀를 통해 반복하면 최대공약수만 2개 남는데
        print('최대공약수는 : ',a[0])  # 그경우에서 재귀를 종료하고 최대공약수를 출력
    else:
        gcd(a)


def list(*n):                       # 가변 매개변수로 데이터를 여러개 입력받으면
                                    # 튜플 형태이기 때문에 데이터 변경이 불가능
    a = []                          # 리스트를 생성하고 데이터 변경이 가능하도록
    for i in n:                     # 튜플 데이터를 잘라서 리스트에 입력
        a.append(i)
    gcd(a)                          # 최종적으로 생성한 리스트 변수를
                                    # 위에 생성한 최대공약수 함수에 입력해서 최대공약수 계산

if _name_=="_main_": #모듈을 불러올 때 이 문장 이후의 문장은 수행되지 않는다


######################탐욕쓰#####################################
def coinGreedy(money, cash_type):
    def coinGreedyRecursive(money, cash_type, res, idx):
        if idx >= len(cash_type): #화폐 다 사용 시 종료
            return res

        dvmd = divmod(money,cash_type[idx]) #divmond(362,100) => (3,62)
        res[cash_type[idx]] = dvmd[0]       #res[100] = 3
        return coinGreedyRecursive(dvmd[1],cash_type,res,idx+1)

    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬
    return coinGreedyRecursive(money,cash_type,{},0)

    #coinGreedyRecursive(362,[100,50,1],res,0) => 1 res= {}
    #coinGreedyRecursive(62,[100,50,1],res,1) => 2 res = {100:3}
    #coinGreedyRecursive(12,[100,50,1],res,2) => 3 res = {100:3, 50:1}
    #coinGreedyRecursive(0,[100,50,1],res,3) => 4 res ={100:3, 50:1, 1:12}


money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for key in res:
    print('{0}원 : {1}개'.format(key,res[key]))


######################표준편차#####################################
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