# Inicializa a lista de transações e o saldo
transacoes = []
saldo = 0

print("Digite as transações uma por vez. Quando terminar, digite 'fim'.")

# Solicita ao usuário que insira as transações uma por vez
while True:
    entrada = input("Digite uma transação (ex: 100 ou -50): ")
    if entrada.lower() == 'fim':  # Verifica se o usuário terminou de inserir
        break
    try:
        transacao = float(entrada)  # Converte a entrada para float
        transacoes.append(transacao)  # Adiciona à lista de transações
    except ValueError:
        print("Entrada inválida. Por favor, insira um número ou 'fim' para terminar.")

# Calcula o saldo somando todas as transações
for transacao in transacoes:
    saldo += transacao

# Formata o saldo em moeda brasileira com duas casas decimais
resultado = f"Saldo: R$ {saldo:.2f}"

# Imprime o resultado
print("\nTransações registradas:", transacoes)
print(resultado)
