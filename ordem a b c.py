a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))
c = float(input("Insira o terceiro valor: "))
lista = []
lista.append(a)
lista.append(b)
lista.append(c)

i = int(input("Qual tipo de filtração você deseja aplicar? Digite 1 para crescente e 2 para decrescente."))

if i == 1:
    lista.sort()

if i == 2:
    lista.sort(reverse=True)

print(f"Com a formatação selecionada, a ordem da lista ficou a seguinte: {lista}.")
