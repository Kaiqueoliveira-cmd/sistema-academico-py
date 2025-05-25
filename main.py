import json
import statistics

class SistemaCadastroAlunos:
    def __init__(self):
        self.alunos = {}
        self.carregar_dados()  # Carrega dados do arquivo JSON ao iniciar

    def salvar_dados(self):
        """Salva os dados dos alunos em um arquivo JSON"""
        with open('alunos.json', 'w') as arquivo:
            json.dump(self.alunos, arquivo, indent=4)

    def carregar_dados(self):
        """Carrega os dados dos alunos de um arquivo JSON"""
        try:
            with open('alunos.json', 'r') as arquivo:
                self.alunos = json.load(arquivo)
        except FileNotFoundError:
            self.alunos = {}

    def cadastrar_aluno(self):
        print("\n--- Cadastro de Aluno ---")
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        curso = input("Curso: ")
        genero = input("masculino ou feminino")
        idade = input("Idade: ")

        self.alunos[matricula] = {
            'nome': nome,
            'curso': curso,
            'idade': idade,
            'notas': []
        }
        self.salvar_dados()
        print(f"Aluno {nome} cadastrado com sucesso!")

    def listar_alunos(self):
        print("\n--- Lista de Alunos Cadastrados ---")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        
        for matricula, info in self.alunos.items():
            print(f"\nMatrícula: {matricula}")
            print(f"Nome: {info['nome']}")
            print(f"Curso: {info['curso']}")
            print(f"Idade: {info['idade']}")
            print(f"Notas: {info['notas']}")
            if info['notas']:
                print(f"Média: {statistics.mean(info['notas']):.2f}")
                print(f"Mediana: {statistics.median(info['notas']):.2f}")

    def buscar_aluno(self):
        matricula = input("\nDigite a matrícula do aluno: ")
        aluno = self.alunos.get(matricula)
        
        if aluno:
            print("\n--- Aluno Encontrado ---")
            print(f"Matrícula: {matricula}")
            print(f"Nome: {aluno['nome']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Notas: {aluno['notas']}")
            if aluno['notas']:
                print(f"Média: {statistics.mean(aluno['notas']):.2f}")
                print(f"Mediana: {statistics.median(aluno['notas']):.2f}")
                print(f"Moda: {statistics.mode(aluno['notas'])}")
        else:
            print("Aluno não encontrado!")

    def adicionar_notas(self):
        matricula = input("\nDigite a matrícula do aluno: ")
        aluno = self.alunos.get(matricula)

        if not aluno:
            print("Aluno não encontrado!")
            return
        
        print("Digite as notas do aluno (0 a 10), digite -1 para encerrar:")
        while True:
            try:
                nota = float(input("Nota: "))
                if nota == -1:
                    break
                if 0 <= nota <= 10:
                    aluno['notas'].append(nota)
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")
        
        self.salvar_dados()

    def mostrar_situacao(self):
        matricula = input("\nDigite a matrícula do aluno: ")
        aluno = self.alunos.get(matricula)

        if not aluno:
            print("Aluno não encontrado!")
            return

        if not aluno['notas']:
            print("Nenhuma nota registrada para este aluno.")
            return

        media = statistics.mean(aluno['notas'])
        print(f"\nMédia das notas: {media:.2f}")
        print(f"Mediana: {statistics.median(aluno['notas']):.2f}")
        print(f"Moda: {statistics.mode(aluno['notas'])}")

        if media >= 7:
            print("Situação: Aprovado!")
        elif media >= 5:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")

    def menu(self):
        while True:
            print("\n=== Sistema de Cadastro de Alunos ===")
            print("1. Cadastrar novo aluno")
            print("2. Listar todos os alunos")
            print("3. Buscar aluno por matrícula")
            print("4. Adicionar notas ao aluno")
            print("5. Ver situação do aluno")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_aluno()
            elif opcao == '2':
                self.listar_alunos()
            elif opcao == '3':
                self.buscar_aluno()
            elif opcao == '4':
                self.adicionar_notas()
            elif opcao == '5':
                self.mostrar_situacao()
            elif opcao == '6':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Iniciar o sistema
if __name__ == "__main__":
    sistema = SistemaCadastroAlunos()
    sistema.menu()