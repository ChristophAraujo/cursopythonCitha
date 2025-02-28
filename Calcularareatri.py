#calcular area do triangulo


def calcularAreadoTriangulo(base, altura):
    area = (base * altura) / 2
    print("Area do triangulo: ", area)

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor de Altura: "))


calcularAreadoTriangulo(base, altura)