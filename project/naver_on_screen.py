import requests
from bs4 import BeautifulSoup
import pymysql



def on_screen():
    url = ("https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve")
    headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    movie = soup.find("ul",class_="lst_detail_t1")
    lis = movie.findAll("li")
    on_s_rank = []

    on_db = pymysql.connect(
        user='root', 
        passwd='1234', 
        host='127.0.0.1', 
        db='daliydb', 
        charset='utf8'
    )

    cursor = on_db.cursor(pymysql.cursors.DictCursor)

    set_sql = "delete from movie_screen;"
    set_rank = "ALTER TABLE movie_screen AUTO_INCREMENT = 1;"
    sql = "insert into movie_screen (title, link, rate, ticket) values(%s,%s,%s,%s);"
    
    cursor.execute(set_sql)
    cursor.execute(set_rank)
    on_db.commit()

    for li in lis:
        try:
            title = li.find("dt", class_="tit").find("a").get_text()
            link = li.find("dt", class_="tit").find("a")["href"]
            rate = li.find("div", class_="star_t1").find("span",class_="num").get_text()
            ticket = li.find("div", class_="star_t1 b_star").find("span",class_="num").get_text()
            result = title,f"https://movie.naver.com/{link}",rate,ticket
            cursor.execute(sql,result)
            on_db.commit()
            on_s_rank.append(result)  
        except AttributeError as e:
            continue
    
    return on_s_rank



