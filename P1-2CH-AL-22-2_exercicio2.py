#Código produzido para a segunda chamada da prova de Algoritmos II - IFC Campus Camboriú
#ALUNO: KAIAN VINICIUS (2022004420)

est1 = []
est2 = []

for numero in range(10):
    numero = int(input("Por favor, insira um valor para a primeira estrutura: "))
    est1.append(numero)

print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

for numero in range(10):
    numero = int(input("Agora, insira um valor para a segunda estrutura: "))
    est2.append(numero)

print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

print(f'A primeira estrutura ficou com os seguintes valores: {est1}')
print(f'A segunda estrutura ficou com os seguintes valores: {est2}')
print(f'Os números que não se repetem entre ambas as estruturas são os seguintes: {set(est1) ^ set(est2)}')