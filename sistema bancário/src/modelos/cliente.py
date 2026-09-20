from datetime import date


class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list:
        return self._contas

    def realizar_transacao(self, conta, transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento