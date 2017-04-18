# -*- coding: utf-8 -*-
#####Chap4. 데이터 다루기

#ex1) 위의 d 리스트 변수에서 1000을 출력하시오
d = [1000, 2000, 3000,4000]
print(d[0])

#ex2) d리스트 변수안에 있는 요소들을 하나씩 출력하시오
d = [1000, 2000, 3000,4000]
for i in d: #변수명
    print(i)

for i in range(100):
    print(i)    #0~99까지 100개 출력됨
         #설명: 파이썬은 세미콜론을 사용하지 않고 그냥 콜론 사용
         #반드시 콜론을 써줘야하는 문법
         ##IF, WHILE LOOP, FOR LOOP, def 함수 생성 시 사용

#ex3) a라는 리스트변수에 아래의 내용을 담고 출력하시오
a = ['7839','KING','PRESIDENT','0','1981-11-17','5000','','10']
print(a)

#ex4)a라는 변수안에 잇는 요소들을 끄집어 내서 출력하시오
for i in a:
    print(i)

#ex5) a 리스트 변수에서 7839만 출력하시오
print(a[0])

##len함수
a = ['7839','KING','PRESIDENT','0','1981-11-17','5000','','10']
cnt = len(a)
print(cnt)

                                        #none(오라클의 null)

# ex6) 카페에서 파이썬 수업자료에 emp2.csv를 내려받아 D드라이브 밑에 data라는 폴도에 다운받고 아래와 같이 수행
import csv  #csv모듈(아나콘다 내장) inport
file = open("D:\data\emp2.csv",'r') # r:  read
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list)
#ex7)위의 결과에서 사원번호만 출력하시오
import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[0])

#ex8)이름과 월급을 출력하시오
import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5])


#ex9) 위의 14개 리스트 변수 요소의 개수를 아래와 같이 출력하시오
#결과
#8
#8(14개)
import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(len(emp_list))

#ex10)이름과 이름의 길이를 아래와 같이 출력하시오
import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],len(emp_list[1]))

#ex11) 사원번호, 이름, 월급 출력
import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[0],emp_list[1],emp_list[5])

#ex12) 이름과 연봉을 출력하시오
#csv에서 불러오는 데이터는 기본적으로 문자라서 변환을 해줘야함
import csv
file = open("D:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],int(emp_list[5])*12)

#ex13)이름과 커미션을 출력하는데 커미션이 none이면 0으로 출력하시오
def ifnull(var,val):
    if var is '':
        return val
    return var


import csv
file = open("D:\data\emp_comm.csv",'r')
emp_comm_csv = csv.reader(file)
for emp_list in emp_comm_csv:
    print(emp_list[1],ifnull(emp_list[6],0))

#ex14)이름, 월급+커미션 출력
def ifnull(var,val):
    if var is '':
        return val
    return var


import csv
file = open("D:\data\emp_comm.csv",'r')
emp_comm_csv = csv.reader(file)
for emp_list in emp_comm_csv:
    print(emp_list[1],int(emp_list[5])+int(ifnull(emp_list[6],0)))


#ex15) 이름과 직업을 출력하는데 소문자로 출력하시오
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1].lower(), emp_list[2].lower() )

#ex16) MIT TTT 코드이해를 위해 중요한 기초 문제
#이름을 출력하는데 이름의 첫번째 철자만 출력하고, 소문자로 출력하시오
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0].lower())

#ex17)이름을 출력하는데 이름의 두번째 철자부터 마지막까지 소문자로 출력
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][1:].lower())


slicing = [ '01234567890','abcdefghi','0123abcdefghi']
print(slicing[0:][1])


#ex18)이름의 첫번째 첫자는 대문자로 출력하고 나머지는 소문자로 출력하시오
def initcap(val):
    return val[0].upper()+val[1:].lower()

import csv

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(initcap(emp_list[1]))

#ex19) 이름의 첫번째 철자부터 세번째 철자까지 출력되게 하시오

import csv

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0:3])

#ex20)이름의 첫번째 철자부터 세번째 철자가 출력되게 하는데 substr함수를 만들어서 출력되게 하시오
def substr(var,num1,num2):
    return var[num1-1:num2]

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(substr(emp_list[1],1,3))


#ex21)이름과 월급을 출력하는데 월급을 출력할 때 0대신에 *를 출력하시오
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5].replace('0','*'))


