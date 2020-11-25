import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

aa = ["물병자리",'물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','사수자리','염소자리']

fortune = []

def search_fortune():
    for i in range(0,12):
        url = (f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={aa[i]}+운세")
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        fortune.append(soup.find("p",{"class":"text _cs_fortune_text"}).get_text())
    return fortune


def extract_fortune(value):
    # print(f"포츈에서 value type 값 : {type(value)}")
    return fortune[int(value)]

search_fortune()