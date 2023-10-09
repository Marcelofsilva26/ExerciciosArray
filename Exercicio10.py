#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depoisa rmazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B(respeitando as mesmas posições) e escrever ovetor Soma.
n = int(input("Digite o tamanho dos vetores: "))
a = []
b = []
soma = []


print("Digite os valores para o vetor A:")
for i in range(n):
    valor = float(input(f"Digite o {i+1}º valor: "))
    a.append(valor)

print("\nDigite os valores para o vetor B:")
for i in range(n):
    valor = float(input(f"Digite o {i+1}º valor: "))
    b.append(valor)


for i in range(n):
    somaelemento = a[i] + b[i]
    soma.append(somaelemento)


print("O vetor Soma é:", soma)
