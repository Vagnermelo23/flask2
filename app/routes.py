from app import app
from flask import render_template, redirect, url_for
from flask import request


@app.route('/')
def index_default():
    nome = "usuário"  
    return render_template('index.html', nome=nome)

@app.route('/index/<nome>')
def index(nome):
    return render_template('index.html', nome=nome)

@app.route ('/login')
def login ():
    return render_template('login.html')

@app.route ('/autenticar', methods=['GET'])
def autenticar ():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return redirect(url_for('index', nome=usuario))