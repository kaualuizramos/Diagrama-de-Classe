## Sistema Bancário Orientado a Objetos

Implementação de um sistema bancário em Python com base no diagrama de classes UML.

## Tecnologias Utilizadas

- Python 3.10+
- Módulo `abc` (Classes Abstratas e Interfaces)
- Módulo `datetime`

## Estrutura do Projeto

- `transacao.py`: Interface `Transacao` e classes concretas `Deposito` e `Saque`.
- `historico.py`: Gestão da lista de transações efetuadas.
- `conta.py`: Classe base `Conta` e especialização `ContaCorrente`.
- `cliente.py`: Classe base `Cliente` e especialização `PessoaFisica`.
- `main.py`: Execução dos fluxos de teste e demonstração do saldo.

## Como Executar
   ```bash
   cd "sistema bancário/src"
   python main.py