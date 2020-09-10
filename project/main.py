from google_news import search_news
from naver_weather import naver_weather


naver_weather()

SEARCH = input("기사 검색 : ")
search_news(SEARCH)