import math

angulo = float(input("Digite um ângulo qualquer: "))
anguloConv = math.radians(angulo) # Converte o angulo de graus para radiano
seno = math.sin(anguloConv)
cosseno = math.cos(anguloConv)
tangente = math.tan(anguloConv)

print(f"O ângulo {angulo:.1f} tem o seno de {seno:.2f}\nO ângulo {angulo:.1f} tem o cosseno de {cosseno:.2f}\nO ângulo {angulo:.1f} tem a tangente de {tangente:.2f}")