#ex22)이름과 월급을 출력하는데 월급을 출력할 대 0~2를 *로 출력하시오
#[re 정규식함수]
#sub(pattern,repl, string)
#string에서 pattern과 일치하는 부분에 대해서 repl로 교체
import re #정규식 모듈 import
import csv

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],re.sub('[0-2]','*',emp_list[5]))

#ex23)이름과 이름의 길이 출력
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    print(emp_list[1], len(emp_list[1]))

#ex24)아래의 split함수의 예제를 수행해보시오
file = 'a b c d e f g'
print(file.split(' ')) #공백으로 분리해서 리스트 생성

#ex25) 아래의 file변수의 요소들을 리스트변수로 담아내서
#두번째 요소인 b만 출력
file = 'a b c d e f g'
print(file.split(' ')[1])

#ex26)겨울왕국 대본을 공백을 구분으로 누고 나눠서 리스트 변수로 저장되게 하시오
file = open("D:\data\겨울왕국_대본.txt",'r')
for winter_list in file:
    print( winter_list.split(' ') )

#ex27) 위의 스크립트를 이용해서 겨울왕국 각 리스트 변수 안에 단어가 몇개가 있는지 아래와 같이 출력되게 하시오

file = open("D:\data\겨울왕국_대본.txt",'r')
for winter_list in file:
    a = winter_list.split(' ')
    print(len(a))

#ex28)위의 숫자들을 다 더한 값을 출력하시오
sum=0
file = open("d:\data\겨울왕국_대본.txt",'r')
for winter_list in file:
    a = winter_list.split(' ')
    sum = sum + len(a)
print(sum)

#ex29)겨울왕국에서 elsa가 몇번 나오는지 확인
#예제
a='Hello'
b=a.count('l')
print(b)

sum=0
file = open("d:\data\겨울왕국_대본.txt",'r')
for winter_list in file:
    a = winter_list.split(' ')
    sum = sum + a.count('Elsa')
print(sum)


#ex30)emp.csv에서 14개의 리스트 변수 중에 5번째 요소(월급) 부분만 담아서 리스트 변수로 아래와 같이 생성하시오
#append()
#[5000,2850,5450,......,1300]
#ex)
a=[1,2,3]
b=a.append(4)
print(a)

#ex)
b=[]
b.append(1)
b.append(2)
b.append(3)
print(b)

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
b =[]
for emp_list in emp_csv:
    b.append(int(emp_list[5]))
print(max(b))

#ex31)겨울왕국 대본을 단어별로 출력하시오
#['anna','elsa','She','YOu']
#['anna','elsa','She','YOu','ORDERS']
#       for loop            for loop
#txt-------------->list변수-------------> 하나의 단어
#ex)하나의 단어
a=['anna','elsa','She','YOu']
for i in a:
    print(i)


file = open("d:\data\겨울왕국_대본.txt",'r')
for winter_list in file: # file:스크립트
    a = winter_list.split(' ') #면 리스트가 나옴
    print(a)
    for word in a:  #리스트일 때  for 돌리면
        print(word) #단어가 나옴

#ex32)31번의 결과르 하나의 리스트로 만드시오
b=[]
file = open("d:\data\겨울왕국_대본.txt",'r')
for winter_list in file: #스크립트-->리스트변수
    a=winter_list.split(' ')

    for word in a: #리스트변수 ->단어만 추출
        b.append(word)
print(b)

#ex33)출력된 단어들 중에 \n은 잘라내시오
b=[]
file = open("d:\data\겨울왕국_대본.txt",'r')
for winter_list in file:
    a = winter_list.split(' ')

    for word in a:
        no_n = word.strip('\n')
        print(b.append(no_n))
print(b)

#ex34) rpad함수를 생성하고 아래와 같이 실행되게 하시오
#월급을 출력할때 전체 10자리를 잡고 남은 왼쪽에 *를 채워넣으시오
def rpad(var,num,val):
        for _ in range(num-len(var)):
            var = var + val
        return(var)

def lpad(var,num,val):
        for _ in range(num-len(var)):
            var = val + var
        return(var)

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], lpad(emp_list[5],10,'*'))
########4/17
#ex35)instr함수를 파이썬으로 구현하시오
def instr(word, target):
    for i in range(0,len(word)):
        if  word[i]==target:
            return i+1

