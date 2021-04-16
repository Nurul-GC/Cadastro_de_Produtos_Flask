from app.Main import db


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    preco = db.Column(db.Integer)
    estoque_minimo = db.Column(db.Integer)
    saldo_estoque = db.Column(db.Integer)
    observacao = db.Column(db.Text)

    def __init__(self, nome, preco, estoqueminimo, saldoestoque, observacao):
        self.nome = nome
        self.preco = preco
        self.estoque_minimo = estoqueminimo
        self.saldo_estoque = saldoestoque
        self.observacao = observacao
