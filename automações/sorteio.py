import random  # Importa o módulo random para usar a função choice

# Define a função sortio_aluno que sorteia um aluno de uma lista
def sortio_aluno():
    alunos = ['Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4', 'Aluno 5']  # Lista de alunos
    escolher = random.choice(alunos)  # Escolhe aleatoriamente um aluno da lista
    print(f"O aluno escolhido foi: {escolher}")  # Imprime o nome do aluno escolhido

# Chama a função sortio_aluno para realizar o sorteio
sortio_aluno()