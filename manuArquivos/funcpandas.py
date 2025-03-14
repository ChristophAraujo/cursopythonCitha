# imports
import pandas as pd
#leitura de arquivo
dadosProdutos = pd.read_csv(r'D:\Python\pythoncurso\manuArquivos\arquivos.csv')
#verificando precos
dadosProdutos [1:1].max()
#saida de tela
print("média de preços dos produtos ", dadosProdutos[1:2].mean())