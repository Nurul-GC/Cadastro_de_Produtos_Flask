from Main import db


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, not_null=True, unique=True)
    preco = db.Column(db.Integer, not_null=True)
    estoque_minimo = db.Column(db.Integer, not_null=True)
    saldo_estoque = db.Column(db.Integer, not_null=True)
    observacao = db.Column(db.Text)

    def __init__(self, nome, preco, estoqueminimo, saldoestoque, observacao):
        self.nome = nome
        self.preco = preco
        self.estoque_minimo = estoqueminimo
        self.saldo_estoque = saldoestoque
        self.observacao = observacao
