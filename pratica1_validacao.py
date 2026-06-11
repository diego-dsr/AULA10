
def soma(a,b):
        res = a + b
        if a % 2 ==0:
             print("Número Par")
        else:
            return "impar"
        if b % 2 ==0:
             print("Número Par")
        else:
            return "impar"
    
        return res
a = (int(input("Digite o primeiro numero: ")))
b = (int(input("Digite o segundo numero: ")))
print(f"o {a} é {soma(a,b)}")
