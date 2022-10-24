#Código produzido para a segunda chamada da prova de Algoritmos II - IFC Campus Camboriú
#ALUNO: KAIAN VINICIUS (2022004420)

est = [] #estrutura principal
est_par = [] #valores pares da estrutura
est_impar = [] #valores ímpares da estrutura
qtd_par = 0 #quantidade numérica de valores pares na estrutura
qtd_impar = 0 #quantidade numérica de valores ímpares na estrutura

for numero in range(10):
    numero = int(input("Insira um valor para a estrutura: "))
    est.append(numero)
    if numero%2 == 1:
        est_impar.append(numero)
        qtd_impar += 1
    else:
        est_par.append(numero)
        qtd_par += 1

print(f'Na estrutura {est}, foi(foram) encontrado(s) {qtd_par} número(s) par(es) e {qtd_impar} número(s) ímpar(es).')
print(f'O(s) valor(es) par(es) encontrado(s) foi(foram) {est_par}, já o(s) valor(es) ímpar(es) encontrado(s) foi(foram) {est_impar}.')