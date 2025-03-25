from datetime import date

print("========= Alistamento Militar =========")
anoNasc = int(input("Qual o ano de nascimento? "))
anoAtual = date.today().year #Ano atual
idade = anoAtual - anoNasc

print(f"Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.")

if idade == 18:
    print("Essa é a idade necessária para se alistar. Se aliste imediatamente! ")
elif idade < 18:
    tempo = 18 - idade
    anoF = anoAtual + tempo
    print(f"Você ainda não tem idade suficiente para se alistar. Seu alistamento será em {anoF}, daqui a {tempo} anos.")
else:
    anoMais = idade - 18
    print(f"Já passou da hora de se alistar! Você deveria ter se alistado a {anoMais} atrás.")