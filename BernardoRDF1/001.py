idade = int(input("Digite a sua idade:"))

if idade < 0:
    classificaçao = "Idade invalida."
elif idade <= 11:
    classificaçao = "Criança"
elif idade <=18:
    classificaçao = "Adolescente"
elif idade <=24:
    classificaçao = "jovem"
elif idade <= 40:
    classificaçao = "adulto"
elif idade <= 59:
    classificaçao = "idoso"
print (f"sua classificaçao etaria é: {classificaçao}")