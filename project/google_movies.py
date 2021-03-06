from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument("window-size = 1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

URL = "https://play.google.com/store/movies/top"
browser.get(URL)

def google_movies():
    soup = BeautifulSoup(browser.page_source, "lxml")
    movie = soup.find_all("div",{"class":"Vpfmgd"})
    movie_rank = []
    google_movies_scroll_down()
    for idx, movies in enumerate(movie):
        title = movies.find("div",{"class":"WsMG1c nnK0zc"}).get_text()
        link = movies.find("div",{"class":"vU6FJ p63iDd"}).find("a")["href"]
        result = {'idx' : idx+1, 'title' : title, 'link' : f"https://play.google.com{link}"}
        movie_rank.append(result)
    return movie_rank

def google_movies_scroll_down():
    interval = 2 # 2초에 한번씩 스크롤 내림
    # 스크롤 맨밑으로 내리는 방법
    prev_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # 스크롤을 가장 아래로 내림
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # 페이지 로딩 대기
        time.sleep(interval)

        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break
        prev_height = curr_height
        

