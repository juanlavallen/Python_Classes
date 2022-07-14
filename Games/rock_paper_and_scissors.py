import random


def play():
    print('Piedra: PI - Papel: PA - Tijera: TI')

    user = input('Ingresa una opcion: ').upper()
    computer = random.choice(['PI', 'PA', 'TI'])

    if ((user == 'PI' and computer == 'TI')
        or (user == 'TI' and computer == 'PA')
        or (user == 'PA' and computer == 'PI')):
        return print('¡Ganaste!')
    elif user == computer:
        return print('¡Empate!')
    else:
        return print('¡Perdiste!')


if __name__ == '__main__':
    play()
