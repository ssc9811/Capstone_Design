import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = ("https://phrase.dict.naver.com/?targetLanguage=en")
browser.get(url)

browser.implicitly_wait(5)
def en_con():
    soup = BeautifulSoup(browser.page_source, "lxml")
    section = soup.find("div",{"class":"section_cen"})
    lis = section.findAll('li')
    r_con = []
    for li in lis:
        try:
            con1 = str(li.find("span", class_=("info_txt")).get_text())
            con1 = re.sub('\t|\r|\n','',con1,0).strip() #한글

            con1_2 = str(li.find("span", class_=("info_txt2")).get_text())
            con1_2 = re.sub('\t|\r|\n','',con1_2,0).strip() #영어
            result = {'kor':con1, 'eng':con1_2}
            r_con.append(result)
        except AttributeError as e:
            continue
    return r_con
browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[4]/a[2]').click()
e1= en_con()
browser.find_element_by_xpath('//*[@id="main_content"]/ul/li[2]').click()
browser.find_element_by_xpath('//*[@id="main_content"]/ul/li[3]').click()
e2 = en_con()
e3 = en_con()

def r1():
    return e1
def r2():
    return e2
def r3():
    return e3    

browser.quit()