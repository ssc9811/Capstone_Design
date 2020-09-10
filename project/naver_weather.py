import requests
from bs4 import BeautifulSoup

def creat_soup(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "lxml")
    return soup

def naver_weather():
    URL = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    soup = creat_soup(URL)
    todaytemp = soup.find("span",{"class":"todaytemp"}).get_text()
    min_temp = soup.find("span",{"class":"min"}).get_text()
    max_temp = soup.find("span",{"class":"max"}).get_text()
    print(f"현재 날씨 : {todaytemp}  ({min_temp}/{max_temp})")
    print("")
