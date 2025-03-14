def inverter(palavra):
    return palavra == palavra[::-1]




palavra = str(input("DIgite seu palindromo: "))
if inverter(palavra):
    print("è um palíndromo!")
else:
    print("Não é um palíndromo")