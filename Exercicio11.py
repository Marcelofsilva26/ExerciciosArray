#Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.
vetor = []
for i in range(30):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)


numeroprocurado = float(input("Digite um número para buscar no vetor: "))


contador = 0
for numero in vetor:
    if numero == numeroprocurado:
        contador += 1


print(f"O número {numeroprocurado} aparece {contador} vezes no vetor.")
