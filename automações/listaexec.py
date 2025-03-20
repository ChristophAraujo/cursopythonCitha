import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
from plyer import notification  # Importa a biblioteca plyer para enviar notificações

# Função para ler e analisar o arquivo CSV
def ler_analisar_csv():
    # Lê o arquivo CSV chamado "vendas.csv" e armazena os dados em um DataFrame
    df = pd.read_csv("arquivo.csv")
    
    # Cria uma nova coluna 'Total', que é o resultado da multiplicação de 'Quantidade' pelo 'Preço'
    df['total'] = df['quantidade'] * df['preco']
    
    # Agrupa os dados por 'Produto' e calcula a soma total para cada produto
    total_por_produto = df.groupby('produto')['total'].sum()
    
    # Identifica o produto mais vendido (aquele com o maior total)
    produto_mais_vendido = total_por_produto.idxmax()
    
    # Calcula o total geral de vendas (soma de todos os produtos)
    total_geral = total_por_produto.sum()
    
    # Retorna o DataFrame original, o total por produto, o produto mais vendido e o total geral
    return df, total_por_produto, produto_mais_vendido, total_geral

# Função para enviar notificação com o resumo de vendas
def enviar_notificacao(produto_mais_vendido, total_geral):
    notification.notify(
        title="Resumo de Vendas",
        message=f"Produto mais vendido: {produto_mais_vendido}\nTotal geral: R${total_geral:.2f}",
        timeout=10  # Tempo em segundos para exibir a notificação
    )

# Chama a função para executar a análise
df, total_por_produto, produto_mais_vendido, total_geral = ler_analisar_csv()

# Exibe os resultados da análise
print("Análise de Vendas:")
print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Total geral de vendas: R${total_geral:.2f}")

# Envia a notificação com o resumo de vendas
enviar_notificacao(produto_mais_vendido, total_geral)

