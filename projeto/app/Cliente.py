class Cliente:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    #método get
    def get_nome(self):
        return self._nome

    #método set
    def set_nome(self, nome):
        self._nome = nome