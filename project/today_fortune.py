import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()

URL = "https://fortune.nate.com/contents/freeunse/freeunseframe.nate?freeUnseId=today03"
browser.get(URL)

browser.find_element_by_xpath("//*[@id='tee']/tbody/tr/td[3]/a/img").click()

browser.quit()