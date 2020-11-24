from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news
from naver_weather import naver_weather
from fortune import extract_fortune
# from naver_movie_rank import naver_movie
from select_movie_rank import select_movie
from select_on_screen import select_on
from naver_on_screen import on_screen
from english import r1, r2, r3


app = Flask(__name__)
app.debug = True


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route('/')
def home():
    headline = headline_news()
    weather = naver_weather()
    return render_template("index.html", headline=headline, weather=weather)


@app.route("/home")
def test():
    weather = naver_weather()
    return render_template("home.html",weather=weather)

@app.route("/report")
def news():
    headline = headline_news()
    weather = naver_weather()
    word = request.args.get('title')
    if word:
        word = word.lower()
        titles = search_news(word)
    else:
        return redirect("/")
    return render_template("home.html", headline=headline, news_title=word, titles=titles, weather=weather)

@app.route("/movie_rank")
def movies():
    weather = naver_weather()
    movies = select_movie()
    return render_template("movie_rank.html", weather=weather, movies=movies)
    
@app.route("/on_screen")
def movie():
    weather = naver_weather()
    movies = select_on()
    return render_template("on_screen.html", weather=weather, movies=movies)


@app.route("/fortune_select")
def fortune_select():
    headline = headline_news()
    weather = naver_weather()
    return render_template("fortune_select.html", headline=headline, weather=weather)

@app.route("/fortune")
def fortune():
    headline = headline_news()
    weather = naver_weather()
    value = request.args.get('selectBox')
    result = extract_fortune(value)
    return render_template("fortune.html", headline=headline, weather=weather, result=result)

@app.route("/english")
def en():
    weather = naver_weather()
    english1 = r1()
    english2 = r2()
    english3 = r3()
    return render_template("english.html", weather=weather, english1=english1, english2=english2, english3=english3)

app.run(host="127.0.0.1")