#Escrevendo em um arquivo
#Crie um programa que pede ao usuário um nome e uma idade e salva esses dados em um arquivo dados.txt

arquivo = open("contatos.txt", "r")
for linha in arquivo:
    print(linha)
arquivo.close()

arquivo = open("contatos.txt", "w")
arquivo.write("\nJOSE")
arquivo.close()


arquivo2 = 