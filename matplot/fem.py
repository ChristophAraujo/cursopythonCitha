import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados diretamente do arquivo CSV
dados = pd.read_csv(r'fem.csv')

# Remover espaços extras nos nomes das colunas
dados.columns = dados.columns.str.strip()

# Filtrar os dados para os anos desejados (por exemplo, 2020 e 2021)
dados_2023 = dados[dados['ano'] == 2023]
dados_2024 = dados[dados['ano'] == 2024]

# Somar os valores de cada categoria para 2020
total_violencia_2023 = dados_2023['casosViolencia'].sum()
total_feminicidio_2023 = dados_2023['feminicidio'].sum()

# Somar os valores de cada categoria para 2021

total_violencia_2024 = dados_2024['casosViolencia'].sum()
total_feminicidio_2024 = dados_2024['feminicidio'].sum()

# Dados para os gráficos de pizza
labels = ['Violência', 'Feminicídio']
sizes_2023 = [total_violencia_2023, total_feminicidio_2023]
sizes_2024 = [total_violencia_2024, total_feminicidio_2024]
colors = ['blue', 'red']

# Configura o tamanho da figura do gráfico
plt.figure(figsize=(16, 8))

# Cria o gráfico de pizza para 2020
plt.subplot(1, 2, 1)
plt.pie(sizes_2023, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribuição de Violência por Feminicídio em 2023')

# Cria o gráfico de pizza para 2021
plt.subplot(1, 2, 2)
plt.pie(sizes_2024, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribuição de Violência por Feminicídio em 2024')
plt.figtext(0.5, 0.01, 'Fonte = G1, CNN, Google', wrap=True, horizontalalignment='center', fontsize=12)
# Ajustar o layout para não cortar os gráficos
plt.tight_layout()

# Exibir os gráficos
plt.show()