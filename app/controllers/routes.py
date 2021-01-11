from Main import app
from flask import render_template, request
from models.produtos import Produtos
from Main import db


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    produtos = Produtos
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        estoqueMin = request.form['estoqueMin']
        saldoEstoque = request.form['saldoEstoque']
        obs = request.form['obs']

        if produtos.query.filter_by(nome=nome).all() == []:
            inserir = produtos(nome, preco, estoqueMin, saldoEstoque,  obs)
            db.session.add(inserir)
            db.session.commit()

    return render_template('cadastrar.html')
