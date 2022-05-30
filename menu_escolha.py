import time
import forca
import advinhacao

print("====================================")
print("*****Bem vindos(as) ao Dotverse*****")
print("**********Escolha seu jogo**********")
print("====================================")

print("(1)Forca   (2)Advinhação")

jogo = int(input("Escolha o jogo: "))

if(jogo == 1):
    print("Você escolheu o jogo da forca")
    time.sleep(3) #delay de 3 segundos para começar
    forca.jogo_forca()
elif(jogo == 2):
    print("Você escolheu o jogo de advinhação")
    time.sleep(3) #delay de 3 segundos para começar
    advinhacao.jogo_advinhacao()