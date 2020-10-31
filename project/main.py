from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news
from naver_weather import naver_weather
from fortune import extract_fortune
# from google_movies import google_movies

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    headline = headline_news()
    weather = naver_weather()
    return render_template("home.html", headline=headline, weather=weather)

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
    return render_template("home.html", news_title=word, titles=titles, headline=headline, weather=weather)

# @app.route("/movies")
# def movies():
#     movies = google_movies()
#     return render_template("movies.html", movies=movies)

@app.route("/fortune")
def fortune():
    headline = headline_news()
    weather = naver_weather()
    value = request.args.get('selectBox')
    result = extract_fortune(value)
    return render_template("home.html", headline=headline, weather=weather, result=result)

app.run(host="127.0.0.1")