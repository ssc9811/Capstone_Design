from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news
from naver_weather import naver_weather
# from fortune import extract_fortune
# from google_movies import google_movies

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    headline = headline_news()
    weather = naver_weather()
    word = request.args.get('name')
    if word:
        word = word.lower()
        titles = search_news(word)
    else:
        return redirect("/")
    return render_template("home.html", headline=headline, weather=weather, news_title=word, titles=titles)

# @app.route("/")
# def news():
#     word = request.args.get('name')
#     if word:
#         word = word.lower()
#         titles = search_news(word)
#         print(type(word))
#     else:
#         return redirect("/")
#     return render_template("home.html", news_title=word, titles=titles)

# @app.route("/movies")
# def movies():
#     movies = google_movies()
#     return render_template("movies.html", movies=movies)

# @app.route("/fortune")
# def fortune():
#     value = request.args.get('selectBox')
#     # print(type(value))
#     result = extract_fortune(value)
#     return render_template("test.html", value=value, result=result)

app.run(host="127.0.0.1")