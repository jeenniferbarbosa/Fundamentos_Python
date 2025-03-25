from datetime import date

anoAtual = date.today().year
anoNasc = int(input("Qual o ano de nascimento do atleta? "))
idade = anoAtual - anoNasc

print(f"De acordo com a data informada a idade do atleta é {idade} anos.")
if idade <= 9:
    print("A categoria que ele (a) se enquadra é MIRIM.")
elif idade <= 14:
    print("A categoria que ele (a) se enquadra é INFANTIL.")
elif idade <= 19:
    print("A categoria que ele (a) se enquadra é JÚNIOR.")
elif idade <= 25:
    print("A categoria que ele (a) se enquadra é SÊNIOR.")
else:
    print("A categoria que ele (a) se enquadra é MASTER.")