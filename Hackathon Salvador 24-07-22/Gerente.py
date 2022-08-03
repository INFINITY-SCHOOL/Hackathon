class Gerente:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf
