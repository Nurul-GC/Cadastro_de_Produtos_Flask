from app.Main import *
from flask import render_template, request, redirect, url_for
from app.models.produtos import *


@app.route('/index/')
@app.route('/')
def index():
    produtos_index = Produtos.query.all()

    return render_template('index.html', produto=produtos_index)


@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar():
    cadastrar_produtos = Produtos
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        estoqueMin = request.form['estoqueMin']
        saldoEstoque = request.form['saldoEstoque']
        obs = request.form['obs']

        if not cadastrar_produtos.query.filter_by(nome=nome).all():
            inserir = cadastrar_produtos(nome, preco, estoqueMin, saldoEstoque, obs)
            db.session.add(inserir)
            db.session.commit()
    else:
        return render_template('cadastrar.html')
    return render_template('cadastrar.html')


@app.route('/deletar/<id>')
def deletar(_id):
    a = Produtos.query.filter_by().get(_id)
    db.session.delete(a)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/atualizar/<id>')
def update(_id):
    dados = Produtos.query.filter_by().get(_id)

    return render_template('atualizar.html', id=_id, dados=dados)


@app.route('/atualizaDados/<id>', methods=['POST'])
def updates(_id):
    nome = request.form['nome']
    preco = request.form['preco']
    estoqueMin = request.form['estoqueMin']
    saldoEstoque = request.form['saldoEstoque']
    observacao = request.form['obs']

    dados = Produtos.query.filter_by().get(_id)

    dados.nome = nome
    dados.preco = preco
    dados.estoque_minimo = estoqueMin
    dados.saldo_estoque = saldoEstoque
    dados.observacao = observacao

    db.session.add(dados)
    db.session.commit()

    return redirect(url_for('index'))
