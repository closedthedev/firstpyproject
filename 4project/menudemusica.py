#criando um menu com o top 10 das melhores músicas de hip-hop dos anos 90, deixando o usuário escolher qual música quer ouvirescolha = 0

import playsound

escolha = 0
nome = str(input('Digite o seu nome: '))

print(f'Olá, {nome}! Temos aqui o top 10 das melhores músicas de hip-hop dos anos 90, pode ouvir a vontade!')
print('               ')

while escolha != 11:
    
    print('[1]  2pac - Ambitionz Az A Ridah')
    print('[2]  2pac - Hit ''Em Up')
    print('[3]  Biggie - Big Poppa')
    print('[4]  Biggie - Hypnotize')
    print('[5]  Dr Dre ft. Snoop Dogg - Nuthin'' But A G Thang')
    print('[6]  Dr Dre ft. Snoop Dogg - Still D.R.E')
    print('[7]  Dr Dre ft. Snoop Dogg - The Next Episode')
    print('[8]  Eminem - My name is')
    print('[9]  Ice Cube - Check Yo Self')
    print('[10] Ice Cube - You Know How We Do It')
    print('[11] Encerrar Programa')

    escolha = int(input('>>>>>>Qual é a sua opção? '))

    if escolha == 1:
        playsound.playsound('2pac - Ambitionz Az A Ridah.mp3')

    elif escolha == 2:
        playsound.playsound('2pac - Hit Em Up.mp3')
    
    elif escolha == 3:
        playsound.playsound('Biggie - Big Poppa.mp3')

    elif escolha == 4:
        playsound.playsound('Biggie - Hypnotize.mp3')

    elif escolha == 5:
        playsound.playsound('Dr Dre ft. Snoop Dogg - Nuthin But A G Thang.mp3')

    elif escolha == 6:
         playsound.playsound('Dr Dre ft. Snoop Dogg - Still D.R.E..mp3')

    elif escolha == 7:
        playsound.playsound('Dr Dre ft. Snoop Dogg - The Next Episode.mp3')

    elif escolha == 8:
        playsound.playsound('Eminem - My Name Is.mp3')   

    elif escolha == 9:
        playsound.playsound('Ice Cube - Check Yo Self.mp3')   

    elif escolha == 10:
        playsound.playsound('Ice Cube - You Know How We Do It.mp3') 

    elif escolha == 11:
        print('Finalizando...')      

    elif escolha == 0 or escolha > 11:
        print('Opção inválida, tente novamente.')
