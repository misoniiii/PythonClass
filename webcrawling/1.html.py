#ex268) beautiful soup 모듈을 이용해서 위의 html 문서의 title을 검색하시오
from bs4 import BeautifulSoup
with open("/Users/misoni/Desktop/pythondata/a.html") as ex:
    soup = BeautifulSoup(ex , 'lxml') #Beautifulsoup클래스의 매개변수를 두개 사용하고 soup을 인스턴스화함
print('title', soup.title.get_text())


#Ex270)a.html문서에서 a태그에 대한 html을 검색하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/a.html") as ex:
    soup = BeautifulSoup(ex,'lxml') #Beautifulsoup클래스의 매개변수를 두개 사용하고 soup을 인스턴스화함
print('soup.find_all',soup.find_all('a')) #a태그의 모든 요소 가져옴
print('soup.find',soup.find('a'))   #첫번째 요소만 가져옴
print('soup.a',soup.a)              #첫번째 요소만 가져옴

#ex272) a.html문서에서 href링크의 url만 긁어오시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/a.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
    for link in soup.find_all('a'):
        print(link)
        print(link.get('href'))

#ex273) b.html문서에서 html소스말고 text만 출력하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/b.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
print(soup.get_text())

#ex274)위의 텍스트를 한줄로 나오게 하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/b.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
print(soup.get_text(strip=True))

#ex275)카페에서 ecologicalpyramid.html 문서를 다운받아 열어보시오
#ex276) html코드를 treemap으로 확인할 수 있는 방법을 구현하시오 ecologicalpyramid.html문서를 tree map으로 구현하시오
#ex277) ecologicalpyramid.html문서에서 text 100000을 출력하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find(class_="number")
print(result)               #<div class="number">100000</div>
print(result.get_text())    #100000

#ex278) ecologicalpyramid.html문서에 number클래스에 있는 모든 텍스트를 다 가져오시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find_all(class_="number")
for link in result:
    print(link.get_text())

#>>>
#  100000
# 100000
# 1000
# 2000
# 100
# 100
# 80
# 50

#ex279) 위의 결과에서 아래의 1000만 출력하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find_all(class_="number")[2] #오홍 여기다가도 붙일 수 있구만 신기
print(result.get_text())

#ex280) ecologicalpyramid.html에서 fox를 출력하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find_all(class_="name")[4] #오홍 여기다가도 붙일 수 있구만 신기
print(result.get_text())


from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find_all("ul")[2]
print(result.li.div.string)

#ex282) ecologicalpyramid.html문서안에 있는 fox 텍스트가 있는지 검색
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find(text = 'fox')
print(result)

#ex283) id="primaryconsumers로 조회해서 deer를 검색하시오
from bs4 import BeautifulSoup

with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find(id = 'primaryconsumers')
print(result.li.div.string)

#ex284) deer아래 있는 1000을 출력되게 하시오
from bs4 import BeautifulSoup
with open("/Users/misoni/Desktop/pythondata/ecologicalpyramid.html") as ex:
    soup = BeautifulSoup(ex,'lxml')
result = soup.find_all('div',class_='number')[2]
print(result.string)

##참고예제
div_li_tags = soup.find_all(["div","li"])
all_css_class = soup.find_all( class_ = ["producerlist","primaryconsumerlist"])


#ex285)레이디버그 게시판 스크롤링
import urllib.request
from bs4 import BeautifulSoup
import re
import os


def fetch_list_url():
  list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
  url = urllib.request.Request(list_url) # url을 파이썬이 인식할 수 있는 코드로 바꿔줌 >>> <urllib.request.Request object at 0x1052e2860>
  print(url)
  res = urllib.request.urlopen(url).read().decode("utf-8") # url을 utf-8로 코딩
  print(res) #위의 두가지 작업을 거치면 위의 url의 html문서를 res변수에 담을 수 있음
  soup = BeautifulSoup(res, "html.parser") #res에 담긴 html코드를 Beautifulsoup모듈로 검색하기 위한 작업
# 위의 ebs 게시판 url 로 접속했을때 담긴 html 코드를
# soup 에 담겠다
  #e_reg = re.compile("(완젼)") #완젼이라는 텏트를 검색하기 위해 완젼이라는 한글을 컴파일
  #a  =  soup.find(text=e_reg)
  a = soup.find(text='p')
fetch_list_url()

#ex285) ebs레이디 버그 시청자 게시판 페이지에서 dd태그의 type2클래스에 있는 href 링크 주소들을 전부 스크롤링 하시오
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url():
  list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
  url = urllib.request.Request(list_url)
  res = urllib.request.urlopen(url).read().decode("utf-8")
  soup = BeautifulSoup(res, "html.parser")
  for link in soup.find_all('a'):
      print(link.get("href"))

fetch_list_url()

#ex286) 현재 페이지의 게시판 13개의 게시글이 전부 출력되게 하시오
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url():
  list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
  url = urllib.request.Request(list_url)
  res = urllib.request.urlopen(url).read().decode("utf-8")
  soup = BeautifulSoup(res, "html.parser")
  contents = soup.find_all('p', class_ = 'con')
  for link in contents:
      print(link.get_text(strip=True))

fetch_list_url()


#ex287)게시글 뿐만 아니라 게시 날짜 정보도 함께 출력되게 하시오
###경원오빠 코드####
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    a = soup.find_all('p',class_="con")
    b = soup.find_all('span',class_="date")
    cnt= 0
    for i in a:
        print(b[cnt].text,i.get_text(strip=True))
        cnt += 1

fetch_list_url()

##############혜승이
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    a = soup.find_all(['p','span'], class_=["con","date"])
    for i in a:
        print(i.get_text(strip=True))

fetch_list_url()


#######################################
#ex288)문제 287코드에 for loop를 추가해서 ebs레이디 버그 게시판글을 모두 스크롤링 하시오
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url():
    for i in range(1,16):
        list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(i)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
        url = urllib.request.Request(list_url)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup= BeautifulSoup(res, "html.parser")
        a = soup.find_all('p',class_="con")
        b = soup.find_all('span',class_="date")
        cnt= 0
        for i in a:
            print(b[cnt].text, i.get_text(strip=True))
            cnt += 1

fetch_list_url()