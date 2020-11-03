import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}


def naver_movie():
    url = ("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date={}".format(datetime.today().strftime("%Y%m%d")))
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    movie = soup.find("table", {"class": "list_ranking"})
    lis = movie.find_all("tr")

    movie_rank = []
    movie_link = []
    reple = []
    i=0

    def naver_review(link):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        # for idx in range(0, len(movie_link)):
        url2 = (f"https://movie.naver.com{link}")
        res = requests.get(url2, headers=headers)
        res.raise_for_status()
        soup2 = BeautifulSoup(res.text, "lxml")
        review = soup2.find("div",{"class":"score_result"})
        reple1 = review.find("p").get_text(strip=True)
        reple.append(reple1)
        return reple

    for movies in lis:
        try:
            title = movies.find("td", class_="title").get_text()[2:-2]
            link = movies.find("div",{"class":"tit5"}).find("a")["href"]
            naver_review(link)
            rate = movies.find("td",{"class":"point"}).get_text()
            result = {'idx' : i+1, 'title' : title, 'link' : f"https://movie.naver.com{link}", 'rate' : rate, 'reple' : reple[i]}
            movie_rank.append(result)
            i+=1
        except AttributeError as e:
            continue

    return movie_rank


