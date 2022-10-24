#Código produzido para a segunda chamada da prova de Algoritmos II - IFC Campus Camboriú
#ALUNO: KAIAN VINICIUS (2022004420)
#est1 = normal
#est2 = maior que 50
#est3 = posição no est1

est1 = []
est2 = []
est3 = []
pos = -1

for num in range(10):
    num = int(input("Por favor, insira um valor: "))
    valor = num
    pos += 1
    est1.append(valor)
    if num > 50:
        est2.append(valor)
        est3.append(pos)        

print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

print(f'A estrutura ficou da seguinte forma: {est1}')

if len(est2) >= 1:
    print(f'Dos valores dessa estruturas, aqueles maiores que 50 são os seguintes: {est2}')
    print(f'Estes valores estão - respectivamente - nas posições {est3} da estrutura.')
else:
    print(f'Não existe nenhum valor maior que 50 presente na estrutura!')