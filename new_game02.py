import random

subjects = ['CARLOS', 'MATHEUS', 'ANA']
verbs = ['COMEU', 'AMA', 'COMPROU']
objects = ['MAÇÃ', 'PIZZA', 'FEIJÃO']

lists = [subjects, verbs, objects]

#Faz o código rodar o quanto o usuário quiser
continue_exercise = 1
while continue_exercise == 1:
    #Gera a frase correta
    answer_correct = []
    for i in range(0, 3):
        answer_correct.append(f'{random.choice(lists[i])}')

    print(answer_correct)
    
    answer_shuffle = []
    for word in answer_correct:
        answer_shuffle.append(word)
    random.shuffle(answer_shuffle)

    #Recebe os inputs do usuário e os valida
    for i in range(0, 3):
        print(answer_shuffle[i])
        answer_user = ''
        
        is_correct = False
        #Enquanto a resposta do usuário for diferente da palavra em questão, rodará o código
        while is_correct == False:
            answer_user = int(input('Informe a posição na frase: '))
            try:    
                if answer_shuffle[i] == answer_correct[answer_user-1]:
                    print('Acertou')
                    is_correct = True
            except IndexError:
                print('Por favor informe um valor de 1 a 3')

    #Permite o usuário encerrar quando estiver satisfeito
    continue_exercise = int(input('Deseja continuar?\nDigite 1 para continuar\nDigite 2 para parar\nResponda aqui: '))
