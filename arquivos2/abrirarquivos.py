with open("arquivos.csv", "w", encoding="utf-8") as file:
    for i in range(3):
        frase = input(f'digite a {i+1}ª frase:')
        file.write(frase + "\n")
print("Frases salvadas com sucesso")
