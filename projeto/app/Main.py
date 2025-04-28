class main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Docinho", "62 9178-3945")
conta = Conta(c1.get_nome(), 6565)

conta.depositar(100)
conta.saque(50)
conta.extrato()


