class Conta:
    _saldo = 0

    def __init__(self, titular, numero):
        self._titular = titular
        self._numero = numero

    def saque(self, valor):
        if (self._saldo >= valor):
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def depositar(self, valor):
        self._saldo += valor

    def extrato(self):
        print("Cliente:", self._titular, "Saldo Atual:", self._saldo)




    @property
    def saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if (saldo < 0):
            print("O saldo nao pode ser negativo")
        else:
            self.saldo = saldo

