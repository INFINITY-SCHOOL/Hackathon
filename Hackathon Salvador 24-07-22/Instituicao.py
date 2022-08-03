import profile


class Instituicao:
    def __init__(self, nome, gerente):
        self._nome = nome
        self._gerente = gerente 
        self._doadores = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def gerente(self):
        return (self._gerente)

    @property
    def doadores(self):
        return self._doadores
    
    def AdicionarDoador (self, Doador):
        self._doadores.append (Doador)
