import random
import time
print('--' *12,'GERADOR DE NÚMEROS DA MEGA-SENA' , '--' *12)
qnt_jogos = int(input('Quantos jogos da mega-sena você quer que eu sorteie?  '))
jogos = []
intervalo = 0.5


for i in range(qnt_jogos):
    print('--' * 5, f'{i+1}ª jogo', '--' * 5)

    números = random.sample(range(1, 61), 6)

    print (números)

    jogo = [números]  
    jogos.append(jogo)
    
    time.sleep(intervalo)

print('--' *12,'BOA SORTE!' , '--' *12)