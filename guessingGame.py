from random import randint
from time import sleep
i = "\033[1;33m"
f = "\033[m"
print("Teste sua sorte no\nJOGO DA ADIVINHAÇÃO\n")
print("""Você tem \033[1;33m100 noobCoins\033[m de crédito para apostar
E apenas {}4 TENTATIVAS{} para vencer""".format(i, f))
print("Vou pensar em um número de 0 a 10\nVocê consegue adivinhar??")
computador = randint(0, 10)
num_palpites = 0
noobCoins = 100
jogadas = 4
acertou = False
# print(computador)
while not acertou:
    if noobCoins >= 1 and jogadas >= 1:
        aposta = int(input("Digite o valor da sua aposta >>"))
    jogador = int(input("Digite seu palpite >> \n"))
    noobCoins -= aposta
    jogadas -= 1

    if jogador == computador:
        acertou = True
    elif noobCoins >= 20 and jogadas == 0:
        tentativa = int(input("Suas jogadas acabaram\nDeseja comprar mais 2 jogadas por 20 noobCoin?\n[1] SIM\n[2] NÃO"))
        if tentativa == 1:
            jogadas += 2
            noobCoins -= 20
            print("Boa sorte nessa próxima rodada.\nVocê tem {} jogadas\n".format(jogadas))
        else:
            print("Você tem {} noobCoins\nFim do jogo".format(noobCoins))
    else:
        print("Que pena! Você errou.\nVocê tem {} noobCoins\n".format(noobCoins))
        if noobCoins < 10:
            print("Boa sorte nessa próxima rodada.\nVocê tem {} jogadas\n".format(jogadas))
        elif noobCoins >= 10:
            opcoes = int(input("Deseja uma dica por 10 noobCoins?\n[1] SIM >>\n[2] NÃO >>"))
            if opcoes == 1 and jogador < computador:
                print("DICA: Pensei em um número maior que {}\n".format(jogador))
                noobCoins -= 10
            elif opcoes == 1 and jogador > computador:
                print("DICA: Pensei em um número menor {}\n".format(jogador))
                noobCoins -= 10
        print("Você tem {} noobCoins".format(noobCoins))
        print("Boa sorte!\nVocê tem {} jogadas\n".format(jogadas))

print("""Parabéns!!Você ganhou {} noobCoins
Você tem {} noobCoins
Ainda restam {} jogadas"""
      .format(aposta, noobCoins + (aposta * 2), jogadas))
