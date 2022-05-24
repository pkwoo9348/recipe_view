import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
mysql = MySQL(app)


app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

@app.route('/api', methods=['GET', 'POST'])
def visit():
    if request.method == 'GET':
        # MySQL 서버에 접속하기
        cur = mysql.connection.cursor()
        # MySQL 명령어 실행하기
        cur.execute("SELECT * FROM recipe")
        # 전체 row 가져오기
        res = cur.fetchall()
        # Flask에서 제공하는 json변환 함수
        return jsonify(res)
    
    if request.method == 'POST':
        url = request.json['recipe_url']
        title = request.json['recipe_Title']
        ingedient = request.json['recipe_Ingredients']
        Direction = request.json['recipe_Directions']
        # mysql 접속 후 cursor 생성하기
        cur = mysql.connection.cursor()
        # DB 데이터 삽입하기
        cur.execute("INSERT INTO recipe (url, Title, Ingredients, Directions) VALUES(%s,%s, %s, %s)", [url, title, ingedient, Direction])
        # DB에 수정사항 반영하기
        mysql.connection.commit()
        # mysql cursor 종료하기
        cur.close()
        return

if __name__ == '__main__':
    app.run(debug=True)
    
