import random

subjects = {'subjects01':'CARLOS', 'subjects02':'MATHEUS', 'subjects03':'ANA'}
verbs = {'verbs01':'COMEU', 'verbs02':'AMA', 'verbs03':'COMPROU'}
objects = {'objects01':'MAÇÃ', 'objects02':'PIZZA', 'objects03':'FEIJÃO'}

dictionaries = [subjects, verbs, objects]

#Faz o código rodar o quanto o usuário quiser
continue_exercise = 1
while continue_exercise == 1:
    #Gera a frase correta
    answer_correct = []
    for i in range(0, 3):
        answer_correct.append(f'{dictionaries[i][random.choice(list(dictionaries[i]))]}')

    print(answer_correct)

    #Recebe os inputs do usuário e os valida
    for i in range(0, 3):
        answer_user = ''
        
        #Enquanto a resposta do usuário for diferente da palavra em questão, rodará o código
        while answer_user != answer_correct[i]:
            answer_user = input('Insira a senha da imagem: ')
            
            #Foi utilizado o try porque tentar achar uma chave inexistente ocasiona KeyError
            try:
                if dictionaries[i][answer_user] == answer_correct[i]:
                    answer_user = answer_correct[i]
                    print('Você acertou!')
            except KeyError:
                print('Não entendi o que você digitou, tente novamente')
    
    #Permite o usuário encerrar quando estiver satisfeito
    continue_exercise = int(input('Deseja continuar?\nDigite 1 para continuar\nDigite 2 para parar\nResponda aqui: '))
