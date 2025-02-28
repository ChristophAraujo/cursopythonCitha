reais = float(input("DIgite um valor em R$:"))

dollar = float(input("digite a taxa de conversao  em $:  "))

convert = reais/ dollar

print(f"O valor em R$ foi R${reais}\n A taxa do dollar é {dollar}\n O valor convertido é ${convert:.2f}")