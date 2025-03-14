import pandas as pd
import matplotlib.pyplot as plt
# Lendo o arquivo CSV
dados_produtos = pd.read_csv('produtos.csv', delimiter=',')
#criando grafico de preço por ano para cada produto
plt.figure(figsize=(10,6))

#plotando os dados oara cada produto
for produto in dados_produtos['produtos'].unique():#.unique especifica algo unico
    dados_produto = dados_produtos[dados_produtos['produtos'] == produto]
    #plt.plot cria a imagem do grafico
    plt.plot(dados_produto['ano'], dados_produto['preco'], label=produto, marker ='o')

#adicionando titulos e rotulos
plt.title('Preço dos produtos ao longo dos anos')
plt.xlabel('ano')
plt.ylabel('preco')
plt.legend(title = 'produto')

#exibindo o grafico

plt.grid(True)
plt.show()