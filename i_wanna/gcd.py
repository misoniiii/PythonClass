###용현ver
def returnGCD(num_list):
    num_list = list(map(lambda x: int(x), num_list))
    max_num = max(num_list)

    i = 2
    gcd = 1  # 최대 공약수
    cnt = 0

    while True:
        # 입력 받은 수에 대해 특정 i 값으로 나눈값이 모두 0인 것을 찾는 루프문
        for num in num_list:
            if num % i == 0:
                cnt += 1

        # 특정 i 값에 대해 입력 받은 모든 수가 다 나누어졌는지 확인
        if cnt == len(num_list):
            gcd *= i  # 최대공약수
            num_list = list(map(lambda x: x/i, num_list))  # 입력받은 수
            i = 1  # i 값 리셋

        i += 1  # i 값 리셋
        cnt = 0  # cnt 리셋

        if i == max(num_list):
            break

    return gcd

num_list = input('최대 공약수를 알고 싶은 n개의 숫자를 입력하세요.').split(' ')

print(returnGCD(num_list))

################################################################
def returnGCD(num_list):
    num_list = list(map(lambda x: int(x), num_list))
    max_num = max(num_list)

    i = 2
    gcd = 1  # 최대 공약수
    cnt = 0

    while True:
        # 입력 받은 수에 대해 특정 i 값으로 나눈값이 모두 0인 것을 찾는 루프문
        for num in num_list:
            if num % i == 0:
                cnt += 1

        # 특정 i 값에 대해 입력 받은 모든 수가 다 나누어졌는지 확인
        if cnt == len(num_list):
            gcd *= i  # 최대공약수
            num_list = list(map(lambda x: x/i, num_list))  # 입력받은 수
            i = 1  # i 값 리셋

        i += 1  # i 값 리셋
        cnt = 0  # cnt 리셋

        if i == max(num_list):
            break

    return gcd

num_list = input('최대 공약수를 알고 싶은 n개의 숫자를 입력하세요.').split(' ')

print(returnGCD(num_list))

###########################################################################

def eucli(num_list):
    num_lit = list(map(lambda x : int(x) , num_list))
    max_num = max(num_list)

    for num in num_list

num_list = '18 36 24'
num_list = list(map(lambda x : int(x) , num_list))


a = '18 36 24'
a = a.split(' ')
a = list(map(lambda x:int(x),a))
a. sort() #
print(a)

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


