#declaração variavel
produto = float(input("Digite o Valor Unitário do Produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

#verificando a % de desconto
if  quantidade < 10:
    desconto = 0
elif quantidade < 20:
    desconto = 0.1
else:
    desconto = 0.2

#calculos de desconto
valor_sem_desconto = quantidade * produto
valor_com_desconto = quantidade * (1 - desconto)
valor_total = quantidade * valor_com_desconto
valor_desconto = quantidade * produto * desconto
porcentagem_desconto = desconto * 100

#saida na tela
print(f"valor total sem desconto: {valor_sem_desconto}")
print(f"valor Unitario: {produto}")
print(f"valor total com desconto: {valor_total:.2f} ({porcentagem_desconto} % de Desconto)")
print(f"valor total: {valor_total:.2f}(Desconto total {valor_desconto:.2f})")