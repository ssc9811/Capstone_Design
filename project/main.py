from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news
from naver_weather import naver_weather
from fortune import extract_fortune
from naver_movie_rank import naver_movie
from naver_on_screen import on_screen


app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    headline = headline_news()
    weather = naver_weather()
    return render_template("home.html", headline=headline, weather=weather)

@app.route("/report")
def news():
    weather = naver_weather()
    word = request.args.get('title')
    if word:
        word = word.lower()
        titles = search_news(word)
    else:
        return redirect("/")
    return render_template("home.html", news_title=word, titles=titles, weather=weather)

@app.route("/movies")
def movies():
    weather = naver_weather()
    movies = naver_movie()
    return render_template("movies.html", weather=weather, movies=movies)

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

@app.route("/todo")
def todo():
    weather = naver_weather()
    return render_template("todo.html", weather=weather)

app.run(host="127.0.0.1")