from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news

app = Flask(__name__)

@app.route("/")
def home():
    headline = headline_news()
    return render_template("home.html", headline=headline)

@app.route("/report")
def name():
    # print(request.args.get('name'))
    word = request.args.get('name')
    if word:
        word = word.lower()
        titles = search_news(word)
    else:
        return redirect("/")
    return render_template("report.html", news_title=word, titles=titles)

# @app.route("/<name>")
# def username(name):
#     return f"당신의 이름은 {name}"

app.run(host="127.0.0.1")