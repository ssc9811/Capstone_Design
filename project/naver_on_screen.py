import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def on_screen():
    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    url = ("https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve")
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "lxml")
    movie = soup.find("ul",class_="lst_detail_t1")
    lis = movie.findAll("li")
    on_s_rank = []
    
    for idx, li in enumerate(lis):
        try:
            title = li.find("dt", class_="tit").find("a").get_text()
            link = li.find("dt", class_="tit").find("a")["href"]
            rate = li.find("div", class_="star_t1").find("span",class_="num").get_text()
            ticket = li.find("div", class_="star_t1 b_star").find("span",class_="num").get_text()
            result = {'title' : title, 'link' : f"https://movie.naver.com/{link}", 'rate' : rate, 'ticket' : ticket}
            on_s_rank.append(result)  
        except AttributeError as e:
            continue
    return on_s_rank


on_screen()

