alt_deg = float(input("Por favor, insira - em metros - a altura do degrau: "))
alt_esc = float(input("Qual a altura, em metros, que você deseja alcançar com essa escada?\n"))

qtd_deg = alt_esc/alt_deg

import math
qtd_deg = math.ceil(qtd_deg)

print(f"Para a altura de {alt_esc}m, com o degrau tendo sua altura de {alt_deg}m cada, serão nescessários {qtd_deg} degraus.")