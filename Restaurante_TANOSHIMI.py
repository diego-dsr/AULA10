menu = {
    1: ("Nigiri (dupla)", 15),
    2: ("Uramaki (8 peças)", 40),
    3: ("Gunkan (dupla)", 20),
    4: ("Hossomaki (8 peças)", 30),
    5: ("Sashimi (Porção)", 50),
    6: ("Temaki (Unidade)", 30)
}

# EXIBIR MENU
def exibir_menu():
    print("=" * 36)
    print("CARDÁPIO DO RESTAURANTE TANOSHIMI")
    print("=" * 36)

    for opcao, (item, valor) in menu.items():
        print(f"{opcao}. {item:<20} R$ {valor:>6.2f}")
        print("_" * 36)


# REGISTRAR PEDIDOS

def registrar_pedidos():
    registro = []
    total = 0

    while True:
        opcao = input(
            "Qual item você quer? (Digite o número ou 'sair' para terminar): "
        )

        if opcao.lower() == "sair":
            break

        try:
            opcao = int(opcao)
        except ValueError:
            print("Digite apenas números ou 'sair'.")

        if opcao in menu:
            item, valor = menu[opcao]
            registro.append((item, valor))
            total += valor
            print(f"Subtotal: R$ {total:.2f}")
        else:
                print("Item inválido!")

        

    return registro, total


# CALCULAR E IMPRIMIR A CONTA
def calcular_conta(registro, total):
    gorjeta = total * 0.10
    total_gorjeta = total + gorjeta

    print("=" * 36)
    print(f'{" " * 14}CONTA')
    print("_" * 36)

    for item, preco in registro:
        print(f"{item:<20} R$ {preco:>6.2f}")

    print("_" * 36)
    print(f"Conta total sem gorjeta: R$ {total:.2f}")
    print(f"Conta total com 10%:     R$ {total_gorjeta:.2f}")
    print("=" * 36)


# PROGRAMA PRINCIPAL
exibir_menu()
registro, total = registrar_pedidos()
calcular_conta(registro, total)