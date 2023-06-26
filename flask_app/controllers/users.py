
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def display():
    return render_template("read.html", users=User.get_all())

@app.route("/user/new")
def create_user():
    return render_template("create.html")

@app.route('/create/new_user',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')