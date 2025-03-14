import pandas as pd

dadosProdutos = pd.read_csv("arquivos.csv")
print(dadosProdutos.columns)

dadosProdutos['preco'].max()
print(f"Média de preços dos proutos ",dadosProdutos['preco'].mean())