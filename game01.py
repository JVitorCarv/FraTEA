#Utilizamos a biblioteca random para escolhermos palavras das listas
import random

list_subjects = ['Rodrigo', 'Eduarda', 'Luiz']
list_verbs = ['come', 'gosta de']
list_objects = ['maçã', 'uva', 'pera']

print('Bem vindo ao exercício! Para sair, informe "SAIR"')

answer_user = ''

#Enquanto a frase informada não for SAIR, o código monta a resposta
while answer_user != 'SAIR':
    subject = random.choice(list_subjects)
    print(subject)

    verb = random.choice(list_verbs)
    print(verb)

    object = random.choice(list_objects)
    print(object)
    
    answer_correct = str(subject + ' ' + verb + ' ' + object)
    answer_correct = answer_correct.upper() #dessa forma, a resposta não é case sensitive

    #Pede a entrada da frase enquanto for diferente da resposta e de SAIR
    #Se uma dessas condições não for satisfeita, o loop é quebrado
    while answer_user != answer_correct and answer_user != 'SAIR':
        answer_user = str(input('Informe a frase: '))
        answer_user = answer_user.upper() #a frase também muda para evitar case sensitivity

        #Dá um feedback de acordo com a resposta
        if answer_user == 'SAIR':
            print('Exercício encerrado')
        elif answer_user != answer_correct:
            print('A resposta ainda não tá correta... Tente novamente')
        else:
            print('A resposta está correta! Parabéns!')