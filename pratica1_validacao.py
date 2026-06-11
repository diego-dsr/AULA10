
# Exceção personalizada
class NumeroImparError(Exception):
    pass

print("SOMATÓRIO SOMENTE DE NÚMEROS PARES")
# Função para somar e imprimir
def soma(a, b):
    print(f"Soma = {a + b}")


# Leitura de 3 pares de números
for i in range(3):
    try:
        print(f"\nPar {i+1}")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        # Verifica se algum número é ímpar
        if num1 % 2 != 0:
            raise NumeroImparError(f"{num1} é ímpar.")

        if num2 % 2 != 0:
            raise NumeroImparError(f"{num2} é ímpar.")

        soma(num1, num2)

    except ValueError:
        print("Erro: digite apenas números inteiros.")

    except NumeroImparError as erro:
        print("Erro:", erro)