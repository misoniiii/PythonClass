import urllib.request
from  bs4  import  BeautifulSoup
from selenium import webdriver #웹 어플리케이션의 테스트를 자동화하기 위한 프레임 워
from selenium.webdriver.common.keys import Keys
import time #중간 중간 sleep을 걸어야해서 time모듈을 import한다.

binary = 'D:\chromedriver/chromedriver.exe' #크롬 드라이버를 다운 받아 위의 위치에 둔다
                                            #팬텀 js로 하면 백그라운드 실행가능
browser = webdriver.Chrome(binary)          #브라우저를 인스턴스화
browser.get("https://search.naver.com/search.naver?where=image&amp;sm=stb_nmr&amp;")    #네이버의 이미지 검색 url을 받아옴
elem = browser.find_element_by_id("nx_query")   #네이버의 이미지 검색에 해당하는 input창의 id가 nx_query여서 검색창에 해당하는 html코드를 찾아서 elem으로 설정
#find_elements_by_class_name("")                #클래스 이름 찾을 때 방

# 검색어 입력
elem.send_keys("아이언맨")  #elem이 input창과 연결되어 스스로 아이언맨을 입력
elem.submit()   #웹에서 submit은 엔터

# 반복할 횟수
for i in range(1,2):
    browser.find_element_by_xpath("//body").send_keys(Keys.END) #브라우저 아무 곳에서나 end키를 누른다고 해서 페이지가 아래로 내려가지 않음
                                                                #body를 활성화해놓고 end키를 누름    time.sleep(5)

time.sleep(5)   #네트웍이 느릴까봐 안정성을 위해 5초의 sleep을 줌
html = browser.page_source  #크롬 브라우저에서 현재 불러온 소스를 가져옴
soup = BeautifulSoup(html,"lxml")   # beautiful soup을 사용해서 html코드 검색할 수 있도록 설정
#print(soup)
#print(len(soup))

def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="_img")   #네이버 이미지 url이 있는 img태그의 _img클래스로 감
    for im in imgList:
        params.append(im["src"])                    #params리스트 변수에 image url을 담는다
    return params


def  fetch_detail_url():
    params = fetch_list_url()
    #print(params)
    a = 1
    for p in params:
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "d:/naverImages/"+ str(a) + ".jpg" )

        a = a + 1

fetch_detail_url()

browser.quit()