#Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e mostrando seu nome e a mensagem, login efetuado com sucesso.
usuarios = {}

for i in range(5):
    nome = input(f"Digite o nome do usuário {i+1}: ")
    senha = input(f"Digite a senha do usuário {i+1}: ")
    usuarios[nome] = senha

usuariologin = input("Digite seu nome de usuário: ")
senhalogin = input("Digite sua senha: ")


if usuariologin in usuarios and usuarios[usuariologin] == senhalogin:
    print(f"Login efetuado com sucesso. Bem-vindo {usuariologin}!")
else:
    print("Nome de usuário ou senha incorretos. Tente novamente.")
