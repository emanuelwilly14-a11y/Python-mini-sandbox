import random

senha = 1234

while True:
    senha_digitada = int(input('Digite a sua senha para entrar: '))

    if senha_digitada == senha:
        print("*" * 100)
        print('Senha correta. Seja bem-vindo ao sitema')
        print("*" * 100)
        break
    else:
        print('Senha incorreta')
        opcao = input('Esqueceu a sua senha? s/n: ').lower()

        match opcao:
            case "s":
                troca = random.randint(1000,9999)
                arquivo = open('Codigo.txt', 'w')
                arquivo.write(f"Digite o seguinte codigo para trocar de senha: {troca}")
                arquivo.close()

                codigo = int(input('Digite o codigo que te deram: '))

                if codigo == troca:
                    new_senha = int(input('Digite a tua nova senha: '))
                    senha = new_senha
                    print("-" * 100)
                    print(f'Senha trocada com sucesso. A sua nova senha é: {senha}')
                    print("-" * 100)
                else:
                    print('O codigo posto está incorreto')
            case "n":
                print('OK, então tente novamente')
            case _:
                print('Comando invalido digite apenas "s" para sim e "n" para não')
    