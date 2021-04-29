import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

DATABASE = "./tmp/flaskr.db"
SECRET_KEY = "teste"
USERNAME = "admin"
PASSWORD = "default"

app = Flask(__name__)
app.config.from_object(__name__)

def criar_bd():
    with closing(conectar_bd()) as bd:
        with app.open_resource('esquema.sql') as sql:
            bd.cursor().executescript(sql.read().decode("utf-8"))
        bd.commit()

def conectar_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.bd.close()

@app.route('/')
def index():
    return "<h1>Roberto ama seu norte<h1>"