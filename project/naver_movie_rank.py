import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import pymysql

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}


def naver_movie():
    url = ("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date={}".format(datetime.today().strftime("%Y%m%d")))
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    movie = soup.find("table", {"class": "list_ranking"})
    lis = movie.find_all("tr")

    movie_rank = []
    reple = []
    i = 0

    mr_db = pymysql.connect(
        user='root', 
        passwd='1234', 
        host='127.0.0.1', 
        db='daliydb', 
        charset='utf8'
    )

    cursor = mr_db.cursor(pymysql.cursors.DictCursor)

    set_sql = "delete from movie_rank;" #삭제
    set_rank = "ALTER TABLE movie_rank AUTO_INCREMENT = 1;" #AUTO_INCREMENT 초기화
    sql = "insert into movie_rank (title, link, rate, reple) values(%s,%s,%s,%s);"
    sss = "select * from movie_rank;"
    
    cursor.execute(set_sql)
    cursor.execute(set_rank)
    mr_db.commit()

    def naver_review(link):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
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
            db_rs = title,f"https://movie.naver.com{link}",rate,reple[i]
            cursor.execute(sql,db_rs)
            mr_db.commit()
            i += 1
        except AttributeError as e:
            continue
    cursor.execute(sss)
    s1 = cursor.fetchall()
    # print(s1)
    return movie_rank
# naver_movie()


