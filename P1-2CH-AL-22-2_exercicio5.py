#Código produzido para a segunda chamada da prova de Algoritmos II - IFC Campus Camboriú
#ALUNO: KAIAN VINICIUS (2022004420)

import numpy as np

est1 = []
est2 = []

tmh_est = int(input("Insira o tamanho que você deseja para a estrutura: "))

for valor in range(tmh_est):
    valor = float(input("Por favor, insira um valor para a primeira estrutura: "))
    est1.append(valor)
    
for valor in range(tmh_est):
    valor = float(input("Por favor, insira um valor para a segunda estrutura: "))
    est2.append(valor)

print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

print(f'A primeira e segunda estrutura ficaram - respectivamente - com os seguintes valores:\n{est1}\n{est2}')

#fazendo uma nova lista com os valores revertidos da ordem da est2, a est3

est3 = []

for valor in reversed(est2):
    est3.append(valor)

#transformando as estruturas em arrays

arry1 = np.array(est1)
arry2 = np.array(est3)

#subtraindo os arrays e armazenando o resultado como lista

sub_arry = np.subtract(arry1, arry2)
est4 = list(sub_arry)

print(f'Após a subtração, a primeira estrutura ficou com os seguintes valores: {est4}.')
