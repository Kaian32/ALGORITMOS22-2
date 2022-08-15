va = int(input("Por favor, insira o primeiro valor: "))
vb = int(input("Por favor, insira o segundo valor: "))
vc = int(input("Por favor, insira o terceiro valor: "))

mediana = 0

if (va<vb or va<vc) and (va>vb or va>vc):
    mediana = va
    
elif (vb<va or vb<vc) and (vb>va or vb>vc):
    mediana = vb
elif (vc<va or vc<vb) and (vc>va or vc>vb):
    mediana = vc
elif va==vb==vc:
    print("Os três números são iguais! Tente novamente com outros valores.")
    exit()

print(f"A mediana entre esses três valores é {mediana}.")