class Doador:
    def __init__(self, nome, cpf, produto_doado, qtd_produto):
        self._nome = nome
        self._cpf = cpf
        self._produto_doado = produto_doado
        self._qtd_produto = qtd_produto

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def produto_doado(self):
        return self._produto_doado

    @property
    def qtd_produto(self):
        return self._qtd_produto


    