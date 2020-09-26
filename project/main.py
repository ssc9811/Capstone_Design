from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news
from naver_weather import naver_weather
from fortune import extract_fortune


app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    headline = headline_news()
    weather = naver_weather()
    return render_template("home.html", headline=headline, weather=weather)

@app.route("/report")
def news():
    # print(request.args.get('name'))
    word = request.args.get('name')
    if word:
        word = word.lower()
        titles = search_news(word)
        print(type(word))
    else:
        return redirect("/")
    return render_template("report.html", news_title=word, titles=titles)

@app.route("/movies")
def movies():
    return render_template("movies.html")

@app.route("/fortune")
def fortune():
    value = request.args.get('selectBox')
    print(type(value))
    result = extract_fortune(value)
    return render_template("test.html", value=value, result = result)

app.run(host="127.0.0.1")