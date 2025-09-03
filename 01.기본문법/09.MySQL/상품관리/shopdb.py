import pymysql

con = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='shop',
    charset='utf8',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
cur = con.cursor()
