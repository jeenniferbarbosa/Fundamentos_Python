print("SERAO ACEITAS APENAS PALAVRAS SEM PONTUACAO")

frase = str(input("Digite uma frase: ")).upper().strip().replace(" ", "")
invertida = ""

for letras in range(len(frase) -1, -1, -1):
    invertida += frase[letras]

if frase == invertida:
    print(f"A frase foi {frase} e ivertida ficará: {invertida}.")
    print("A frase é um palíndromo")

else:
    print(f"A frase foi {frase} e ivertida ficará: {invertida}.")
    print("A frase não é um palíndromo")