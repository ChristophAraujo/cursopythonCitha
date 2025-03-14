import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados diretamente do arquivo CSV
dados = pd.read_csv(r'dados.csv')

# Remover espaços extras nos nomes das colunas
dados.columns = dados.columns.str.strip()

# Filtrar os dados para os anos mais recentes disponíveis (por exemplo, últimos 5 anos)
anos_recentes = dados['Year'].unique()[-5:]
dados_anos_recentes = dados[dados['Year'].isin(anos_recentes)]

# Agrupar os dados por país e ano, e somar os valores
dados_agrupados = dados_anos_recentes.groupby(['Area', 'Year'])['Value'].sum().reset_index()

# Plotar o gráfico de barras agrupadas
plt.figure(figsize=(14, 8))
sns.barplot(x='Area', y='Value', hue='Year', data=dados_agrupados, palette='viridis')

# Ajustar o título e rótulos
plt.title('População Trabalhando')
plt.xlabel('País')
plt.ylabel('População (em milhares)')

# Rotacionar os rótulos do eixo x para melhor legibilidade
plt.xticks(rotation=45)

# Ajustar a legenda para evitar que ela seja cortada
plt.legend(title='Ano', bbox_to_anchor=(1.05, 1), loc='upper left')

# Exibir o gráfico
plt.tight_layout()
plt.show()
