#um pequeno quiz game, com a adição de áudios

import random
import playsound



num = random.randint(0, 10)
num_selecionado = int(input('O programa vai gerar um número de 0 a 10, digite um número e tente a sorte: '))

if num == num_selecionado:
    print('Você acertou!!')
    playsound.playsound('certo.mp3')  


else: 
    print('Você errou!!')
    playsound.playsound('errado.mp3')  


