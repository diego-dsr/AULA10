try:
    def soma(a,b):
        res = a + b
            
        return res
    
    
    
    
except ZeroDivisionError:
    print("Não e possível dividir por ZERO ")
    
except ValueError:
    print("Apenas Valores inteiros ")
else:
      print(f"Soma Feita! ")
finally:
        print ("Fim da Operação")


""" def par_ou_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

num = int(input("Entre com o número: "))
print(f"Numero {num} é {par_ou_impar(num)}")
 """
""" def calcular_soma(num1, num2):
    resultado = num1 + num2
    return resultado

resultado1 = calcular_soma(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
resultado2 = calcular_soma(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
resultado3 = calcular_soma(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))

print(F"o resultado do primeiro calculo é: {resultado1}")
print(F"o resultado do segundo calculo é: {resultado2}")
print(F"o resultado do terceiro calculo é: {resultado3}") """