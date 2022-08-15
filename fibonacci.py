n_termos = int(input("Quantos termos você deseja calcular?\n"))  
n1 = 0
n2 = 1
ctd = 0

if n_termos <= 0:  
    print ("Insira um valor positivo! O valor não é válido!")
    exit()  
elif n_termos == 1:  
    print (f"A sequência Fibonacci dessa quantidade de {n_termos} é: {n1}")  
else:
    print ("A sequência Fibonacci dessa quantidade de termos é:")  
    while ctd < n_termos:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        ctd += 1