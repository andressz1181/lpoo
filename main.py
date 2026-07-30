class Plano:
    def __init__(self, nome, valor):
        if valor < 0:
            raise ValueError("O valor do plano não pode ser negativo.")
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"{self.nome} - R$ {self.valor:.2f}"


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def exibir_cartao(self):
        print("-------------------------")
        print(f"Nome: {self.nome}")
        print("-------------------------")


class Aluno(Pessoa):
    def __init__(self, nome, plano):
        super().__init__(nome)
        self.plano = plano

    def trocar_plano(self, novo_plano):
        self.plano = novo_plano

    def exibir_cartao(self):
        print("-------------------------")
        print("CARTÃO DO ALUNO")
        print(f"Nome : {self.nome}")
        print(f"Plano: {self.plano.nome}")
        print(f"Mensalidade: R$ {self.plano.valor:.2f}")
        print("-------------------------")


class Instrutor(Pessoa):
    def __init__(self, nome, especialidade, salario):
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        super().__init__(nome)
        self.especialidade = especialidade
        self.salario = salario

    def exibir_cartao(self):
        print("-------------------------")
        print("CARTÃO DO INSTRUTOR")
        print(f"Nome: {self.nome}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Salário: R$ {self.salario:.2f}")
        print("-------------------------")


planos = []
alunos = []
instrutores = []


def cadastrar_plano():
    nome = input("Nome do plano: ")

    try:
        valor = float(input("Valor mensal: R$ "))
        plano = Plano(nome, valor)
        planos.append(plano)
        print("Plano cadastrado com sucesso!")
    except ValueError as erro:
        print(erro)


def cadastrar_aluno():
    if len(planos) == 0:
        print("Cadastre um plano primeiro.")
        return

    nome = input("Nome do aluno: ")

    print("\nPlanos disponíveis:")
    for i, plano in enumerate(planos):
        print(f"{i + 1} - {plano}")

    try:
        escolha = int(input("Escolha um plano: "))
        plano = planos[escolha - 1]
        aluno = Aluno(nome, plano)
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    except:
        print("Opção inválida.")


def cadastrar_instrutor():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")

    try:
        salario = float(input("Salário: R$ "))
        instrutor = Instrutor(nome, especialidade, salario)
        instrutores.append(instrutor)
        print("Instrutor cadastrado com sucesso!")
    except ValueError as erro:
        print(erro)


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos):
        print(f"{i + 1} - {aluno.nome} ({aluno.plano.nome})")


def listar_instrutores():
    if len(instrutores) == 0:
        print("Nenhum instrutor cadastrado.")
        return

    for i, instrutor in enumerate(instrutores):
        print(f"{i + 1} - {instrutor.nome} ({instrutor.especialidade})")


def calcular_faturamento():
    total = 0

    for aluno in alunos:
        total += aluno.plano.valor

    print(f"Faturamento mensal: R$ {total:.2f}")


def trocar_plano():
    if len(alunos) == 0:
        print("Não existem alunos.")
        return

    if len(planos) == 0:
        print("Não existem planos.")
        return

    listar_alunos()

    try:
        indice = int(input("Escolha o aluno: ")) - 1
        aluno = alunos[indice]

        print("\nPlanos disponíveis:")
        for i, plano in enumerate(planos):
            print(f"{i + 1} - {plano}")

        novo = int(input("Novo plano: ")) - 1
        aluno.trocar_plano(planos[novo])

        print("Plano alterado com sucesso!")

    except:
        print("Opção inválida.")


def exibir_cartao():
    print("1 - Aluno")
    print("2 - Instrutor")

    opcao = input("Escolha: ")

    if opcao == "1":

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
            return

        listar_alunos()

        try:
            indice = int(input("Aluno: ")) - 1
            alunos[indice].exibir_cartao()
        except:
            print("Opção inválida.")

    elif opcao == "2":

        if len(instrutores) == 0:
            print("Nenhum instrutor cadastrado.")
            return

        listar_instrutores()

        try:
            indice = int(input("Instrutor: ")) - 1
            instrutores[indice].exibir_cartao()
        except:
            print("Opção inválida.")

    else:
        print("Opção inválida.")


while True:

    print("\n========== ACADEMIA ==========")
    print("1 - Cadastrar plano")
    print("2 - Cadastrar aluno")
    print("3 - Cadastrar instrutor")
    print("4 - Listar alunos")
    print("5 - Listar instrutores")
    print("6 - Calcular faturamento mensal")
    print("7 - Trocar plano de um aluno")
    print("8 - Exibir cartão")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_plano()

    elif opcao == "2":
        cadastrar_aluno()

    elif opcao == "3":
        cadastrar_instrutor()

    elif opcao == "4":
        listar_alunos()

    elif opcao == "5":
        listar_instrutores()

    elif opcao == "6":
        calcular_faturamento()

    elif opcao == "7":
        trocar_plano()

    elif opcao == "8":
        exibir_cartao()

    elif opcao == "9":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
