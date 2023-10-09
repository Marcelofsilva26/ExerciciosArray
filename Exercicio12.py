#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, umpor linha.
nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("Nomes na ordem original:")
for nome in nomes:
    print(nome)

print("Nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
