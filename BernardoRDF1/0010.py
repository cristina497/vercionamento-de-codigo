numeros = [3,7,10,1,2,0,42,51]
print("Lista de números",numeros)
numero_usuario = int(input("Digite o número para verificar se está na lista:"))
if numero_usuario in numeros:
    print(f"o numero{numero_usuario}esta na lista!,sim")
else:
    print(f" o numero {numero_usuario}nao esta na lista!,não")   
