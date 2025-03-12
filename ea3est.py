import os

class Aluno:
    def __init__(self, matricula, nome, frequencia, disciplinas):
        self.matricula = matricula
        self.nome = nome
        self.frequencia = frequencia
        self.disciplinas = disciplinas

    def __str__(self):
        return (f"Aluno: {self.nome}  \n  Matrícula: {self.matricula}  \n  Frequência: {self.frequencia}  \n  Disciplinas: {', '.join(self.disciplinas)}")

# Criação de arquivo com a lista, para armazenar no sistema.
def criar_arquivo():
    if not os.path.exists('alunos.txt'):
        with open('alunos.txt', 'w') as arquivo:
            pass

# Salvar alunos no arquivo
def salvar_alunos(Alunos):
    with open('alunos.txt', 'w') as arquivo:
        for aluno in Alunos:
            arquivo.write(f"{aluno.matricula},{aluno.nome},{aluno.frequencia},{','.join(aluno.disciplinas)}\n")

# Carregar os alunos do arquivo
def carregar_alunos():
    alunos = []
    if os.path.exists('alunos.txt'):
        with open('alunos.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                matricula = dados[0]
                nome = dados[1]
                frequencia = dados[2]
                disciplinas = dados[3:]
                alunos.append(Aluno(matricula, nome, frequencia, disciplinas))

    return alunos

# Experiência de Aprendizagem 3
def busca_binaria(lista, chave):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        matricula = lista[meio].matricula
        
        # Verifica se encontrou a matrícula
        if matricula == chave:
            return lista[meio]
        elif matricula < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

def main():
    criar_arquivo()
    Alunos = carregar_alunos()

    # Ordenar os alunos pela matrícula para a busca binária
    Alunos.sort(key=lambda aluno: aluno.matricula)

    while True:
        # Menu
        opcao = input('Centro Universitário Cesmac.  \n ----------------- \n O que deseja fazer?  \n 1 - Verificar alunos registrados. \n 2 - Editar alunos registrados. \n 3 - Adicionar aluno \n 4 - Remover aluno \n 5 - Sair\n')
        if opcao == '1':    # Verificar
            for aluno in Alunos:
                print(aluno)

        elif opcao == '2':    # Editar
            editar = input('Qual o número da matrícula do aluno que deseja editar? ')
            aluno = busca_binaria(Alunos, editar)
            
            if aluno:
                print(f'Aluno encontrado: {aluno}')
                print('O que deseja editar? \n 1 - Frequência \n 2 - Disciplinas')
                
                opcao_editar = input('Escolha a opção: ')
                
                if opcao_editar == '1':
                    nova_frequencia = input('Digite a nova frequência: ')
                    antiga_frequencia = aluno.frequencia
                    aluno.frequencia = nova_frequencia
                    print(f'Frequência alterada de {antiga_frequencia} para {aluno.frequencia}')
                
                elif opcao_editar == '2':
                    novas_disciplinas = input('Digite as novas disciplinas, separadas por vírgula e sem ponto final.: ')
                    aluno.disciplinas = [disciplina.strip() for disciplina in novas_disciplinas.split(',')]
                    print(f'Disciplinas alteradas para: {", ".join(aluno.disciplinas)}')
            else:
                print(f'Aluno com matrícula {editar} não encontrado.')

        elif opcao == '3':   # Adicionar
            matricula = input('Matrícula do aluno: ')
            nome = input('Nome do aluno: ')
            frequencia = input('Frequência do aluno: ')
            disciplinas = input('Disciplinas, separadas por vírgula: ').split(',')
            aluno_novo = Aluno(matricula, nome, frequencia, [disciplina.strip() for disciplina in disciplinas])
            Alunos.append(aluno_novo)
            Alunos.sort(key=lambda aluno: aluno.matricula)  # Reorganizar após adicionar novo aluno
            print(f'Aluno {nome} adicionado.')

        elif opcao == '4':   # Remover
            matricula_remover = input('Digite a matrícula do aluno que deseja remover: ')
            aluno = busca_binaria(Alunos, matricula_remover)

            if aluno:
                Alunos.remove(aluno)
                print(f'Aluno {aluno.nome} removido.')
            else:
                print(f'Aluno com matrícula {matricula_remover} não encontrado.')

        elif opcao == '5':   # Salvar e sair
            salvar_alunos(Alunos)
            print('Encerrando.')
            break

        else:
            print('Opção inválida!')

# Executar o programa
main()