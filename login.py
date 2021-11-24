print(13*'=' + '\nVAMOS COMEÇAR\n' + 13*'=')

option = ''
while option != '1' and option != '2':
    option = input((f'Deseja começar?\n1 - Para sim\n2 - Para não\nInsira aqui: '))
    #Ensina/relembra como jogar antes de continuar
    if option == '1':
        print('''Pronto!\nAgora vamos aprender a jogar: \n
        Neste jogo, nós vamos aprender sobre alguns dos elementos básicos que formam as sentenças do português.\n
        Você só precisa arrastar as imagens para os seus lugares correspondentes nas sentenças.\n
        Vamos aprender brincando!\n''')
    #Encerra a aplicação
    elif option == '2':
        print('Até mais!')
        exit()
    #No caso do usuário inserir alguma opção inválida
    else:
        print('Não entendi o que você informou... \n\nPor favor tente novamente')
