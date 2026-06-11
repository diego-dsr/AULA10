def soma(a, b):
    res = a + b

    if res % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")

    return res


try:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    resultado1 = soma(a, b)

    print(f"O resultado do cálculo é {resultado1}")

except ValueError:
    print("Apenas valores inteiros!")

else:
    print("Soma feita!")

finally:
    print("Fim da operação")