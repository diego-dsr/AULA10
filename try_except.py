try:
    def soma(a,b):
        res = a + b
        #print(f"o resultado do primeiro calculo é: {res}")
        if i in soma % 2 ==0:
             print("Número Impar")
        else:
            return "impar"
    
        return res
    
    resultado1 = soma(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
    print(F"o resultado do primeiro calculo é {soma(a,b)}")
    
except ZeroDivisionError:
    print("Não e possível dividir por ZERO ")
    
except ValueError:
    print("Apenas valores inteiros!")

else:
    print("Soma feita!")

finally:
    print("Fim da operação")