import time  # Importa o módulo time para usar a função sleep

# Define a função mensagemPersonalizada que recebe uma lista de nomes
def mensagemPersonalizada(lista):
    # Itera sobre cada nome na lista
    for i in listaNome:
        print(f"Olá, {i}!")  # Imprime uma mensagem personalizada para cada nome
        time.sleep(1)  # Pausa a execução por 2 segundos
        print("Seja bem-vindo(a) ao mundo Python!")  # Imprime uma mensagem de boas-vindas
        time.sleep(1)  # Pausa a execução por 2 segundos
        print("esta mensagem esta simulando um chatbot")  # Imprime uma mensagem simulando um chatbot

# Inicializa uma lista vazia para armazenar os nomes
listaNome = []


# Loop infinito para coletar nomes do usuário
while True:
    listaNome.append(input("Digite um nome: "))  # Adiciona o nome digitado pelo usuário à lista
    maisnome = input("deseja continuar: S/N \n").lower()  # Pergunta se o usuário deseja continuar e converte a resposta para minúsculo
    if maisnome == "n":  # Se a resposta for "n", sai do loop
        break

# Chama a função mensagemPersonalizada passando a lista de nomes coletados
mensagemPersonalizada(listaNome)