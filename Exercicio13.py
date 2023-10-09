#Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor. A seguir, o algoritmo deverá informar(1) todos os números pares que existem no vetor;(2) o menor e o maior valor existente no vetor;(3) quantos dos valores do vetor são maiores que a média desses valores:

valores = []


primeirovalor = int(input("Digite o 1º valor: "))
valores.append(primeirovalor)
menorvalor = primeirovalor
maiorvalor = primeirovalor


somavalores = primeirovalor
contagemmaioresquemedia = 0


for i in range(1, 30):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)


    if valor % 2 == 0:
        print(f"Valor par encontrado: {valor}")


    if valor < menorvalor:
        menorvalor = valor
    if valor > maiorvalor:
        maiorvalor = valor


    somavalores += valor


media = somavalores / 30


for valor in valores:
    if valor > media:
        contagemmaioresquemedia += 1


print("Menor valor no vetor:", menorvalor)
print("Maior valor no vetor:", maiorvalor)
print("Quantidade de valores maiores que a média:", contagemmaioresquemedia)
