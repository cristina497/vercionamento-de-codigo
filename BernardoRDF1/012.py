def calcular_marmitas(estoque_arroz, estoque_feijao, estoque_carne, estoque_salada):
    # Quantidade de insumos necessários para cada marmita
    arroz_por_marmita = 100
    feijao_por_marmita = 50
    carne_por_marmita = 25
    salada_por_marmita = 10

    # Calcular o número máximo de marmitas que podem ser feitas com o estoque atual
    marmitas_possiveis_arroz = estoque_arroz // arroz_por_marmita
    marmitas_possiveis_feijao = estoque_feijao // feijao_por_marmita
    marmitas_possiveis_carne = estoque_carne // carne_por_marmita
    marmitas_possiveis_salada = estoque_salada // salada_por_marmita

    # O número máximo de marmitas é limitado pelo insumo que acabar primeiro
    marmitas_possiveis = min(marmitas_possiveis_arroz, marmitas_possiveis_feijao, marmitas_possiveis_carne, marmitas_possiveis_salada)

    return marmitas_possiveis

def atualizar_estoque(estoque_arroz, estoque_feijao, estoque_carne, estoque_salada, marmitas_vendidas):
    # Quantidade de insumos para cada marmita
    arroz_por_marmita = 100
    feijao_por_marmita = 50
    carne_por_marmita = 25
    salada_por_marmita = 10

    # Atualizar o estoque
    estoque_arroz -= arroz_por_marmita * marmitas_vendidas
    estoque_feijao -= feijao_por_marmita * marmitas_vendidas
    estoque_carne -= carne_por_marmita * marmitas_vendidas
    estoque_salada -= salada_por_marmita * marmitas_vendidas

    return estoque_arroz, estoque_feijao, estoque_carne, estoque_salada

def exibir_estoque(estoque_arroz, estoque_feijao, estoque_carne, estoque_salada):
    print("\nEstoque Atual:")
    print(f"Arroz: {estoque_arroz}g")
    print(f"Feijão: {estoque_feijao}g")
    print(f"Carne: {estoque_carne}g")
    print(f"Salada: {estoque_salada}g")
    print("-" * 30)

def main():
    # Entrada inicial de estoque
    estoque_arroz = int(input("Digite a quantidade de arroz disponível (em gramas): "))
    estoque_feijao = int(input("Digite a quantidade de feijão disponível (em gramas): "))
    estoque_carne = int(input("Digite a quantidade de carne disponível (em gramas): "))
    estoque_salada = int(input("Digite a quantidade de salada disponível (em gramas): "))

    while True:
        # Calcular o número de marmitas possíveis de serem feitas
        marmitas_possiveis = calcular_marmitas(estoque_arroz, estoque_feijao, estoque_carne, estoque_salada)

        # Exibir estoque e número de marmitas possíveis
        exibir_estoque(estoque_arroz, estoque_feijao, estoque_carne, estoque_salada)
        print(f"Você pode fazer {marmitas_possiveis} marmitas com o estoque atual.\n")

        if marmitas_possiveis > 0:
            marmitas_vendidas = int(input(f"Quantas marmitas foram vendidas (máximo {marmitas_possiveis}): "))
            if marmitas_vendidas <= marmitas_possiveis:
                # Atualizar o estoque com a venda
                estoque_arroz, estoque_feijao, estoque_carne, estoque_salada = atualizar_estoque(
                    estoque_arroz, estoque_feijao, estoque_carne, estoque_salada, marmitas_vendidas)
                
                print(f"{marmitas_vendidas} marmitas foram feitas com sucesso!")
            else:
                print(f"Você não pode vender mais de {marmitas_possiveis} marmitas!")
        else:
            print("Não há insumos suficientes para fazer mais marmitas.")
        
        continuar = input("Deseja continuar (s/n)? ")
        if continuar.lower() != 's':
            break

    print("\nSistema encerrado. Obrigado por usar!")
    
if __name__ == "__main__":
    main()