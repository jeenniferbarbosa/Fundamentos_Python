from math import hypot

catetoOps = float(input("Comprimento do cateto oposto: "))
catetoAdj = float(input("Comprimento do cateto adjacente "))
calculo = hypot(catetoOps, catetoAdj)

print(f"A hipotenusa é {calculo:.2f}")