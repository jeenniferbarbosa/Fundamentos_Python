from random import randint

soma = 0
vencidas = 0

print("=-=-=" * 8)
print("JOGO DE ADIVINHA - PAR OU ÍMPAR")
print("=-=-=" * 8)

while True:
    pc = randint(0, 11)
    jogador_num = int(input("Informe um valor: "))
    jogador_par_impar = str(input("Par ou Ímpar? [P/I] ")).upper().strip()
    soma = jogador_num + pc
    print("˜˜˜˜˜˜˜" * 5)

    if soma % 2 == 0 and jogador_par_impar == 'P':
        vencidas += 1
        print(f"Você escolheu o número {jogador_num} e pc escolheu o número {pc}. A soma desses valores é: {soma}")
        print("VOCE VENCEU! Vamos continuar.")
        print("˜˜˜˜˜˜˜" * 5)
    elif soma % 2 != 0 and jogador_par_impar == "I":
        vencidas += 1
        print(f"Você escolheu o número {jogador_num} e pc escolheu o número {pc}. A soma desses valores é: {soma}")
        print("VOCE VENCEU! Vamos continuar.")
        print("˜˜˜˜˜˜˜" * 5)
    else:
        print(f"Você escolheu o número {jogador_num} e pc escolheu o número {pc}. A soma desses valores é: {soma}")
        print(f"VOCE PERDEU! NO final, você teve partidas {vencidas} ganhas.")
        break