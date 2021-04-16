from app.Main import app, db
from flask import render_template, request, redirect, url_for
from app.models.produtos import *


@app.route('/index/')
@app.route('/')
def index():
    produtos = Produtos.query.all()

    return render_template('index.html', produto=produtos)


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
            inserir = produtos(nome, preco, estoqueMin, saldoEstoque, obs)
            db.session.add(inserir)
            db.session.commit()
    else:
        return render_template('cadastrar.html')
    return render_template('cadastrar.html')


@app.route('/deletar/<id>')
def deletar(id):
    a = Produtos.query.filter_by().get(id)
    db.session.delete(a)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/atualizar/<id>')
def update(id):
    dados = Produtos.query.filter_by().get(id)

    return render_template('atualizar.html', id=id, dados=dados)


@app.route('/atualizaDados/<id>', methods=['POST'])
def updates(id):
    nome = request.form['nome']
    preco = request.form['preco']
    estoqueMin = request.form['estoqueMin']
    saldoEstoque = request.form['saldoEstoque']
    observacao = request.form['obs']

    dados = Produtos.query.filter_by().get(id)

    dados.nome = nome
    dados.preco = preco
    dados.estoque_minimo = estoqueMin
    dados.saldo_estoque = saldoEstoque
    dados.observacao = observacao

    db.session.add(dados)
    db.session.commit()

    return redirect(url_for('index'))
