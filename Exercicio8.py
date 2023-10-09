#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação,imprimir , nome, senha e posição dos dados no array
nomes = []
senhas = []

for i in range(5):
    nome = input(f"Digite o nome do usuário {i+1}: ")
    senha = input(f"Digite a senha do usuário {i+1}: ")
    nomes.append(nome)
    senhas.append(senha)

print("Dados armazenados:")
for i in range(5):
    print(f"posição {i+1}: nome de usuário: {nomes[i]}, senha: {senhas[i]}")
