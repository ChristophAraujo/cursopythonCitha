import random  # Importa o módulo random para usar a função choice

# Define a função sortio_num que sorteia um número de uma lista
def sortio_num():
    numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Lista de números
    escolher = random.choice(numero)  # Escolhe aleatoriamente um número da lista
    print(f"O número escolhido foi: {escolher}")  # Imprime o número escolhido

# Chama a função sortio_num para realizar o sorteio
sortio_num()