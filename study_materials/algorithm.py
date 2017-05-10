# #1-1 단어 세기
# def WordCount(str):
#     word =str.split() #공백 기준 단어 자르기
#     distinct = list(set(str.split()) #담는게 아니라 정리만 해주고 넘겨줌 #리스트 끼리 비교라서 list를 써주긴했는데 안써줘도 개수는 나옴
#     for guide in distinct:
#         cnt = 0
#         for piece in word:
#             if piece == guide:
#                 cnt += 1
#         print( guide , cnt )
#
# sentence = input('문장을 입력하세요')
#
# while True:
#     if len(sentence) <= 200:
#         if sentence.upper() != 'END':
#             WordCount(sentence)
#             sentence = input('문장을 입력하세요')
#         if sentence.upper() == 'END':
#             break
#     else:
#         sentence = input('너무 길어요. 200자 이내로 문장을 입력하세요')
# #while <= 200 하고 싶은데 아닐 경우 다시 입력을 못하겠음

###################################################################################################
## 1. 문제        : 오류고정 (고급)
## 2. 소요 시간   : 0.0 초 (소수점 6자리 반올림)
## 3. 사용 메모리 : 163840 byte
## 4. 만든 사람   : 길용현
###################################################################################################


def wordcount():
    sentence = ''
    wordlist = []
    while len(sentence) <= 200:
        sentence = input('문장을 입력하세요')
        if sentence != 'END':
            for i in sentence.split():
                wordlist.append(i)
            print(len(set(wordlist)))
        else :
            break
wordcount()

# def word_cnt():
#     a = ''
#     while a != 'END':
#         c=[]
#         a = str(input('단어를 입력하세요!'))
#         if len(a) <= 6:
#             b = a.split()
#             c = list(set(b))
#             c.sort()
#             for i in c:
#                 if i != 'END':
#                     cnt = 0
#                     cnt += b.count(i)
#                     print(i,':',cnt)
#
# print(word_cnt())
#




# #1-2
# def addSentence():
#     sentence = input('문장을 입력하세요')
#     addword = []
#     while True:
#         piece = set(sentence.split()) #입력한 문장 중복제거해서 단어별로
#         if len(sentence) <= 50 and len(sentence.split()) <= 10:
#             if sentence not in 'END':
#                 anotherSen = input('문장을 입력하세요')  # add sentence
#                 for i in anotherSen.split():
#                     if i not in piece:
#                         addword.append(i)
#                         print(addword)
#                 for j in addword: #없는 단어 붙이기
#                     sentence = sentence + ' ' + j
#                 print(sentence)
#
# addSentence()
# # 두개라고 생각하고 짜니까 코드가 두쌍씩으로만 실행됨
# # 중복 제거하려고 set만 쓰다보니까 순서x

def addword():
    s1 = ' '
    word = []
    while True:
        s1 = input('문장을 입력하세요')  #두번째 문장 입력
        if s1 == 'END':
            break
        sp_s1 = s1.split()          #입력한 문장을 공백 기준 단어별 쪼개기              # 두번째 문장 단어별 쪼개기
        if len(s1) <= 50 and len(sp_s1) <= 10:
            for i in sp_s1:             #단어 순서별로 i로 들어감
                if i not in word:       #입력한 문장의 단어가 word에 없으면               #중복되더라도 순서대로 한번씩만 들어감
                    word.append(i)      #word에 붙여짐 ( 처음 문장 입력시 word에는 처음 입력한 문장이 들어감)
            print(' '.join(word))

addword()

##궁금쓰 while s1 != 'END'로는 END입력해서 끝나게 못하나???