#declarar variaveis
qtdimpar = 0
qtdpar = 0
#for para pedir numero solicitado de numeros
for i in range(5):
    numeros = int(input("Digite um numero: "))
    #estruturas condicionais para saber se é par ou impar
    if numeros % 2 == 0:
        qtdpar += 1
    else:
        qtdimpar += 1
#print para telas
print(f"QUuantidade de Pares: {qtdpar}")

print(f"QUuantidade de Impares: {qtdimpar}")
    