# Importa as bibliotecas necessárias
import tkinter as tk  # Para criar a interface gráfica
from tkinter import messagebox  # Para exibir mensagens de erro
import pyautogui  # Para exibir alertas na tela
import threading  # Para executar tarefas em threads separadas
import time  # Para manipular o tempo (ex.: sleep)

# Função para criar o lembrete
def criar_lembrete():
    # Obtém os valores inseridos pelo usuário
    mensagem = entrada_mensagem.get()  # Mensagem do lembrete
    tempo = entrada_tempo.get()  # Tempo em segundos

    # Verifica se os campos estão preenchidos corretamente
    if not mensagem or not tempo.isdigit():
        # Exibe uma mensagem de erro se os dados forem inválidos
        messagebox.showerror("Erro", "Por favor, insira uma mensagem e um tempo válido (em segundos).")
        return

    # Converte o tempo para inteiro
    tempo = int(tempo)
    # Cria uma nova thread para executar o lembrete sem travar a interface
    threading.Thread(target=mostrar_lembrete, args=(mensagem, tempo)).start()

# Função para exibir o lembrete após o tempo especificado
def mostrar_lembrete(mensagem, tempo):
    time.sleep(tempo)  # Aguarda o tempo especificado
    # Exibe o lembrete em uma janela de alerta
    pyautogui.alert(text=mensagem, title="Lembrete", button="OK")

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela principal
janela.title("Criador de Lembretes")  # Define o título da janela

# Adiciona os widgets (elementos da interface)
tk.Label(janela, text="Mensagem do Lembrete:").pack(pady=5)  # Rótulo para a mensagem
entrada_mensagem = tk.Entry(janela, width=40)  # Campo de entrada para a mensagem
entrada_mensagem.pack(pady=5)

tk.Label(janela, text="Tempo (em segundos):").pack(pady=5)  # Rótulo para o tempo
entrada_tempo = tk.Entry(janela, width=10)  # Campo de entrada para o tempo
entrada_tempo.pack(pady=5)

# Botão para criar o lembrete
botao_criar = tk.Button(janela, text="Criar Lembrete", command=criar_lembrete)
botao_criar.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()