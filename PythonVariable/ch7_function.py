###############################7.2 기본값 매개변수와 키워드 매개변수
def print_string(text,count=1): #디폴트값을 원할때는 ' = 값' 써주면 됨
    for i in range(count):
        print(text)
    return ''
print_string('안녕하세요')
print_string('안녕하세요',3) #함수 생성시 print(text)로 해줘야  count만큼 나옴(none안나오게 하려면 return ''으로)

#ex149) 아래와 같이 이름만 넣으면 소속팀과 직위가 출력되는 함수를 생성하시오
# print_inform(name='장경원')
# 이름=장경원
# 소속팀=머신러닝팀
# 직위 = 팀원 (매개변수)
# print_inform(name='장경원',position='팀장')

def print_inform(name,position='팀원',team='머신러닝팀'):
    print('name = {0}'.format(name) )
    print('position = {0}'.format(position))
    print('team = {0}'.format(team))

print_inform('장경원')
print_inform('장경원','팀장')

###############################7.3 가변 매개변수
def merge_string(*text_list):
    result = ''
    for s in text_list:
        result += s + ' '
    return result

merge_string('아버지가','방에','들어가신다')

# ◼︎ 파이썬에서 *가 쓰이는 경우
# 1. 가변 매개변수
# 2. 리스트 변수 내의 요소들을 뽑아낼 때-->mit코드

###############################7.4 매개변수로 함수를 사용하는 경우
#함수 종료의미로 retrun을 사용하는 경우
def stop_func(num):
    for i in range(1,num+1):
        print('숫자 {0}을 출력합니다'.format(i))
        if i == 5:
            retrun #리턴 뒤에 아무것도 안적어주면 함수 종료 #break랑 뭐가 다른가
stop_func(10)

#ex151)아래와 같이 숫자를 입력하고 함수를 실행하면 숫자가 세로로 출력되게 하시오
#print_something(1,2,3,4,5) #얼마든지 숫자를 쓸 수 있어야함

def print_someting(*num_list):
    for i in num_list:
        print(i)
    return

print_someting(1,2,3,4,5,6,7,8,9) #이건 왜 none이 안나오지->오홍 함수라서 print일때만