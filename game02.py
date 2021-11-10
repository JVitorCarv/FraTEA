import random

subjects = {'CARLOS':'subjects01', 'MATHEUS':'subjects02', 'ANA':'subjects03'}
verbs = {'COMEU':'verbs01', 'GOSTA DE':'verbs02', 'COMPROU':'verbs03'}
objects = {'MAÇÃ':'objects01', 'PIZZA':'objects02', 'FEIJÃO':'objects03'}

#Recebe o value informado pelo usuário e o respectivo dicionário aonde esse value será buscado
def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key #Retorna o nome da pessoa caso esse id seja achado na key
        elif val == 'sair':
            return 'SAIR'
        
    return '(id inválido)'

loop = True
while loop == True:
    answer_user = 0
    
    #Pega as keys dos respectivos dicionários e os transforma numa lista para serem escolhidos pelo random.choice
    answer_correct = (f'{random.choice(list(subjects.keys()))} {random.choice(list(verbs.keys()))} {random.choice(list(objects.keys()))}')
    
    #Repetirá o processo sempre que a resposta estiver incorreta
    while answer_user != answer_correct:    
        print(answer_correct)

        answer_user_subject = input('Digite o id correspondente à imagem do sujeito: ').lower()
        answer_user_verb = input('Digite o id correspondente à imagem do verbo: ').lower()
        answer_user_object = input('Digite o id correspondente à imagem do objeto: ').lower()

        #Recebe cada resposta do usuário, jogadas na função get_key para receber os nomes correspondentes ao ids
        answer_user = (f'{get_key(answer_user_subject, subjects)} {get_key(answer_user_verb, verbs)} {get_key(answer_user_object, objects)}')
        print(answer_user)
        
        if answer_user == answer_correct:
            print('Sua resposta está correta')
        elif 'SAIR' in answer_user:
            loop = False
            break
        else:
            print('Tente novamente')
