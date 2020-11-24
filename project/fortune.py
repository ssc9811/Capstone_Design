# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import requests
# from bs4 import BeautifulSoup

# options = webdriver.ChromeOptions()
# options.headless = True

# browser = webdriver.Chrome(options=options)
# browser.maximize_window()

# URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B3%84%EC%9E%90%EB%A6%AC+%EC%9A%B4%EC%84%B8&oquery=%EC%9A%B4%EC%83%88%E3%85%94&tqi=U22U9wprvOsssKW7lRKssssssnV-054440"
# browser.get(URL)

# # aa = ["물병자리",'물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','사수자리','염소자리']

# def search_fortune():
#     soup = BeautifulSoup(browser.page_source, "lxml")
#     fortune = soup.find("p",{"class":"text _cs_fortune_text"}).get_text()
#     return fortune

# fortune = []

# browser.find_element_by_link_text("물병자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("물병자리").click()
# browser.find_element_by_link_text("물고기자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("물고기자리").click()
# browser.find_element_by_link_text("양자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("양자리").click()
# browser.find_element_by_link_text("황소자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("황소자리").click()
# browser.find_element_by_link_text("쌍둥이자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("쌍둥이자리").click()
# browser.find_element_by_link_text("게자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("게자리").click()
# browser.find_element_by_link_text("사자자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("사자자리").click()
# browser.find_element_by_link_text("처녀자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("처녀자리").click()
# browser.find_element_by_link_text("천칭자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("천칭자리").click()
# browser.find_element_by_link_text("전갈자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("전갈자리").click()
# browser.find_element_by_link_text("사수자리").click()
# fortune.append(search_fortune())
# browser.find_element_by_link_text("사수자리").click()
# browser.find_element_by_link_text("염소자리").click()
# fortune.append(search_fortune())

# def extract_fortune(value):
#     # print(f"포츈에서 value type 값 : {type(value)}")
#     return fortune[int(value)]


# # def extract_fortune(value):
# #     try:
# #         WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, fortune[int(value)]))).click()
# #         result = search_fortune()
# #         return result
# #     finally:
# #         browser.quit()
    
# # print(extract_fortune(idx))
# browser.quit()
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