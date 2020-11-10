import requests
from bs4 import BeautifulSoup


def on_screen():
    url = ("https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    movie = soup.find("ul",class_="lst_detail_t1")
    lis = movie.findAll("li")
    on_s_rank = []
    
    i = 1
    for li in lis:
        try:
            title = li.find("dt", class_="tit").find("a").get_text()
            link = li.find("dt", class_="tit").find("a")["href"]
            rate = li.find("div", class_="star_t1").find("span",class_="num").get_text()
            ticket = li.find("div", class_="star_t1 b_star").find("span",class_="num").get_text()
            result = {'idx' : i, 'title' : title, 'link' : f"https://movie.naver.com/{link}", 'rate' : rate, 'ticket' : ticket}
            i = i+1;
            on_s_rank.append(result)  
        except AttributeError as e:
            continue
    # print(on_s_rank)
    return on_s_rank
