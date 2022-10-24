#Código produzido para a segunda chamada da prova de Algoritmos II - IFC Campus Camboriú
#ALUNO: KAIAN VINICIUS (2022004420)

estrutura = []

for numero in range(15):
    numero = int(input("Por favor, insira um valor: "))
    estrutura.append(numero)

print(f'A estrutura após os números ficou da seguinte forma: {estrutura}.')
print(f'O maior valor encontrado na estrutura foi {max(estrutura)}.')