#ex36)이름, 이름에 M자가 몇번째 자리에 있는지 출력하시오
import csv
def instr(word, target):
    for i in range(0,len(word)):
        if  word[i]==target:
            return i+1

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],instr(emp_list[1],'M')) #대문자 조심쓰

#ex37)이름,월급,보너스를 출력하는데 보너스는 월급의 15퍼센트로 출력하시오
import csv

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5],round(int(emp_list[5])*0.15))

#ex38) 위의 결과르 다시 출력하는데 컬럼명도 출력되게 하시오
import csv

file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
print('이름','월급','보너스')
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5],round(int(emp_list[5])*0.15))

#ex39)위의 결과를 다시 출력하는데 소숫점이하는 안나오고 반올림 되게 하시오
#ex40) 보너스를 출력할 때 소숫점 이하를 trunc를 써서 잘라내시오
import csv
import math
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
print('이름','월급','보너스')
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5],math.trunc(int(emp_list[5])*0.15))

#ex41)input명령어를 이용해서 숫자를 입력받아 해당 숫자가 짝수인지 홀수인지 출력되게 하시오
a= input('첫번째 숫자 입력')
b= input('두번째 숫자 입력')

result = int(a) + int(b) # 문자형일 경우 연결 연산자., 숫자형 변환 해줘야함!!
print(result)

c=int(input('숫자 입력하세요')) #매번 써줘야 하니까 여기다가
if c%2==0: # % 나머지
    print('짝수')
else:
    print('홀수')

#ex42) power함수를 이용해서 아래의 프로그램을 구현사시오
#숫자를 입력하세요! 2
#숫자를 입력하세요! 3
# 8입니다
a = int(input('밑을 입력하세요'))
b = int(input('지수를 입력하세요'))

print( pow(a,b))



#ex43) 오늘 날짜를 출력하시오
import datetime
today = datetime.date.today()
print(today)

#
from datetime import date
print(date.today())

#ex44) 오늘부터 세달뒤의 날짜를 출력하시오
from datetime import date
from dateutil.relativedelta import relativedelta

result = date.today() + relativedelta(months=+3)
print(date.today())
print(result)


#ex55)
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[0]) == 7788:
        print(emp_list[1],emp_list[5])

#ex56) 월급이 3000이상인 사원들의 이름과 월급을 출력하시오
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[5]) >= 3000:
        print(emp_list[1],emp_list[5])


#ex57)1981년 11월 17일에 입사한 직원 이름, 입사일 출력
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[4] == '1981-11-17':
        print(emp_list[1],emp_list[4])
#ex58)(TTT프로그램을 이해하는데 중요한 문제)
    #81년도에 입사한 사원들의 이름과 입사일을 출력하시오
