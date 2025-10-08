from datetime import datetime

ano_atual = datetime.now().year

print("=" * 50)
print("VERIFICADOR DE MAIORIDADE")
print("=" * 50)

ano_nascimento = int(input("Digite o ano em que voce nasceu: "))

idade = ano_atual - ano_nascimento

print("\n" + "=" * 50)

if idade == 18:
    print(f"Voce fará ou já fez 18 anos em {ano_atual}!")
    print("Bem-vindo(a) á maioridade! ")
elif idade > 18:
    anos_passados = idade - 18
    print(f"Voce já completou 18 anos!")
    print(f"voce tem {idade} anos em {ano_atual}.")
    print(f"Voce completou 18 anoa há {anos_passados} ano(s).")
else:
    anos_faltando = 18 - idade
    anos_maioridade = ano_atual + anos_faltando
    print(f"Voce ainda nao tem 18 anos.")
    print(f"Voce tem {idade} anos em {ano_atual}.")
    print(f"Voce completará 18 anos em {anos_maioridade}.")

    print("=" * 50) 