# 틱택토 프로그램을 만들기 위해 필요한 기능
#     1. 보드판
#     2. 보드판 리셋
#     3. your move?어디에다가 수를 놓는지 물어보는거
#     4. 중간 중간 게임의 승리자가 결정되었는지 확인하는 기능
#     5. 게임이 다 끝나면 누가 이겼는지 알려주는 메세지를 출력해지는 기능
#     6. 게임순서에 맞춰서 x 다음에 o가 수행되고 play하는 기능
#     7. 게임이 한번만에 끝나는게 아니라 계속 진행이 되게 하는 기능
#ex187) (mit ttt) 1부터 9사이의 숫자를 받게해서 해당 숫자를 출력하는 함수를 생성하는데 1부터 9사이의 숫자가 아니면 잘못입력하셨습니다라는 에러메세지가 나오게하는 함수를 생성하시오
# 1 2 3
# 4 5 6
# 7 8 9
# print(get_number())
#숫자를 입력하세요 12
#잘못입력하셨습니다 하고 에러가 나게 하시오


def get_number():
    num = int(input('숫자를 입력하세요'))
    num_list = []
    for i in range(1,10):
        num_list.append(i)
    if num not in num_list:
        raise Exception('잘못 입력하셨습니다')
    else:
        return num
print(get_number())


#ex188) 위의 코드를 수정해서 1번부터 9번사이의 숫자를 입력하지 않았으면 숫자를 다시 물어보게 하시오
def get_number():
    num_list = []
    for i in range(1,10):
        num_list.append(i)

    while True:
        num = int(input('숫자를 입력하세요'))

        if num not in num_list:
            continue
        else:
            return num

print(get_number())


def get_number():
    num = 0
    while num>9 or num<1:
        num = int(input('숫자를 입력하세요'))
    return num
print(get_number())


#ex189) 머신러닝화하지 않은 mit코드 ttt를 수행해서 숫자를 1-9 외의 번호를 입력해보세요
import random
from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player
    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]
    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))
def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner
if __name__ == "__main__":
    p1 = Human(1)
    p2 = Human(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

#ex190) 이번에는 1부터 9번 사이외에 숫자를 넣으면 다시 물어보게 할 뿐만 아니라 입력을 안해도 다시 물어보게 코드를 수정하시오
#your move? 11

import random
from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player
    # 착수
    def action(self, state):
        printboard(state)
        action = ''
        while action not in ['1', '2', '3', '4', '5', '6', '7' , '8', '9']:
            action = input('Your move? ')
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[int(action)]
    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))
def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner
if __name__ == "__main__":
    p1 = Human(1)
    p2 = Human(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

#ex191) 생각해야할 문제에 경원이가 올린 코드를 수정해서 아무것도 입력안했을 때 다시 물어보게 하시오
def get_number():
    num =''
    while num == '' or int(num) not in range(1,10)  :
        num=input('숫자를 입력하세요')
    else:
        return num

get_number()



#ex192)아래의 리스트안에 리스트 변수에서 리스트 1에 해당하는 첫번째 리스트를 출력하시오
#    [리스트 1, 리스트2, 리스트3]

state = [ [1,2,0],[0,0,0],[[0,0,0]]]
print( state[0][1])

###########################################################TTT
#ex193) 아래의 printboard 함수에 print를 넣어서 디버깅하시오
################################################1. printboard 설명
EMPTY = 0
PLAYER_X = 1
PLAYER_X =2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [ ' ', 'X','O']

state =[ [1,2,0],[0,0,0],[0,0,0]]
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))  #state[0][0] -> 1 => 'X'
                                                        #state[0][1] -> 2 => 'O'
                                                        #state[0][2] -> 0 => ' '
    print(cells)                                        #['x','o', ' ', ' ', ' ', ' ', ' ', ' ' , ' ']
    print(*cells) #리스트에서 요소만 빼내는 거                 # X O
    print(BOARD_FORMAT.format(*cells))

print( printboard(state))


#################################################2. emptystate() 함수 설명 #한판 끝나고 리셋
def emptystate():
    reurn [ [EMPTY, EMPTY, EMPTY] ,[EMPTY, EMPTY, EMPTY] ,[EMPTY, EMPTY, EMPTY] ]

#ex195) 함수의 매개변수로 함수를 사용할 수 있다고 했습니다 printboard 매개변수로 emptystate()함수를 사용하면 결과가 어떤게 출력되는지 결과를 출력하시오
#cf) 파이썬 함수의 4가지 특징
    #변수에 할당될 수 있음
    state = emptystate()
    #다른 함수내에서 정의 될 수 있다
    #함수의 매개변수로 함수가 전달 될 수 있다
    #함수의 변환값이 될 수 있다
