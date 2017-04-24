#############################################################7.3가변변수 쓰일때
#### States as integer : manual coding
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [' ', 'X', 'O']
def printboard(state):
    """ Print the board from the internal state."""
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6)) #center: 가운데 정렬
    #print(cells) ['  X   ', '  O   ', '      ', '      ', '      ', '      ', '      ', '      ', '      '] #리스트변수
    #print(*cells)   #X      O    리스트 변수 요소 추출
    print(BOARD_FORMAT.format(*cells)) #*cell(리스트요소가 순서대로 들어감

printboard([[1,2,0],[0,0,0],[0,0,0]]) #names[숫자]: 리스트 요소, 순서대로 1행, 2행, 3행
print(BOARD_FORMAT.format('a','b','c','d','e','f','g','h','g'))
print(BOARD_FORMAT.format('x','o','x','o','x',' ',' ',' ',' '))
print(BOARD_FORMAT.format('x'.center(6),'o'.center(6),'x'.center(6),'o','x',' ',' ',' ',' '))

#############################################################7.4 매개변수 return이 함수 종료로 쓰일때
def enumstates(state, idx, agent):
    if idx > 8:
        player = last_to_act(state)
        if player == agent.player:
            agent.add(state)
    else:
        winner = gameover(state)
        if winner != EMPTY:
            return
        i = int(idx / 3)
        j = idx % 3
        for val in range(3):

               state[i][j] = val
               enumstates(state, idx+1, agent)