import time  # Importa o módulo time para usar a função sleep
import pyautogui
import webbrowser

# Define a função msgperson que coleta uma mensagem personalizada do usuário
def msgperson():
    msgpersonalizada = input("Digite a mensagem personalizada: ")
    return msgpersonalizada

# Define a função enviar_mensagem que envia uma mensagem no WhatsApp Web
def enviar_mensagem(nome, mensagem):
    webbrowser.open("https://web.whatsapp.com/send?phone=" + nome)
    time.sleep(10)  # Espera 10 segundos para garantir que a página carregue
    pyautogui.typewrite(mensagem)
    pyautogui.press('enter')

# Define a função menu que exibe as opções de mensagem
def menu(listaNome, listaMensagens):
    while True:
        print("\nMenu:")
        print("1. Adicionar nome")
        print("2. Adicionar mensagem personalizada")
        print("3. Mostrar mensagens personalizadas")
        print("4. Enviar mensagens no WhatsApp")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listaNome.append(input("Digite um número de telefone com código do país (ex: +5511999999999): "))
        elif opcao == "2":
            listaMensagens.append(msgperson())
        elif opcao == "3":
            print("\nMensagens personalizadas:")
            for i, msg in enumerate(listaMensagens, 1):
                print(f"{i}. {msg}")
        elif opcao == "4":
            for nome in listaNome:
                for mensagem in listaMensagens:
                    enviar_mensagem(nome, mensagem)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicializa listas vazias para armazenar os nomes e mensagens
listaNome = []
listaMensagens = []

# Chama a função menu para interagir com o usuário
menu(listaNome, listaMensagens)

