## screva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

## F = C x 1,8 + 32.

celsius = float(input("Informe uma temperatura em graus celsius: "))
fahrenheit = celsius * 1.8 + 32

print(f"A temperatura {celsius}ºC é igual a {fahrenheit:.2f}ºF")