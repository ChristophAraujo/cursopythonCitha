#dicionario é uma estrutura de dados mais completas e representa uma coleção de 48 dados que contem sua estruturas
# no qual cada chave individual  tem um valor associado
# 'Nome': 'Christoph'

"""""
#variaveis
produto = {'Nome':'feijao', 'quantidade':'10'}


#alteração
produto['quantidade'] = 100

#verificando 
nome = produto ['Nome']
quantidade = produto['quantidade']
#mostrando
print("Nome: ",nome)
print('quantidade: ', quantidade)



#percorrendo dict

for chave, valor in produto.items():
    print(chave,valor)


"""""

produto = {
    'Nome': ['feijao', 'arroz', 'farinha'],
    'Quantidade': [ 10, 10, 100 ],
    'preco': [8,6,5]
    }



for nome, quantidade, preco in zip (produto['Nome'], produto['Quantidade'], produto['preco']):
    print("Produto: ", nome, "\nQuantidade: ",quantidade, '\nPreço: ', preco)