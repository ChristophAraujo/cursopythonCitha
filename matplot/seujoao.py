import pandas as pd
import matplotlib.pyplot as plt

def maisRentavel():
    # Carregar os dados diretamente do arquivo CSV
    dados = pd.read_csv(r'seujoao.csv')

 # Remover espaços extras nos nomes das colunas
    dados.columns = dados.columns.str.strip()

    # Calcular a rentabilidade
    dados['rentabilidade'] = dados['vendas'] - (dados['customedio'] / dados['quantidade'])

    # Agrupar os dados por tipo de peixe e somar a rentabilidade
    rentabilidade_agrupada = dados.groupby('tipoPeixe')['rentabilidade'].sum().reset_index()

    # Ordenar os dados pela rentabilidade
    rentabilidade_agrupada = rentabilidade_agrupada.sort_values(by='rentabilidade', ascending=False)

    # Mostrar o tipo de peixe mais rentável
    mais_rentavel = rentabilidade_agrupada.iloc[0]
    print(f'Tipo de peixe mais rentável: {mais_rentavel["tipoPeixe"]} com rentabilidade de {mais_rentavel["rentabilidade"]:.2f}')



# Carregar os dados diretamente do arquivo CSV
dados = pd.read_csv(r'seujoao.csv')

# Remover espaços extras nos nomes das colunas
dados.columns = dados.columns.str.strip()

# Agrupar os dados por tipo de peixe e somar as vendas
dados_agrupados = dados.groupby('tipoPeixe')['vendas'].sum().reset_index()

# Configura o tamanho da figura do gráfico
plt.figure(figsize=(8, 8))

# Cria um gráfico de pizza
# - vendas: valores a serem representados no gráfico
# - labels: rótulos para cada fatia do gráfico
# - autopct: formato para exibir os valores percentuais
# - startangle: ângulo inicial para a primeira fatia
plt.pie(dados_agrupados['vendas'], labels=dados_agrupados['tipoPeixe'], autopct='%1.1f%%', startangle=90)

# Define o título do gráfico
plt.title('Vendas por Tipo de Peixe')




# Exibe o gráfico
plt.show()
maisRentavel()