EMPTY = 0
PLAYER_X = 1
PLAYER_X =2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [ ' ', 'X','O']
def emptystate():
    return [ [EMPTY, EMPTY, EMPTY] ,[EMPTY, EMPTY, EMPTY] ,[EMPTY, EMPTY, EMPTY] ]

state = emptystate()

def printboard( state ):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

print( printboard(state))

#################################################3. gameover : 게임이 끝났는지(누가 이겼는지)를 결정하는 함수
##내가 봐야징 state =[ [1,2,0],[0,0,0],[0,0,0]]
# 00 01 02
# 10 11 12
# 20 21 22
#아래의 리스트를 하나씩 gameover에 넣어서 실행
EMPTY = 0
state = [[1,0,0] ,[ 0, 0 ,0],[0,0,0]]
#state = [[1,2,0],[0,0,0],[0,0,0]]
#state= [[1,0,0],[1,0,0],[1,0,0]]
#state=[[2,0,0],[0,2,0],[0,0,2]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:  #가로
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:  #세로
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지 => 게임 계속 진행하려고 비어있는 곳있는지 확인해보는거
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW


print( gameover(state))

#ex196) 아래 7번째 X를 찍어주고 리셋되게 하시오
import random
from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            printboard(state)
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            printboard(state)
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        printboard(state)
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        printboard(state)
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                 printboard(state)
                return EMPTY
    printboard(state)
    return DRAW
# 4. action : 어디에 수를 둘지 물어보는 함수 (your move)

