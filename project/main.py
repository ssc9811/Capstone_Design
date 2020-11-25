from flask import Flask , render_template, request, redirect
from google_news import search_news, headline_news
from naver_weather import naver_weather
from fortune import extract_fortune
from naver_movie_rank import naver_movie
from naver_on_screen import on_screen
from select_movie_rank import select_movie
from select_on_screen import select_on
from english import r1, r2, r3
import pymysql, bcrypt


app = Flask(__name__)
app.debug = True

db = pymysql.connect(user='root', passwd='1234', host='127.0.0.1', db='daliydb', charset='utf8')
cursor = db.cursor(pymysql.cursors.Cursor)

@app.route('/main')
def main():
    headline = headline_news()
    weather = naver_weather()
    return render_template("index.html", headline=headline, weather=weather)

@app.route("/home")
def home():
    headline = headline_news()
    weather = naver_weather()
    return render_template("home.html",weather=weather, headline=headline)

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

@app.route('/', methods=['GET'])
def index():
    
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

    return render_template('login.html')
@app.route('/confirm_register', methods=['POST'])
def confirm_register():
    db = pymysql.connect(user='root', passwd='1234', host='127.0.0.1', db='daliydb', charset='utf8')
    cursor = db.cursor(pymysql.cursors.Cursor)
    if request.method == 'POST':
        register_info = request.form
        id = register_info['id']
        first_name = register_info['first_name']
        last_name = register_info['last_name']
        name = first_name+last_name
        pw = bcrypt.hashpw(register_info['pw'].encode('UTF-8'), bcrypt.gensalt())
        pw_verify = bcrypt.hashpw(register_info['pw_verify'].encode('UTF-8'), bcrypt.gensalt())
        email = register_info['email']
        tel = '010'+register_info['tel']
        print(id,name,pw,pw_verify,email,tel)
        sql = """insert into member (id,hashed_pw,name,email,tel) values(%s,%s,%s,%s,%s);"""
        cursor.execute(sql,(id,pw,name,email,tel))
        db.commit()
        db.close()

        return redirect("/")
    
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    db = pymysql.connect(user='root', passwd='1234', host='127.0.0.1', db='daliydb', charset='utf8')
    cursor = db.cursor(pymysql.cursors.Cursor)
    if request.method == 'POST':
        login_info = request.form

        user_id = login_info['id']
        user_pw = login_info['pw']

        sql = "select * from member where id = %s"
        rows_cnt = cursor.execute(sql, user_id)

        if rows_cnt > 0:
            user_info = cursor.fetchone()
            print("user_info : ",user_info)

            is_pw_verify = bcrypt.checkpw(user_pw.encode('UTF-8'), user_info[1].encode('UTF-8'))
            print("password check : ",is_pw_verify)

        else:
            print("User does not exist")
        db.close()
        return redirect("/home")
    
    return render_template('login.html')


db.close()
app.run(host="127.0.0.1")