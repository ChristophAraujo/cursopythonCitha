import time  # Importa o módulo time para usar a função sleep
import random  # Importa o módulo random para usar a função choice

# Define a função mensagemPersonalizada que recebe uma lista de nomes
def mensagemPersonalizada(lista):
    print("Olá, " + random.choice(lista) + "!")  # Imprime uma mensagem personalizada com um nome aleatório da lista
    time.sleep(2)  # Pausa a execução por 2 segundos
    print("Seja bem-vindo(a) ao mundo Python!")  # Imprime uma mensagem de boas-vindas
    time.sleep(2)  # Pausa a execução por 2 segundos
    print("esta mensagem esta simulando um chatbot")  # Imprime uma mensagem simulando um chatbot

# Inicializa uma lista vazia para armazenar os nomes
listaNome = []
#for i in range(3):
#    listaNome.append(input("Digite um nome: "))  # Código comentado para adicionar nomes à lista

maisnome = "Ss"  # Inicializa a variável maisnome com "Ss" para entrar no loop

# Loop infinito para coletar nomes do usuário
while True:
    listaNome.append(input("Digite um nome: "))  # Adiciona o nome digitado pelo usuário à lista
    maisnome = input("deseja continuar: S/N \n").lower()  # Pergunta se o usuário deseja continuar e converte a resposta para minúsculo
    if maisnome == "n":  # Se a resposta for "n", sai do loop
        break

# Chama a função mensagemPersonalizada passando a lista de nomes coletados
mensagemPersonalizada(listaNome)