# import urllib.request
# from  bs4 import BeautifulSoup
#
# def fetch_list_url():
#     for page in range(20):
#         list_url = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq="+str(page)
#         url = urllib.request.Request(list_url)
#         res = urllib.request.urlopen(url).read().decode("utf-8")
#         soup = BeautifulSoup(res, "html.parser")
#         params = []
#         for i in range(20):
#             try:
#                 soup2 = soup.find_all('dt')[i]
#                 soup3 = soup2.find('a')['href']
#                 params.append(soup3)
#             except Exception:   #비어있는 요소 <dt></dt>인 애들은 오류가 남
#                  continue       #pass써도 됨
#         print(params)
#     return params
#
# fetch_list_url()
#
# import urllib.request
# from  bs4 import BeautifulSoup
# def fetch_list_url2():
#     list_url = "http://www.hani.co.kr/arti/economy/it/794467.html"
#     url = urllib.request.Request(list_url)
#     res = urllib.request.urlopen(url).read().decode("utf-8")
#     soup = BeautifulSoup(res, "html.parser")
#     soup2 = soup.find_all('div',class_='text')
#     for text in soup2:
#         print(text.get_text())
# fetch_list_url2()
#
# #<class 'bs4.element.Tag'> <---tag여야 get_text()를 사용할 수 있다
# #<class 'bs4.element.Tag'>
#
# #ex300) fetch_list_url() 함수가 리턴하는 params의 url값들을 fetch_list_url2()함수에서 호출해오시오
# ###ex299)복붙
# import urllib.request
# from  bs4 import BeautifulSoup
#
# def fetch_list_url():
#     params = []
#     for page in range(20):
#         list_url = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq="+str(page)
#         url = urllib.request.Request(list_url)
#         res = urllib.request.urlopen(url).read().decode("utf-8")
#         soup = BeautifulSoup(res, "html.parser")
#         for i in range(20):
#             try:
#                 soup2 = soup.find_all('dt')[i]
#                 soup3 = soup2.find('a')['href']
#                 params.append(soup3)
#             except Exception:   #비어있는 요소 <dt></dt>인 애들은 오류가 남
#                  continue       #pass써도 됨
#     return params
#
# def fetch_list_url2():
#     params2 = fetch_list_url()
#     print(params2)
#
#
# fetch_list_url2()
#
#
# #ex301) 위의 스크립트에 for loop문을 살짝 사용해서 상세 기사 전체가 출력되게 하시오
# import urllib.request
# from  bs4 import BeautifulSoup
#
# def fetch_list_url():
#     params = []
#     for page in range(20):
#         list_url = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq="+str(page)
#         url = urllib.request.Request(list_url)
#         res = urllib.request.urlopen(url).read().decode("utf-8")
#         soup = BeautifulSoup(res, "html.parser")
#         for i in range(20):
#             try:
#                 soup2 = soup.find_all('dt')[i]
#                 soup3 = soup2.find('a')['href']
#                 params.append(soup3)
#             except Exception:   #비어있는 요소 <dt></dt>인 애들은 오류가 남
#                  continue       #pass써도 됨
#     return params
#
# def fetch_list_url2():
#     params2 = fetch_list_url()
#     for i in params2:
#         list_url2 = i
#         url2 = urllib.request.Request(list_url2)
#         res2 = urllib.request.urlopen(url2).read().decode("utf-8")
#         soup = BeautifulSoup(res2, "html.parser")
#
#         soup2 = soup.find_all('div',class_='article-text')[0]
#         #print(soup2)
#         print(soup2.get_text(strip=True))
#
#         # for text in soup2:
#         #     print(text.get_text(strip=True)) #<class 'bs4.element.Tag'>
#         #     print(type(text.get_text(strip=True)))
# fetch_list_url2()
#
#
# #ex302) 인공지능 검색한 한겨례 신문사 기사 전체를 data7이라는 폴더에 생성되게 하시
# import urllib.request
# from  bs4 import BeautifulSoup
# import os
#
# def get_save_path():
#     save_path = input("Enter the file name and file location :" )
#     save_path = save_path.replace("\\", "/")
#     if not os.path.isdir(os.path.split(save_path)[0]): #폴더가 없으면 만드는 작업
#         os.mkdir(os.path.split(save_path)[0])
#     return save_path
#
# def fetch_list_url():
#     params = []
#     for page in range(20):
#         list_url = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq="+str(page)
#         url = urllib.request.Request(list_url)
#         res = urllib.request.urlopen(url).read().decode("utf-8")
#         soup = BeautifulSoup(res, "html.parser")
#         for i in range(20):
#             try:
#                 soup2 = soup.find_all('dt')[i]
#                 soup3 = soup2.find('a')['href']
#                 params.append(soup3)
#             except Exception:   #비어있는 요소 <dt></dt>인 애들은 오류가 남
#                  continue       #pass써도 됨
#     return params
#
# def fetch_list_url2():
#     params2 = fetch_list_url()
#     f = open(get_save_path(),'w',encoding='utf-8')
#     for i in params2:
#         list_url2 = i
#         url2 = urllib.request.Request(list_url2)
#         res2 = urllib.request.urlopen(url2).read().decode("utf-8")
#         soup = BeautifulSoup(res2, "html.parser")
#
#         soup2 = soup.find_all('div',class_='article-text')[0]
#         result3 = soup2.get_text(strip=True,separator ='\n')
#         f.write(result3+'\n')
#     f.close()
#
# fetch_list_url2()

#/Users/misoni/Desktop/pythondata/data7/jungang_AI.txt

#ex303) 중앙일보에서 인공지능으로 검색한 기사를 모두 스크롤링하시


import urllib.request
from  bs4 import BeautifulSoup
import os

def get_save_path():
    save_path = input("Enter the file name and file location :" )
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]):
        os.mkdir(os.path.split(save_path)[0])
    return save_path


def fetch_list_url():
    params = []
    for page in range(20):
        list_url = "http://search.joins.com/JoongangNews?page="+str(page)+"&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews&MatchKeyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5"
        url = urllib.request.Request(list_url)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser")
        for i in range(20):
            try:
                soup2 = soup.find_all('span',class_='thumb')[i]
                soup3 = soup2.find('a')['href']
                params.append(soup3)
            except Exception:
                 continue
    return params


def fetch_list_url2():
    params2 = fetch_list_url()
    f = open(get_save_path(),'w',encoding='utf-8')
    for i in params2:
        list_url2 = i
        url2 = urllib.request.Request(list_url2)
        res2 = urllib.request.urlopen(url2).read().decode("utf-8")
        soup = BeautifulSoup(res2, "html.parser")

        #soup2 = soup.find_all(id='article_body')
        #print('soup2',soup2) (id= article_body인 기사 코드 포함되서 다 나옴)
        # for content in soup2:
        #     result3 = content.get_text(strip=True)
        #     print(result3)
        #     f.write(result3+'\n')

        soup2 = soup.find_all('div',id="article_body")[0]
        result3 = soup2.get_text(strip=True, separator='\n')
        f.write(result3+'\n')
    f.close()

fetch_list_url2()