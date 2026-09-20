from modelos.historico import Historico
from modelos.transacao import Saque


class Conta:
    def __init__(self, numero: int, cliente, agencia: str = "0001"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero: int) -> "Conta":
        return cls(numero=numero, cliente=cliente)

    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("\nOperação falhou: o valor informado é inválido.")
            return False

        if valor > self._saldo:
            print("\nOperação falhou: saldo insuficiente.")
            return False

        self._saldo -= valor
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("\nOperação falhou: o valor informado deve ser positivo.")
            return False

        self._saldo += valor
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente, limite: float = 500.0, limite_saques: int = 3, agencia: str = "0001"):
        super().__init__(numero=numero, cliente=cliente, agencia=agencia)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        saques_realizados = len([t for t in self.historico.transacoes if isinstance(t, Saque)])

        if valor > (self._saldo + self._limite):
            print("\nOperação falhou: valor do saque excede saldo disponível + limite.")
            return False

        if saques_realizados >= self._limite_saques:
            print("\nOperação falhou: limite diário de saques atingido.")
            return False

        if valor <= 0:
            print("\nOperação falhou: valor informado é inválido.")
            return False

        self._saldo -= valor
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        return True