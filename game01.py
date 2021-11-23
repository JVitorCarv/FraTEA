#Utilizamos a biblioteca random para escolhermos "imagens" das listas
import random

list_pictures = ['Imagem de maçã', 'Imagem de uva', 'Imagem de pera']

print('Bem vindo ao exercício! Para sair, informe "SAIR"')

answer_user = ''

#Enquanto a frase informada não for SAIR, o código monta a resposta
while answer_user != 'SAIR':
    picture = random.choice(list_pictures)
    answer_correct = picture.upper()
    answer_correct = answer_correct[10::]

    #Pede a entrada da frase enquanto for diferente da resposta e de SAIR
    #Se uma dessas condições não for satisfeita, o loop é quebrado
    while answer_user != answer_correct and answer_user != 'SAIR':
        print(picture)
        answer_user = str(input('O que é isso? '))
        answer_user = answer_user.upper() #a frase também muda para evitar case sensitivity

        #Dá um feedback de acordo com a resposta
        if answer_user == 'SAIR':
            print('Exercício encerrado')
        elif answer_user != answer_correct:
            print('A resposta ainda não tá correta... Tente novamente')
        else:
            print('A resposta está correta! Parabéns!')
