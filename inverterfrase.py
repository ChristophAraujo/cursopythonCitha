#FUNCAO INVERTER
def inverterstr(texto):
    return texto[::-1]#INVERTE AS STRINGS

#ENTRADA DE STRING
texto = str(input("escreva uma frase: "))
#SAIDA NA TELA
print("frase invertida: ", inverterstr(texto))