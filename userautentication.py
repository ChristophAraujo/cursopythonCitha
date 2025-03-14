#função idade maior
def idadeMaior(login, senha):
    return login == loginsec and senha == senhasec

#Entrada de dados
login = str(input("Login: "))
senha = str(input("Senha: "))

loginsec = "Christoph"
senhasec = "123456"

#chamando a função
idadeMaior(login, senha)
#saida de dados
print(idadeMaior(login, senha))