def action(state):
    #printboard(state)
    action = None
    while action not in range(1, 10):
        action = int(input('Your move? '))
    switch_map = {
        1: (0, 0), #딕셔너리 키 : value
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    return switch_map[action]
print(action(state))


#ex197) 아무것도 입력하지 않으면 계속 물어보게 하시오
#혜승이

def action(state):
    #printboard(state)
    action = ''
    while action not in ['1', '2', '3', '4', '5', '6', '7' , '8', '9']: #왜 range일때는 안되지??
        action = input('Your move? ')
    switch_map = {
        1: (0, 0), #딕셔너리 키 : value
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    return switch_map[int(action)]
print(action(state))


def action(state):
    #printboard(state)
    action = None
    while action not in range(1, 10):
        try:
            action = int(input('Your move? '))
        except ValueError:
            continue
    switch_map = {
        1: (0, 0), #딕셔너리 키 : value
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    return switch_map[action]
print(action(state))

#5. episode_over : 게임 종료시 누가 이겼는지 비겼는지 메세지를 출력하는 함수
def episode_over(winner):
    if winner == DRAW:
        print('Game over! It was a draw.')
    else:
        print('Game over! Winner: Player {0}'.format(winner))
print(episode_over(3))


#6. play함수 : 실제로 게임을 진행하는함수, 게임종료 여부를 확인하고 결과를 리턴하는 함수
def play(agent1, agent2): #플레이어 1p,2p
    state = emptystate() #판 새로 리셋
    for i in range(9):  #0,1,2,3,4,5,6,7,8,9
        if i % 2 == 0:  #i 짝수(0,2,4,6,8)
            move = agent1.action(state) #move에 (0,1)값이 들어옴
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner

# 코드설명 :
# i= 0  짝수이므로  >  move = agent1.action(state)  수행 > action함수가 수행되면서 your move? 물어봄
# > 1을 입력하면 move에 (0,0)이 담기게 됨
# > state[0][0]로 첫번째 리스트의 첫번째 요소를 가르키는 인덱스
# > (0%2) + 1 = 1이 담기게 된다
# > state에 담기는 내용은 아래와 같음
# > [[1,0,0],[0,0,0],[0,0,0]]
# > 그리고 나서 바로 gameover함수에 state리스트를 넣고 게임이 종료 여부를 확인
#
#
# i = 1 일때  > move = agent2.action(state) 수행 > action함수 수행되면서 your move?
# >5 입력하면 move에 (1,1)이 담기게 됨
# > state[1][1]이 되고 가운데수를 가리키는 인덱스
# > 여기에 (1%2)+1 =2가 담기게 됨
# >state에 담기는 내용은 아래와 같음
# > [[1,0,0],[0,2,0],[0,0,0]]
# > 그리고 나서 gameover에 위의 state리스트를 넣어보고 게임 종료여부 확인


###########################################7. 메인 : 게임을 진행시키면서 게임을 무한 반
if __name__ == "__main__": #메인 모듈 아니면 실행하지 마라
p1 = Human(1) #human클래스를 p1으로 인스턴스화
p2 = Human(2) #human클래스를 p2으로 인스턴스화
while True: #무한루프
    winner = play(p1, p2) #한게임 진행
    p1.episode_over(winner) #play함수가 return 하는 winner를 받아 메세지 출력
    p2.episode_over(winner)


#ex198) 아래 코드를 이용해서 main함수를 생성하는데 무한루프가 아닌 게임횟수를 지정해서 수행되게 하시오
#main(2) 함수로
#전체코드에서 main부분을 바꾸면 게임을 2번 실행함
def main(val):
    p1 = Human(1) #human클래스를 p1으로 인스턴스화
    p2 = Human(2) #human클래스를 p2으로 인스턴스화
    while val > 0 : #무한루프
        winner = play(p1, p2) #한게임 진행
        p1.episode_over(winner) #play함수가 return 하는 winner를 받아 메세지 출력
        p2.episode_over(winner)
        val -= 1

main(2)

#ex199) 사람 vs 컴퓨터(랜덤)으로 게임할 수 있도록하시오
import random #숫자를 랜덤으로 발
#from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]
    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner

class Computer(object):
    def __init__(self, player):
        self.player = player #컴퓨터가 두번째 두면 player에 2가 담김

#state = [[1,0,0],[0,0,0],[0,0,0]]

    def random(self, state): #state가 요기로 들어감
            available = []      #비어있는 리스트 변수 선언
            for i in range(3):
                for j in range(3):
                    if state[i][j] == EMPTY:        #비어있는게 몇번인지 확인
                        available.append((i,j))     # [ (0,1), (0,2), (1,0) .... ]
            return random.choice(available)         # 윗줄에 있는 거 중에 아무거나 골라
#state = [[1,0,0],[0,0,0],[0,0,0]]
    # 컴퓨터가 착수
    def action(self, state):
        printboard(state) #보드판 그리고
        action = None
        move = self.random(state)                  #위에서 만든 랜덤함수를 호출 (아무거나 하나 골라서 move에 넣기)
        state[move[0]][move[1]] = self.player
        return move

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

if __name__ == "__main__":
    p1 = Human(1)
    p2 = Computer(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)


#ex200) 컴퓨터(랜덤)와 컴퓨터(랜덤)끼리 게임을 하게 하시오


import random #숫자를 랜덤으로 발
#from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]
    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner

class Computer(object):
    def __init__(self, player):
        self.player = player #컴퓨터가 두번째 두면 player에 2가 담김

#state = [[1,0,0],[0,0,0],[0,0,0]]

    def random(self, state): #state가 요기로 들어감
            available = []      #비어있는 리스트 변수 선언
            for i in range(3):
                for j in range(3):
                    if state[i][j] == EMPTY:        #비어있는게 몇번인지 확인
                        available.append((i,j))     # [ (0,1), (0,2), (1,0) .... ]
            return random.choice(available)         # 윗줄에 있는 거 중에 아무거나 골라
#state = [[1,0,0],[0,0,0],[0,0,0]]
    # 컴퓨터가 착수
    def action(self, state):
        printboard(state) #보드판 그리고
        action = None
        move = self.random(state)                  #위에서 만든 랜덤함수를 호출 (아무거나 하나 골라서 move에 넣기)
        state[move[0]][move[1]] = self.player
        return move

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

if __name__ == "__main__":
    p1 = Computer(1)
    p2 = Computer(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

#ex201) 컴퓨터(랜덤)와 컴퓨터(랜덤)과의 대결의 게임 진행 데이터를 test200.csv로 생성되게 하시오
import csv
import random #숫자를 랜덤으로 발
#from copy import copy, deepcopy
# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))

# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW
# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]
    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner

class Computer(object):
    def __init__(self, player):
        self.player = player #컴퓨터가 두번째 두면 player에 2가 담김

#state = [[1,0,0],[0,0,0],[0,0,0]]

    def random(self, state): #state가 요기로 들어감
            available = []      #비어있는 리스트 변수 선언
            for i in range(3):
                for j in range(3):
                    if state[i][j] == EMPTY:        #비어있는게 몇번인지 확인
                        available.append((i,j))     # [ (0,1), (0,2), (1,0) .... ]
            return random.choice(available)         # 윗줄에 있는 거 중에 아무거나 골라
#state = [[1,0,0],[0,0,0],[0,0,0]]
    # 컴퓨터가 착수
    def action(self, state):
        printboard(state) #보드판 그리고
        action = None
        move = self.random(state)                  #위에서 만든 랜덤함수를 호출 (아무거나 하나 골라서 move에 넣기)
        state[move[0]][move[1]] = self.player
        Fn = ("/Users/misoni/Desktop/pythondata/Test200.csv")
        w = csv.writer(open(Fn, 'a'), delimiter=',')
        w.writerow([state[0][0],
                    state[0][1],
                    state[0][2],
                    state[1][0],
                    state[1][1],
                    state[1][2],
                    state[2][0],
                    state[2][1],
                    state[2][2]])
        return move

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))

if __name__ == "__main__":
    p1 = Computer(1)
    p2 = Computer(2)
    while True:
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

#ex202) 게임 과정의 데이터 말고 게임 종료된 결과 데이터만 수집되게 하시오
#         Fn = ("/Users/misoni/Desktop/pythondata/Test300.csv")
#         w = csv.writer(open(Fn, 'a'), delimiter=',')
#         w.writerow([state[0][0],
#                     state[0][1],
#                     state[0][2],
#                     state[1][0],
#                     state[1][1],
#                     state[1][2],
#                     state[2][0],
#                     state[2][1],
#                     state[2][2]])
#
# 아래코드를 어느 함수에 추가
#융성이 방법 ( draw는 안들어감) #카페 참고

#ex203) 위의 코드를 수정해서 게임의 승패여부도 출력되게 하시오
#융성(잘나옴)
import random,csv
from copy import copy, deepcopy

# deepcopy : 메모리를 완전히 새롭게 생성
# copy : 껍데기만 카피, 내용은 동일한 곳을 가리킴
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']


# 보드 출력
def printboard(state):
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(BOARD_FORMAT.format(*cells))


# 빈 판
def emptystate():
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def gameover(state):
    # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
    for i in range(3):
        if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
            return state[i][0]
        if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
            return state[0][i]
    # 좌우 대각선
    if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
        return state[0][0]
    if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
        return state[0][2]
    # 판이 비었는지
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                return EMPTY
    return DRAW


# 사람
class Human(object):
    def __init__(self, player):
        self.player = player

    # 착수
    def action(self, state):
        printboard(state)
        action = None
        while action not in range(1, 10):
            action = int(input('Your move? '))
        switch_map = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        return switch_map[action]

    def episode_over(self, winner):
        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))


