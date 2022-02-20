from multiprocessing import connection
from sqlite3 import Cursor
from flask import Flask,render_template,request
import os
import mysql.connector

connection=mysql.connector.connect(host="localhost",user="awab",password="awabahmed1",database="users")
cursor=connection.cursor()


app=Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute(""" Select * From `users` WHERE `email` LIKE '{}' AND `password`  LIKE '{}'  """
    .format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute(""" INSERT INTO `users` (`user_id`,`name`,`email`,`password`)
    VALUES (NULL,'{}','{}','{}') """ .format(name,email,password))
    connection.commit()
    return render_template('login.html')




@app.route("/home")
def home():
    return render_template('home.html')

if __name__ =="__main__":
    app.run(debug=True)
