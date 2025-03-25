#Conversor de Medidas

medida = float(input("Digite uma distância em metros: "))
med_cent = medida * 100
med_mili = medida * 1000

print(f"A medida de {medida:.1f}km corresponde a: \n{med_cent} centímetros \n{med_mili} milímetros")