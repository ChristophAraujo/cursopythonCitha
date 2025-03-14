import pandas as pd

dadosProdutos = pd.read_csv("arquivos.csv")
indice = dadosProdutos['preco'].idxmax()
produto_maior_preco = dadosProdutos.loc[indice, "produto"]
preco = dadosProdutos.loc[indice, "preco"]

print("produto com maior quantidade: ", produto_maior_preco, "com", preco, "unidades")