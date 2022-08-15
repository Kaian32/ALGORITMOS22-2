val = 0
val_list025 = list()
val_list2650 = list()
val_list5175 = list()
val_list76100 = list()
while val >= 0:
    val = int(input("Insira um valor inteiro positivo. Para finalizar, digite um valor negativo.\n"))
    if val < 25 and val > 0:
        val_list025.append(val)
    elif val > 25 and val < 51:
        val_list2650.append(val)
    elif val > 50 and val < 76:
        val_list5175.append(val)
    elif val > 75 and val < 101:
        val_list76100.append(val)

print (f"Dentre todos os valores informados, os valores entre 0-25 foram {val_list025}, os valores entre 25-50 {val_list2650}, os valores entre 51-75 {val_list5175} e os valores entre 76 e 100 foram {val_list76100}.")