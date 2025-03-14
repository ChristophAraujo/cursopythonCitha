"""""num = int(input("Digite um numero: "))
par = num % 2 == 0
if par:
    print(par)
else:
    print(par)
"""""


def eh_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um numero: "))

print(eh_par(numero))