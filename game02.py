import random

subjects = {'CARLOS':'subject01', 'MATHEUS':'subject02', 'ANA':'subject03'}
verbs = {'COMEU':'verbs01', 'GOSTA DE':'verbs02', 'COMPROU':'verbs03'}
objects = {'MAÇÃ':'objects01', 'PIZZA':'objects02', 'FEIJÃO':'objects03'}

#Pega as keys dos respectivos dicionários e os transforma numa lista para serem escolhidos pelo random.choice
answer_correct = (f'{random.choice(list(subjects.keys()))} {random.choice(list(verbs.keys()))} {random.choice(list(objects.keys()))}')

print(answer_correct)
