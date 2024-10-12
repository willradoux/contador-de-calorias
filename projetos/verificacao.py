senha_correta = 'Monkey123'
tentativas = 3 

while tentativas > 0:
    senha = input('Digite a senha: ')
    if senha == senha_correta:
        print('Senha correta.')
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print('Senha incorreta, tente novamente.')
        else:
            print('Suas tentativas acabaram.') 