import sys
from pathlib import Path

# Garante que a pasta src esteja no caminho de busca do Python
sys.path.insert(0, str(Path(__file__).resolve().parent))

from datetime import date
from modelos.cliente import PessoaFisica
from modelos.conta import ContaCorrente
from modelos.transacao import Deposito, Saque


def menu():
    texto = """\n
    ================ MENU ================
    [1] Novo Cliente
    [2] Nova Conta
    [3] Depositar
    [4] Sacar
    [5] Extrato / Histórico
    [6] Listar Contas
    [0] Sair
    => """
    return input(texto)


def buscar_cliente(cpf: str, clientes: list[PessoaFisica]) -> PessoaFisica | None:
    clientes_filtrados = [c for c in clientes if c.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_cliente(clientes: list[PessoaFisica]):
    cpf = input("Informe o CPF (somente números): ").strip()
    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        print("\nErro: Já existe cliente cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ").strip()
    data_str = input("Informe a data de nascimento (DD/MM/AAAA): ").strip()
    try:
        dia, mes, ano = map(int, data_str.split("/"))
        data_nascimento = date(ano, mes, dia)
    except Exception:
        print("\nErro: Formato de data inválido. Use DD/MM/AAAA.")
        return

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ").strip()

    novo_cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(novo_cliente)
    print("\nCliente cadastrado com sucesso!")


def criar_conta(numero_conta: int, clientes: list[PessoaFisica], contas: list[ContaCorrente]):
    cpf = input("Informe o CPF do titular: ").strip()
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\nErro: Cliente não encontrado. Cadastre o cliente primeiro.")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f"\nConta criada com sucesso! Agência: {conta.agencia} | Conta: {conta.numero}")


def realizar_deposito(clientes: list[PessoaFisica]):
    cpf = input("Informe o CPF do titular: ").strip()
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\nErro: Cliente não encontrado.")
        return

    if not cliente.contas:
        print("\nErro: O cliente não possui contas cadastradas.")
        return

    try:
        valor = float(input("Informe o valor do depósito: R$ "))
    except ValueError:
        print("\nErro: Digite um número válido.")
        return

    transacao = Deposito(valor)
    conta = cliente.contas[0]
    cliente.realizar_transacao(conta, transacao)


def realizar_saque(clientes: list[PessoaFisica]):
    cpf = input("Informe o CPF do titular: ").strip()
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\nErro: Cliente não encontrado.")
        return

    if not cliente.contas:
        print("\nErro: O cliente não possui contas cadastradas.")
        return

    try:
        valor = float(input("Informe o valor do saque: R$ "))
    except ValueError:
        print("\nErro: Digite um número válido.")
        return

    transacao = Saque(valor)
    conta = cliente.contas[0]
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes: list[PessoaFisica]):
    cpf = input("Informe o CPF do titular: ").strip()
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\nErro: Cliente não encontrado.")
        return

    if not cliente.contas:
        print("\nErro: O cliente não possui contas cadastradas.")
        return

    conta = cliente.contas[0]
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in transacoes:
            tipo = t.__class__.__name__
            print(f"{tipo}:\tR$ {t.valor:.2f}")

    print(f"\nSaldo atual:\tR$ {conta.saldo():.2f}")
    print("==========================================")


def listar_contas(contas: list[ContaCorrente]):
    if not contas:
        print("\nNenhuma conta registrada.")
        return

    for c in contas:
        print("=" * 40)
        print(f"Agência:\t{c.agencia}")
        print(f"Conta:\t\t{c.numero}")
        print(f"Titular:\t{c.cliente.nome}")
        print(f"Saldo:\t\tR$ {c.saldo():.2f}")


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu().strip()

        if opcao == "1":
            criar_cliente(clientes)
        elif opcao == "2":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "3":
            realizar_deposito(clientes)
        elif opcao == "4":
            realizar_saque(clientes)
        elif opcao == "5":
            exibir_extrato(clientes)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida, tente novamente.")


if __name__ == "__main__":
    main()