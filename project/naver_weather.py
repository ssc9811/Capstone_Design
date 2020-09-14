import requests
from bs4 import BeautifulSoup

def creat_soup(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "lxml")
    return soup

def naver_weather():
    URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%96%91%EC%8B%9C+%EB%A7%8C%EC%95%88%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EA%B8%B0%EC%83%81%EC%B2%AD&tqi=U1JXRsp0YidssKrc73NssssstiV-040794"
    soup = creat_soup(URL)
    todaytemp = soup.find("span",{"class":"todaytemp"}).get_text()
    min_temp = soup.find("span",{"class":"min"}).get_text()
    max_temp = soup.find("span",{"class":"max"}).get_text()
    print(f"현재 날씨 : {todaytemp}  ({min_temp}/{max_temp})")
    print("")
