import random
import playsound


direções_validas = ['ESQUERDA', 'DIREITA']

direção = input('Você está andando de boa na rua até que encontra Jorgenelson. Jorgenelson é o maior e melhor ARREMESSADOR DE MANGA de toda a Bahia. Jorgenelson se prepara para arremessar uma manga em você, sendo que só tem como desviar para a esquerda ou direita. Qual direção você escolhe? ').upper() .strip()

if direção not in direções_validas:
    print("Por favor, digite apenas 'ESQUERDA' ou 'DIREITA'.")
else:
    mira_jorgenelson = random.choice(direções_validas)

    if direção == mira_jorgenelson:
        print('Infelizmente, você foi RECEPCIONADO com uma bela mangada!') 
        playsound.playsound('tomou.mp3')
    else:
        print('Você desviou, você exala a sucesso. ELE VENCE Y VENCE')
        playsound.playsound('desviou.mp3')