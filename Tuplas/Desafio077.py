palavras = (
    "Luz",
    "Urso",
    "Computador",
    "Mouse",
    "Aprender",
    "Python",
    "Estudos",
    "Livro",
    "Musica"
)

for pos in range(len(palavras)): # Analisa cada palavra da tupla
    vogal = palavras[pos]
    print(f"\nNa palavra {vogal} temos as vogais: ", end="")
    for letra in vogal: # Analisa cada letra da palavra da tupla
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")

