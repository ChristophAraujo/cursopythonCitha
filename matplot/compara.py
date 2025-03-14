import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para criar gráficos

# Lista de países
paises = ['Argentina', 'Brasil']

# Lista de consumo de energia correspondente aos países
consumo = [100, 200]

# Configura o tamanho da figura do gráfico
plt.figure(figsize=(8, 8))

# Cria um gráfico de pizza
# - consumo: valores a serem representados no gráfico
# - labels: rótulos para cada fatia do gráfico
# - autopct: formato para exibir os valores percentuais
# - colors: cores para cada fatia do gráfico
# - startangle: ângulo inicial para a primeira fatia
plt.pie(consumo, labels=paises, autopct='%1.1f%%', colors=['blue', 'red'], startangle=90)

# Define o título do gráfico
plt.title('Consumo de Energia')

# Exibe o gráfico
plt.show()