import time  # Importa o módulo time para usar a função sleep

# Define a função lembrete_atividade que recebe um intervalo em minutos (padrão é 10 minutos)
def lembrete_atividade(intervalo_minutos=10):
    contador = 1  # Inicializa o contador de lembretes
    while True:  # Loop infinito para gerar lembretes periodicamente
        print(f"\nTempo encerrado (lembrete {contador})")  # Imprime a mensagem de lembrete com o número do contador
        contador += 1  # Incrementa o contador de lembretes
        time.sleep(intervalo_minutos * 60)  # Pausa a execução por 'intervalo_minutos' convertido para segundos

# Chama a função lembrete_atividade com o intervalo padrão de 10 minutos
lembrete_atividade()

