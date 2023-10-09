#Faça um código para ler 5 números e armazenar em um vetor. Após a leitur atotal dos 5 números, o código deve escrever esses 5 números lidos na ordeminversa.
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("Ordem inversa:")
for numero in reversed(numeros):
    print(numero)
