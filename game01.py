import random
import time

subjects = ['CARLOS', 'MATHEUS', 'MARIA']
verbs = ['COMEU', 'ADORA', 'COMPROU']
objects = ['MAÇÃ', 'PIZZA', 'FEIJÃO']

lists = [subjects, verbs, objects]

listsCampos=[]

#Faz o código rodar o quanto o usuário quiser
continue_exercise = '1'
while continue_exercise != '2':
    #Gera a frase correta
    answer_correct = []
    for i in range(0, 3):
        answer_correct.append(f'{random.choice(lists[i])}')

    print(f"\n======FRASE======\n|   {answer_correct[0]}\t|\n|   {answer_correct[1]}\t|\n|   {answer_correct[2]}\t|\n=================")
    print(f"\t\  /\n\t \/\t\t")
    print(f"===CORRELAÇÃO====\n| SUJEITO  - 1\t|\n| VERBO\t   - 2\t|\n| OBJETO   - 3\t|\n=================")

    answer_shuffle = []
    for word in answer_correct:
        answer_shuffle.append(word)
    random.shuffle(answer_shuffle)

    #Recebe os inputs do usuário e os valida
    for i in range(0, 3):
        print(f"Agora é a vez da palavra: {answer_shuffle[i]}")
        answer_user = ''
        
        is_correct = False
        #Enquanto a resposta do usuário for diferente da palavra em questão, rodará o código
        while is_correct == False:
            is_valid = False
            while is_valid == False:
                try:
                    answer_user = int(input('\tInforme a posição na frase: '))
                    is_valid = True
                except ValueError:
                    print('Não entendi o que você digitou')
                except TypeError:
                    print('Não entendi o que você digitou')
            try:    
                if answer_shuffle[i] == answer_correct[answer_user-1]:
                    if answer_user == 1:
                        campo = "sujeito"
                    elif answer_user == 2:
                        campo = "verbo"
                    elif answer_user == 3:
                        campo = "objeto"
                    print('Parabens!! Você acertou!')
                    print(f'\tA palavra {answer_shuffle[i]} é o {campo.upper()}({answer_user}) desta frase! \n')                    
                    is_correct = True
                else:
                    print('Essa não é a resposta certa... Tente novamente')
            except IndexError:
                print('Por favor informe um valor de 1 a 3')

    #Permite o usuário encerrar quando estiver satisfeito
    print('Parabéns! Você acertou todos os elementos da frase!!\n')
    time.sleep(0.5)
    
    #O valor de continue_exercise é resettado para poder dar escolha ao usuário
    continue_exercise = '3'
    while continue_exercise != '1' and continue_exercise != '2':
        continue_exercise = input('Deseja continuar?\n\tDigite 1 para continuar\n\tDigite 2 para parar\nResponda aqui: ')
        if continue_exercise == '1':
            print('Vamos continuar!\n')
        elif continue_exercise == '2':
            print('\nMuito obrigado por brincar com a gente!\nAté mais!')
        else:
            print('Não entendi o que você digitou...\nTente novamente\n')
