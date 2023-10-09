#Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X. Armazenar em um vetor M o resultado decada elemento de A multiplicado pelovalor X. Logo após, imprimir o vetor M.
a = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    a.append(numero)

x = float(input("Digite o valor que vc quer multiplicar: "))

m = [a * x for a in a]

print("O vetor m é:", m)
