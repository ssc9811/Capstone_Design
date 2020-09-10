import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}


def creat_soup(SEARCH):
    URL = f"https://news.google.com/search?q={SEARCH}&hl=ko&gl=KR&ceid=KR%3Ako"
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    return soup

def search_news(SEARCH):
    soup = creat_soup(SEARCH)
    news = soup.find_all("div",{"class":"NiLAwe"})
    for new in news:
        title = new.find("h3",{"class":"ipQwMb"}).get_text()
        link = new.find("a",{"class":"VDXfz"})["href"]

        print(f"제목 : {title}   링크 : https://news.google.com/{link}")

