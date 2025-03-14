def contvogal(palavra):
    vogais = 'aeiou'
    cont = 0
    for letras in palavra:
        if letras in vogais:
            cont +=1
    return cont


palavra = str(input("Escreva uma palavra: "))


print(contvogal(cont))
