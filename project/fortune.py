from selenium import webdriver
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True

browser = webdriver.Chrome(options=options)
browser.maximize_window()

URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B3%84%EC%9E%90%EB%A6%AC+%EC%9A%B4%EC%84%B8&oquery=%EC%9A%B4%EC%83%88%E3%85%94&tqi=U22U9wprvOsssKW7lRKssssssnV-054440"
browser.get(URL)

a = ["물병자리",'물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','사수자리','염소자리']

def search_fortune():
    soup = BeautifulSoup(browser.page_source, "lxml")
    fortune = soup.find("p",{"class":"text _cs_fortune_text"}).get_text()
    return fortune

def extract_fortune(idx):
    browser.find_element_by_link_text("물병자리").click()
    # browser.find_element_by_link_text(a[idx]).click()
    result = search_fortune()
    return result
