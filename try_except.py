try:
    
    def soma(a,b):
        print(a + b)
        return a + b
    
    soma (int(input("Numero ")), int(input("Numero "))) 
except ZeroDivisionError:
    print("Não e possível dividir por ZERO ")
    
except ValueError:
    print("Apenas Valores inteiros ")
else:
      print(f"Soma Feita! ")
finally:
        print ("Fim da Operação")
