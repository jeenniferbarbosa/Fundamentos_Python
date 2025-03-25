larguraParede = float(input("Qual é a largura da sua parede em metros? "))
alturaParede = float(input("Qual é a altuta da sua parede em metros? "))
area = larguraParede * alturaParede
litroTinta = area / 2

print(f"Para pintar uma parede com uma área total de {area} serão necessários {litroTinta} litros de tinta. ")
