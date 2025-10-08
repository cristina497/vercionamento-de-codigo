idade = int(input("Digite sua idade:"))
if idade < 0:
    print("Idade invalida.")
elif idade <=11:
    print("Classificacao: Criança")
elif idade <= 18:
    print("Classificaçao: Adolescente")
elif idade <= 24:
    print("Classificaçao: Jovem")
elif idade <= 40:
    print(" Clasificaçao: Adulto")
elif idade <= 60:
    print("Classificaçao: Meia Idade")
else:
    print("Classificaçao: Idoso")    