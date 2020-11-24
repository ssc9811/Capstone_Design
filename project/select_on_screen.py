import pymysql

on_db = pymysql.connect(
        user='root', 
        passwd='1234', 
        host='127.0.0.1', 
        db='daliydb', 
        charset='utf8'
    )

cursor = on_db.cursor(pymysql.cursors.DictCursor)

def select_on():
    select_sql = '''select * from  movie_screen'''
    cursor.execute(select_sql)
    result= cursor.fetchall()
    return result
