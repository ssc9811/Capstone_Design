import requests
from bs4 import BeautifulSoup 

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}


def creat_soup(SEARCH): #이 함수를 통합할수는 없을까?
    URL = f"https://news.google.com/search?q={SEARCH}&hl=ko&gl=KR&ceid=KR%3Ako" 
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    return soup

def headline_news():
    URL = "https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "lxml")
    news = soup.find_all("div",{"class":"NiLAwe"})
    head_news = []
    for idx, new in enumerate(news):
        title = new.find("h3",{"class":"ipQwMb"}).get_text()
        link = new.find("a",{"class":"VDXfz"})["href"]
        search = {'idx' : idx+1, 'title' : title, 'link' : f"https://news.google.com/{link}"}
        head_news.append(search)
    return head_news
        

def extract_news(new):
    title = new.find("h3",{"class":"ipQwMb"}).get_text()
    link = new.find("a",{"class":"VDXfz"})["href"]
    return {'title' : title, 'link' : f"https://news.google.com/{link}"} # web에 출력하기 위해선 딕셔너리 형태로 리턴해야함.

def search_news(SEARCH):
    get_news = []
    soup = creat_soup(SEARCH)
    news = soup.find_all("div",{"class":"NiLAwe"}, limit=5)
    for new in news:
        search = extract_news(new)
        get_news.append(search)
    return get_news
        


