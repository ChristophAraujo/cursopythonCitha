import pandas as pd

# Substitua 'caminho_para_seu_arquivo.csv' pelo caminho real do seu arquivo CSV
caminho_arquivo_csv = 'dadosagricolas.csv'

# Leitura do arquivo CSV
dados = pd.read_csv(caminho_arquivo_csv)

# Exibição dos dados
print(dados)

# Encontrar o produto com a maior produtividade
produto_maior_produtividade = dados.loc[dados['produtividade'].idxmax()]

print(f"Produto com maior produtividade: {produto_maior_produtividade['produto']}")
print(f"Produtividade: {produto_maior_produtividade['produtividade']}")