def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            Fn = ("/Users/misoni/Desktop/pythondata/Test999.csv")
            w = csv.writer(open(Fn, 'a'), delimiter=',', lineterminator='\n')
            w.writerow([state[0][0],
                        state[0][1],
                        state[0][2],
                        state[1][0],
                        state[1][1],
                        state[1][2],
                        state[2][0],
                        state[2][1],
                        state[2][2],
                        winner ])
            return winner
    return winner


class Computer(object):
    def __init__(self, player):
        self.player = player

    def random(self, state):
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i, j))
        return random.choice(available)

    # 컴퓨터가 착수
    def action(self, state):
        printboard(state)
        action = None
        move = self.random(state)
        state[move[0]][move[1]] = self.player

        # Fn = ("D:\data\Test200.csv")
        # w = csv.writer(open(Fn, 'a'), delimiter=',', lineterminator='\n')
        # w.writerow([state[0][0],
        #             state[0][1],
        #             state[0][2],
        #             state[1][0],
        #             state[1][1],
        #             state[1][2],
        #             state[2][0],
        #             state[2][1],
        #             state[2][2]])
        #
        return move

    def episode_over(self, winner):



        if winner == DRAW:
            print('Game over! It was a draw.')
        else:
            print('Game over! Winner: Player {0}'.format(winner))


def main(num):
    p1 = Computer(1)
    p2 = Computer(2)
    cnt =0
    while cnt<num:
        cnt+=1
        winner = play(p1, p2)
        p1.episode_over(winner)
        p2.episode_over(winner)

main(100)

#ex206) 10만번 학습시킨 csv파일을 생성하시오 ( 컴퓨터(ai) vs 컴퓨터(ai) )
def backup(self, nextval):
    if self.prevstate != None and self.learning:
        prevval = self.values[self.prevstate]
        self.values[self.prevstate] += self.alpha * (nextval - self.prevscore)
        Fn = open("/Users/misoni/Desktop/pythondata/learn01million.csv", 'a')
        w = csv.writer(Fn, delimiter=',')
        w.writerow([self.prevstate[0][0],
                   self.prevstate[0][1],
                   self.prevstate[0][2],
                   self.prevstate[1][0],
                   self.prevstate[1][1],
                   self.prevstate[1][2],
                   self.prevstate[2][0],
                   self.prevstate[2][1],
                   self.prevstate[2][2],
                    prevval,
                   self.values[self.prevstate],
                   self.player,
                    self.gamenum,
                   self.rownum])
        Fn.close()
        self.rownum += 1