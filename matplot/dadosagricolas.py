import pandas as pd
import matplotlib.pyplot as plt

# Função para obter a maior produtividade
def max_produtividade(dados_produto):
    return dados_produto['produtividade'].max()

# Lendo o arquivo CSV
dados_produtos = pd.read_csv('dadosagricolas.csv', delimiter=',')
#criando grafico de preço por ano para cada produto
plt.figure(figsize=(10,6))

#plotando os dados oara cada produto
for infos in dados_produtos['tipoCultivo'].unique():#.unique especifica algo unico
    dados_produto = dados_produtos[dados_produtos['tipoCultivo'] == infos]
    #plt.plot cria a imagem do grafico
    plt.plot(dados_produto['ano'], dados_produto['produtividade'], label= infos, marker ='o')

#adicionando titulos e rotulos
plt.title('Produtividade Media por 3 anos')
plt.xlabel('Tipo de Cultivo')
plt.ylabel('Produtividade')
plt.legend(title = 'Cultivos')

# Obtendo a maior produtividade
maior_produtividade = max_produtividade(dados_produtos)
print(f"A maior produtividade é: {maior_produtividade}")

   



#exibindo o grafico

plt.grid(True)
plt.show()

