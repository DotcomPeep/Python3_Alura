#Curso do Alura Python 3 parte 1: Introdução à nova versão da linguagem

import random

from forca import jogo_forca

def jogo_advinhacao():
    print("====================================")
    print("Bem vindos(as) ao jogo de advinhação")
    print("====================================")

    numero_secreto = random.randrange(1, 101) # 1 a 100
    total_tentativas = 0
    pontos = 100

    print("Escolha o nível de dificuldade desejado sendo")
    print("(1)fácil (2)médio (3)difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    for rodada_atual in range(1, total_tentativas + 1):

        print("Você terá 3 tentativas")
        print("Tentativa {} de {}".format(rodada_atual, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou {}".format(chute_str))

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 0 e 100!")
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(numero_secreto == chute):
            print("Você acertou")
            print("Você fez um total de {} pontos. Parabéns!!!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou, seu chute foi menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("O número secreto era: {}".format(numero_secreto))

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogo_advinhacao()