dados = open('arquivos.csv', 'r')
for j in dados:
    vogal = 0
    vogais = 'aeiouAEIOU'
    if vogais in dados:
        vogal = vogal + 1
    print(vogal)
dados.close()