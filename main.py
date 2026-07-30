class Plano:
    def __init__(self, nome, valor_mensal):
        if valor_mensal < 0:
            raise ValueError("O valor do plano não pode ser negativo.")
        self.nome = nome
        self.valor_mensal = valor_mensal

    def cartao(self):
        return f"Plano: {self.nome}\nMensalidade: R$ {self.valor_mensal:.2f}"


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cartao(self):
        return f"Nome: {self.nome}"


class Aluno(Pessoa):
    def __init__(self, nome, plano):
        super().__init__(nome)
        self.plano = plano

    def trocar_plano(self, novo_plano):
        self.plano = novo_plano

    def cartao(self):
        return (
            f"===== ALUNO =====\n"
            f"Nome: {self.nome}\n"
            f"Plano: {self.plano.nome}\n"
            f"Mensalidade: R$ {self.plano.valor_mensal:.2f}"
        )


class Instrutor(Pessoa):
    def __init__(self, nome, especialidade, salario):
        super().__init__(nome)

        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")

        self.especialidade = especialidade
        self.salario = salario

    def cartao(self):
        return (
            f"=== INSTRUTOR ===\n"
            f"Nome: {self.nome}\n"
            f"Especialidade: {self.especialidade}\n"
            f"Salário: R$ {self.salario:.2f}"
        )


class Academia:
    def __init__(self):
        self.planos = []
        self.alunos = []
        self.instrutores = []

    # Cadastrar plano
    def cadastrar_plano(self, nome, valor):
        plano = Plano(nome, valor)
        self.planos.append(plano)
        return plano

    # Cadastrar aluno
    def cadastrar_aluno(self, nome, plano):
        aluno = Aluno(nome, plano)
        self.alunos.append(aluno)

    # Cadastrar instrutor
    def cadastrar_instrutor(self, nome, especialidade, salario):
        instrutor = Instrutor(nome, especialidade, salario)
        self.instrutores.append(instrutor)

    # Listar alunos
    def listar_alunos(self):
        print("\n--- ALUNOS ---")
        for aluno in self.alunos:
            print(aluno.cartao())
            print()

    # Listar instrutores
    def listar_instrutores(self):
        print("\n--- INSTRUTORES ---")
        for instrutor in self.instrutores:
            print(instrutor.cartao())
            print()

    # Calcular faturamento
    def calcular_faturamento(self):
        return sum(aluno.plano.valor_mensal for aluno in self.alunos)


# ==========================
# Exemplo de utilização
# ==========================

academia = Academia()

# Cadastro de planos
basico = academia.cadastrar_plano("Básico", 80)
premium = academia.cadastrar_plano("Premium", 150)

# Cadastro de alunos
academia.cadastrar_aluno("João", basico)
academia.cadastrar_aluno("Maria", premium)

# Cadastro de instrutores
academia.cadastrar_instrutor("Carlos", "Musculação", 3500)
academia.cadastrar_instrutor("Ana", "Pilates", 4200)

# Listagens
academia.listar_alunos()
academia.listar_instrutores()

# Faturamento
print(f"Faturamento mensal: R$ {academia.calcular_faturamento():.2f}")

# Troca de plano
academia.alunos[0].trocar_plano(premium)

print("\nApós troca de plano:\n")
print(academia.alunos[0].cartao())

print(f"\nNovo faturamento: R$ {academia.calcular_faturamento():.2f}")