import csv
file = open("d:\data\emp2.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[4][0:4]) == 1981:
        print(emp_list[1], emp_list[4])

#ex59) 아래의 리스트 변수에서 positive라는 단어는 몇개 나오는가
word = ['winter','cold','positive','neagative']
sum= 0
for i in word:
    if 'positive' == i:
        sum = sum + 1
print(sum)
#ex60)
word = ['winter', 'cold', 'positive', 'negative']
sum = 0
for i in word:
    if i in ['positive','negative']:
        sum = sum + 1
print(sum)

positive=['a+','abound','abounds','abundance','abundant','accessable','accessible','acclaim','acclaimed','acclamation','accolade','accolades','accommodative','accomodative','accomplish','accomplished','accomplishment','accomplishments','accurate','accurately','achievable','achievement','achievements','achievible','acumen','adaptable','adaptive','adequate','adjustable','admirable','admirably','admiration','admire','admirer','admiring','admiringly','adorable','adore','adored','adorer','adoring','adoringly','adroit','adroitly','adulate','adulation','adulatory','advanced','advantage','advantageous','advantageously','advantages','adventuresome','adventurous','advocate','advocated','advocates','affability','affable','affably','affectation','affection','affectionate','affinity','affirm','affirmation','affirmative','affluence','affluent','afford','affordable','affordably','afordable','agile','agilely','agility','agreeable','agreeableness','agreeably','all-around','alluring','alluringly','altruistic','altruistically','amaze','amazed','amazement','amazes','amazing','amazingly','ambitious','ambitiously','ameliorate','amenable','amenity','amiability','amiabily','amiable','amicability','amicable','amicably','amity','ample','amply','amuse','amusing','amusingly','angel','angelic','apotheosis','appeal','appealing','applaud','appreciable','appreciate','appreciated','appreciates','appreciative','appreciatively','appropriate','approval','approve','ardent','ardently','ardor','articulate','aspiration','aspirations','aspire','assurance','assurances','assure','assuredly','assuring','astonish','astonished','astonishing','astonishingly','astonishment','astound','astounded','astounding','astoundingly','astutely','attentive','attraction','attractive','attractively','attune','audible','audibly','auspicious','authentic','authoritative','autonomous','available','aver ','avid ','avidly','award','awarded','awards','awe  ','awed ','awesome','awesomely','awesomeness','awestruck','awsome','backbone','balanced','bargain','beauteous','beautiful','beautifullly','beautifully','beautify','beauty','beckon','beckoned','beckoning','beckons','believable','believeable','beloved','benefactor','beneficent','beneficial','beneficially','beneficiary','benefit','benefits','benevolence','benevolent','benifits','best ','best-known','best-performing','best-selling','better','better-known','better-than-expected','beutifully','blameless','bless','blessing','bliss','blissful','blissfully','blithe','blockbuster','bloom','blossom','bolster','bonny','bonus','bonuses','boom ','booming','boost','boundless','bountiful','brainiest','brainy','brand-new','brave','bravery','bravo','breakthrough','breakthroughs','breathlessness','breathtaking','breathtakingly','breeze','bright','brighten','brighter','brightest','brilliance','brilliances','brilliant','brilliantly','brisk','brotherly','bullish','buoyant','cajole','calm ','calming','calmness','capability','capable','capably','captivate','captivating','carefree','cashback','cashbacks','catchy','celebrate','celebrated','celebration','celebratory','champ','champion','charisma','charismatic','charitable','charm','charming','charmingly','chaste','cheaper','cheapest','cheer','cheerful','cheery','cherish','cherished','cherub','chic ','chivalrous','chivalry','civility','civilize','clarity','classic','classy','clean','cleaner','cleanest','cleanliness','cleanly','clear','clear-cut','cleared','clearer','clearly','clears','clever','cleverly','cohere','coherence','coherent','cohesive','colorful','comely','comfort','comfortable','comfortably','comforting','comfy','commend','commendable','commendably','commitment','commodious','compact','compactly','compassion','compassionate','compatible','competitive','complement','complementary','complemented','complements','compliant','compliment','complimentary','comprehensive','conciliate','conciliatory','concise','confidence','confident','congenial','congratulate','congratulation','congratulations','congratulatory','conscientious','considerate','consistent','consistently','constructive','consummate','contentment','continuity','contrasty','contribution','convenience','convenient','conveniently','convience','convienient','convient','convincing','convincingly','cool ','coolest','cooperative','cooperatively','cornerstone','correct','correctly','cost-effective','cost-saving','counter-attack','counter-attacks','courage','courageous','courageously','courageousness','courteous','courtly','covenant','cozy ','creative','credence','credible','crisp','crisper','cure ','cure-all','cushy','cute ','cuteness','danke','danken','daring','daringly','darling','dashing','dauntless','dawn ','dazzle','dazzled','dazzling','dead-cheap','dead-on','decency','decent','decisive','decisiveness','dedicated','defeat','defeated','defeating','defeats','defender','deference','deft ','deginified','delectable','delicacy','delicate','delicious','delight','delighted','delightful','delightfully','delightfulness','dependable','dependably','deservedly','deserving','desirable','desiring','desirous','destiny','detachable','devout','dexterous','dexterously','dextrous','dignified','dignify','dignity','diligence','diligent','diligently','diplomatic','dirt-cheap','distinction','distinctive','distinguished','diversified','divine','divinely','dominate','dominated','dominates','dote ','dotingly','doubtless','dreamland','dumbfounded','dumbfounding','dummy-proof','durable','dynamic','eager','eagerly','eagerness','earnest','earnestly','earnestness','ease ','eased','eases','easier','easiest','easiness','easing','easy ','easy-to-use','easygoing','ebullience','ebullient','ebulliently','ecenomical','economical','ecstasies','ecstasy','ecstatic','ecstatically','edify','educated','effective','effectively','effectiveness','effectual','efficacious','efficient','efficiently','effortless','effortlessly','effusion','effusive','effusively','effusiveness','elan ','elate','elated','elatedly','elation','electrify','elegance','elegant','elegantly','elevate','elite','eloquence','eloquent','eloquently','embolden','eminence','eminent','empathize','empathy','empower','empowerment','enchant','enchanted','enchanting','enchantingly','encourage','encouragement','encouraging','encouragingly','endear','endearing','endorse','endorsed','endorsement','endorses','endorsing','energetic','energize','energy-efficient','energy-saving','engaging','engrossing','enhance','enhanced','enhancement','enhances','enjoy','enjoyable','enjoyably','enjoyed','enjoying','enjoyment','enjoys','enlighten','enlightenment','enliven','ennoble','enough','enrapt','enrapture','enraptured','enrich','enrichment','enterprising','entertain','entertaining','entertains','enthral','enthrall','enthralled','enthuse','enthusiasm','enthusiast','enthusiastic','enthusiastically','entice','enticed','enticing','enticingly','entranced','entrancing','entrust','enviable','enviably','envious','enviously','enviousness','envy ','equitable','ergonomical','err-free','erudite','ethical','eulogize','euphoria','euphoric','euphorically','evaluative','evenly','eventful','everlasting','evocative','exalt','exaltation','exalted','exaltedly','exalting','exaltingly','examplar','examplary','excallent','exceed','exceeded','exceeding','exceedingly','exceeds','excel','exceled','excelent','excellant','excelled','excellence','excellency','excellent','excellently','excels','exceptional','exceptionally','excite','excited','excitedly','excitedness','excitement','excites','exciting','excitingly','exellent','exemplar','exemplary','exhilarate','exhilarating','exhilaratingly','exhilaration','exonerate','expansive','expeditiously','expertly','exquisite','exquisitely','extol','extoll','extraordinarily','extraordinary','exuberance','exuberant','exuberantly','exult','exultant','exultation','exultingly','eye-catch','eye-catching','eyecatch','eyecatching','fabulous','fabulously','facilitate','fair ','fairly','fairness','faith','faithful','faithfully','faithfulness','fame ','famed','famous','famously','fancier','fancinating','fancy','fanfare','fans ','fantastic','fantastically','fascinate','fascinating','fascinatingly','fascination','fashionable','fashionably','fast ','fast-growing','fast-paced','faster','fastest','fastest-growing','faultless','fav  ','fave ','favor','favorable','favored','favorite','favorited','favour','fearless','fearlessly','feasible','feasibly','feat ','feature-rich','fecilitous','feisty','felicitate','felicitous','felicity','fertile','fervent','fervently','fervid','fervidly','fervor','festive','fidelity','fiery','fine ','fine-looking','finely','finer','finest','firmer','first-class','first-in-class','first-rate','flashy','flatter','flattering','flatteringly','flawless','flawlessly','flexibility','flexible','flourish','flourishing','fluent','flutter','fond ','fondly','fondness','foolproof','foremost','foresight','formidable','fortitude','fortuitous','fortuitously','fortunate','fortunately','fortune','fragrant','free ','freed','freedom','freedoms','fresh','fresher','freshest','friendliness','friendly','frolic','frugal','fruitful','ftw  ','fulfillment','fun  ','futurestic','futuristic','gaiety','gaily','gain ','gained','gainful','gainfully','gaining','gains','gallant','gallantly','galore','geekier','geeky','gem  ','gems ','generosity','generous','generously','genial','genius','gentle','gentlest','genuine','gifted','glad ','gladden','gladly','gladness','glamorous','glee ','gleeful','gleefully','glimmer','glimmering','glisten','glistening','glitter','glitz','glorify','glorious','gloriously','glory','glow ','glowing','glowingly','god-given','god-send','godlike','godsend','gold ','golden','good ','goodly','goodness','goodwill','goood','gooood','gorgeous','gorgeously','grace','graceful','gracefully','gracious','graciously','graciousness','grand','grandeur','grateful','gratefully','gratification','gratified','gratifies','gratify','gratifying','gratifyingly','gratitude','great','greatest','greatness','grin ','groundbreaking','guarantee','guidance','guiltless','gumption','gush ','gusto','gutsy','hail ','halcyon','hale ','hallmark','hallmarks','hallowed','handier','handily','hands-down','handsome','handsomely','handy','happier','happily','happiness','happy','hard-working','hardier','hardy','harmless','harmonious','harmoniously','harmonize','harmony','headway','heal ','healthful','healthy','hearten','heartening','heartfelt','heartily','heartwarming','heaven','heavenly','helped','helpful','helping','hero ','heroic','heroically','heroine','heroize','heros','high-quality','high-spirited','hilarious','holy ','homage','honest','honesty','honor','honorable','honored','honoring','hooray','hopeful','hospitable','hot  ','hotcake','hotcakes','hottest','hug  ','humane','humble','humility','humor','humorous','humorously','humour','humourous','ideal','idealize','ideally','idol ','idolize','idolized','idyllic','illuminate','illuminati','illuminating','illumine','illustrious','ilu  ','imaculate','imaginative','immaculate','immaculately','immense','impartial','impartiality','impartially','impassioned','impeccable','impeccably','important','impress','impressed','impresses','impressive','impressively','impressiveness','improve','improved','improvement','improvements','improves','improving','incredible','incredibly','indebted','individualized','indulgence','indulgent','industrious','inestimable','inestimably','inexpensive','infallibility','infallible','infallibly','influential','ingenious','ingeniously','ingenuity','ingenuous','ingenuously','innocuous','innovation','innovative','inpressed','insightful','insightfully','inspiration','inspirational','inspire','inspiring','instantly','instructive','instrumental','integral','integrated','intelligence','intelligent','intelligible','interesting','interests','intimacy','intimate','intricate','intrigue','intriguing','intriguingly','intuitive','invaluable','invaluablely','inventive','invigorate','invigorating','invincibility','invincible','inviolable','inviolate','invulnerable','irreplaceable','irreproachable','irresistible','irresistibly','issue-free','jaw-droping','jaw-dropping','jollify','jolly','jovial','joy  ','joyful','joyfully','joyous','joyously','jubilant','jubilantly','jubilate','jubilation','jubiliant','judicious','justly','keen ','keenly','keenness','kid-friendly','kindliness','kindly','kindness','knowledgeable','kudos','large-capacity','laud ','laudable','laudably','lavish','lavishly','law-abiding','lawful','lawfully','lead ','leading','leads','lean ','led  ','legendary','leverage','levity','liberate','liberation','liberty','lifesaver','light-hearted','lighter','likable','like ','liked','likes','liking','lionhearted','lively','logical','long-lasting','lovable','lovably','love ','loved','loveliness','lovely','lover','loves','loving','low-cost','low-price','low-priced','low-risk','lower-priced','loyal','loyalty','lucid','lucidly','luck ','luckier','luckiest','luckiness','lucky','lucrative','luminous','lush ','luster','lustrous','luxuriant','luxuriate','luxurious','luxuriously','luxury','lyrical','magic','magical','magnanimous','magnanimously','magnificence','magnificent','magnificently','majestic','majesty','manageable','maneuverable','marvel','marveled','marvelled','marvellous','marvelous','marvelously','marvelousness','marvels','master','masterful','masterfully','masterpiece','masterpieces','masters','mastery','matchless','mature','maturely','maturity','meaningful','memorable','merciful','mercifully','mercy','merit','meritorious','merrily','merriment','merriness','merry','mesmerize','mesmerized','mesmerizes','mesmerizing','mesmerizingly','meticulous','meticulously','mightily','mighty','mind-blowing','miracle','miracles','miraculous','miraculously','miraculousness','modern','modest','modesty','momentous','monumental','monumentally','morality','motivated','multi-purpose','navigable','neat ','neatest','neatly','nice ','nicely','nicer','nicest','nifty','nimble','noble','nobly','noiseless','non-violence','non-violent','notably','noteworthy','nourish','nourishing','nourishment','novelty','nurturing','oasis','obsession','obsessions','obtainable','openly','openness','optimal','optimism','optimistic','opulent','orderly','originality','outdo','outdone','outperform','outperformed','outperforming','outperforms','outshine','outshone','outsmart','outstanding','outstandingly','outstrip','outwit','ovation','overjoyed','overtake','overtaken','overtakes','overtaking','overtook','overture','pain-free','painless','painlessly','palatial','pamper','pampered','pamperedly','pamperedness','pampers','panoramic','paradise','paramount','pardon','passion','passionate','passionately','patience','patient','patiently','patriot','patriotic','peace','peaceable','peaceful','peacefully','peacekeepers','peach','peerless','pep  ','pepped','pepping','peppy','peps ','perfect','perfection','perfectly','permissible','perseverance','persevere','personages','personalized','phenomenal','phenomenally','picturesque','piety','pinnacle','playful','playfully','pleasant','pleasantly','pleased','pleases','pleasing','pleasingly','pleasurable','pleasurably','pleasure','plentiful','pluses','plush','plusses','poetic','poeticize','poignant','poise','poised','polished','polite','politeness','popular','portable','posh ','positive','positively','positives','powerful','powerfully','praise','praiseworthy','praising','pre-eminent','precious','precise','precisely','preeminent','prefer','preferable','preferably','prefered','preferes','preferring','prefers','premier','prestige','prestigious','prettily','pretty','priceless','pride','principled','privilege','privileged','prize','proactive','problem-free','problem-solver','prodigious','prodigiously','prodigy','productive','productively','proficient','proficiently','profound','profoundly','profuse','profusion','progress','progressive','prolific','prominence','prominent','promise','promised','promises','promising','promoter','prompt','promptly','proper','properly','propitious','propitiously','pros ','prosper','prosperity','prosperous','prospros','protect','protection','protective','proud','proven','proves','providence','proving','prowess','prudence','prudent','prudently','punctual','pure ','purify','purposeful','quaint','qualified','qualify','quicker','quiet','quieter','radiance','radiant','rapid','rapport','rapt ','rapture','raptureous','raptureously','rapturous','rapturously','rational','razor-sharp','reachable','readable','readily','ready','reaffirm','reaffirmation','realistic','realizable','reasonable','reasonably','reasoned','reassurance','reassure','receptive','reclaim','recomend','recommend','recommendation','recommendations','recommended','reconcile','reconciliation','record-setting','recover','recovery','rectification','rectify','rectifying','redeem','redeeming','redemption','refine','refined','refinement','reform','reformed','reforming','reforms','refresh','refreshed','refreshing','refund','refunded','regal','regally','regard','rejoice','rejoicing','rejoicingly','rejuvenate','rejuvenated','rejuvenating','relaxed','relent','reliable','reliably','relief','relish','remarkable','remarkably','remedy','remission','remunerate','renaissance','renewed','renown','renowned','replaceable','reputable','reputation','resilient','resolute','resound','resounding','resourceful','resourcefulness','respect','respectable','respectful','respectfully','respite','resplendent','responsibly','responsive','restful','restored','restructure','restructured','restructuring','retractable','revel','revelation','revere','reverence','reverent','reverently','revitalize','revival','revive','revives','revolutionary','revolutionize','revolutionized','revolutionizes','reward','rewarding','rewardingly','rich ','richer','richly','richness','right','righten','righteous','righteously','righteousness','rightful','rightfully','rightly','rightness','risk-free','robust','rock-star','rock-stars','rockstar','rockstars','romantic','romantically','romanticize','roomier','roomy','rosy ','safe ','safely','sagacity','sagely','saint','saintliness','saintly','salutary','salute','sane ','satisfactorily','satisfactory','satisfied','satisfies','satisfy','satisfying','satisified','saver','savings','savior','savvy','scenic','seamless','seasoned','secure','securely','selective','self-determination','self-respect','self-satisfaction','self-sufficiency','self-sufficient','sensation','sensational','sensationally','sensations','sensible','sensibly','sensitive','serene','serenity','sexy ','sharp','sharper','sharpest','shimmering','shimmeringly','shine','shiny','significant','silent','simpler','simplest','simplified','simplifies','simplify','simplifying','sincere','sincerely','sincerity','skill','skilled','skillful','skillfully','slammin','sleek','slick','smart','smarter','smartest','smartly','smile','smiles','smiling','smilingly','smitten','smooth','smoother','smoothes','smoothest','smoothly','snappy','snazzy','sociable','soft ','softer','solace','solicitous','solicitously','solid','solidarity','soothe','soothingly','sophisticated','soulful','soundly','soundness','spacious','sparkle','sparkling','spectacular','spectacularly','speedily','speedy','spellbind','spellbinding','spellbindingly','spellbound','spirited','spiritual','splendid','splendidly','splendor','spontaneous','sporty','spotless','sprightly','stability','stabilize','stable','stainless','standout','state-of-the-art','stately','statuesque','staunch','staunchly','staunchness','steadfast','steadfastly','steadfastness','steadiest','steadiness','steady','stellar','stellarly','stimulate','stimulates','stimulating','stimulative','stirringly','straighten','straightforward','streamlined','striking','strikingly','striving','strong','stronger','strongest','stunned','stunning','stunningly','stupendous','stupendously','sturdier','sturdy','stylish','stylishly','stylized','suave','suavely','sublime','subsidize','subsidized','subsidizes','subsidizing','substantive','succeed','succeeded','succeeding','succeeds','succes','success','successes','successful','successfully','suffice','sufficed','suffices','sufficient','sufficiently','suitable','sumptuous','sumptuously','sumptuousness','super','superb','superbly','superior','superiority','supple','support','supported','supporter','supporting','supportive','supports','supremacy','supreme','supremely','supurb','supurbly','surmount','surpass','surreal','survival','survivor','sustainability','sustainable','swank','swankier','swankiest','swanky','sweeping','sweet','sweeten','sweetheart','sweetly','sweetness','swift','swiftness','talent','talented','talents','tantalize','tantalizing','tantalizingly','tempt','tempting','temptingly','tenacious','tenaciously','tenacity','tender','tenderly','terrific','terrifically','thank','thankful','thinner','thoughtful','thoughtfully','thoughtfulness','thrift','thrifty','thrill','thrilled','thrilling','thrillingly','thrills','thrive','thriving','thumb-up','thumbs-up','tickle','tidy ','time-honored','timely','tingle','titillate','titillating','titillatingly','togetherness','tolerable','toll-free','top  ','top-notch','top-quality','topnotch','tops ','tough','tougher','toughest','traction','tranquil','tranquility','transparent','treasure','tremendously','trendy','triumph','triumphal','triumphant','triumphantly','trivially','trophy','trouble-free','trump','trumpet','trust','trusted','trusting','trustingly','trustworthiness','trustworthy','trusty','truthful','truthfully','truthfulness','twinkly','ultra-crisp','unabashed','unabashedly','unaffected','unassailable','unbeatable','unbiased','unbound','uncomplicated','unconditional','undamaged','undaunted','understandable','undisputable','undisputably','undisputed','unencumbered','unequivocal','unequivocally','unfazed','unfettered','unforgettable','unity','unlimited','unmatched','unparalleled','unquestionable','unquestionably','unreal','unrestricted','unrivaled','unselfish','unwavering','upbeat','upgradable','upgradeable','upgraded','upheld','uphold','uplift','uplifting','upliftingly','upliftment','upscale','usable','useable','useful','user-friendly','user-replaceable','valiant','valiantly','valor','valuable','variety','venerate','verifiable','veritable','versatile','versatility','vibrant','vibrantly','victorious','victory','viewable','vigilance','vigilant','virtue','virtuous','virtuously','visionary','vivacious','vivid','vouch','vouchsafe','warm ','warmer','warmhearted','warmly','warmth','wealthy','welcome','well ','well-backlit','well-balanced','well-behaved','well-being','well-bred','well-connected','well-educated','well-established','well-informed','well-intentioned','well-known','well-made','well-managed','well-mannered','well-positioned','well-received','well-regarded','well-rounded','well-run','well-wishers','wellbeing','whoa ','wholeheartedly','wholesome','whooa','whoooa','wieldy','willing','willingly','willingness','win  ','windfall','winnable','winner','winners','winning','wins ','wisdom','wise ','wisely','witty','won  ','wonder','wonderful','wonderfully','wonderous','wonderously','wonders','wondrous','woo  ','work ','workable','worked','works','world-famous','worth','worth-while','worthiness','worthwhile','worthy','wow  ','wowed','wowing','wows ','yay  ','youthful','zeal ','zenith','zest ','zippy']
file = open("d:\data\겨울왕국_대본.txt",'r')
sum=0
for winter_list in file:
    words = winter_list.split(' ')
    for word in words:
        if word in positive:
            sum = sum+1
print(sum)