# Command + B: Go to def.
# Command + [, ]: Back, Forward
# Alt + Space: Preview (이거 진짜 강추)
# Command + Shift + F: Find all
# Command + L: Go to line
# Alt + Command + O: Go to symbol (Anything)
# F3: Toggle bookmark
# Alt + F3: Toggle custom bookmark (Numeric, Alphabet..)
# Command + F3: Show bookmarks
# Ctrl + R: Run
# Ctrl + D: Debug
# Command + R: Rerun
# Shift + Command + R: Resume on debugging
# Command + F2: Stop
# Shift + F6: Rename
# Command + F8: Toggle break point
#option+shift+e


##############################################
#4/24 return과 break차이점
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

print_someting(1,2,3,4,5) #print쓰면 none하고 같이 출력/ 함수 쓰면 그냥 나옴


def factorial(num):                         #10
    if num > 1:
        return factorial(num-1) * num       #10-1=9
    elif num == 1:
        return 1

print(factorial(5))


def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b - 1)
    value = a + rest
    return value
print("3 * 2 = ", mult(3, 2))


