import urllib.request
from bs4 import BeautifulSoup
import os
import re

def get_save_path():
    save_path = input('Enter the file name and file location')
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]): #폴더가 없으면 만드는 작업
        os.mkdir(os.path.split(save_path)[0])
    return save_path

def fetch_list_url():
    params=[]
    for j in range(10):
        list_url = 'http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp'
        request_header = urllib.parse.urlencode({"page":j}) #print(request_header) # >>> page1, page2.....

        request_header = request_header.encode('utf-8')  #print(request_header) #>>>b'page=1' #밑 번호를 눌러도 url번호가 안 바뀌어서 url을 요청해야함
        url = urllib.request.Request(list_url, request_header)  # 페이지 번호도 줘야함 #print(url) # >> <urllib.request.Request object at 0x100775160>... 유니크한 메모리 주소 정보
        res = urllib.request.urlopen(url).read().decode('utf-8') #웹서비스에서 url을 받아서 html이 나옴
        soup = BeautifulSoup(res,"html.parser")
        try:
            for i in range(100):
                soup2 = soup.find_all('li',class_='pclist_list_tit2')[i]
            # print(soup2)
            # <li class="pclist_list_tit2" style="text-align:left;">
            # <a href="JavaScript:onView ('20170504000603')" title="주택가 무속인 미취학 아동 보호 "> 주택가 무속인 미취학 아동 보호 </a>
            # </li>,  .... 지정된 조건인 애들이 쫙 나옴 ( 해당 페이지에서 게시글 제목들)
                soup3 = soup2.find('a')['href']
                params.append(re.search( "[0-9]{14}",soup3 ).group())
        except Exception:
            continue
    #print(params)
    return(params)
#fetch_list_url()


def fetch_list_url2():
    params = fetch_list_url()
    f = open(get_save_path(),'w',encoding='utf-8')
    for param in params:
        detail_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"
        request_header = urllib.parse.urlencode( { "RCEPT_NO": str(param) })
        request_header = request_header.encode('utf-8')

        url = urllib.request.Request(detail_url,request_header)
        res = urllib.request.urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(res, 'html.parser')
        soup2 = soup.find('div',class_="form_table")

        tables = soup2.find_all('table')

        table0 = tables[0].find_all('td')
        table1 = tables[1].find_all('div',class_='table_inner_desc')
        table2 = tables[2].find_all('div', class_='table_inner_desc')

        title =table0[0].get_text()
        date = table0[1].get_text()
        question = table1[0].get_text(strip=True)
        answer = table2[0].get_text(strip=True)

        # print('title',title)
        # print('date',date)
        # print('question',question)
        # print('answer',answer)

        #f.write("=="*30 + '\n')
        f.write(title+'\n')
        f.write(question +'\n')
        f.write(answer +'\n')
        #f.write("=="*30 + '\n')

    f.close()
fetch_list_url2()

