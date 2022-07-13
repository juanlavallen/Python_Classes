import random

def run(a, b):

    print('=======================')
    print(' ¡Bienvenido al Juego! ')
    print('=======================')

    random_number = random.randint(a, b)
    prediction = 0

    while prediction != random_number:
        prediction = int(input(f'Ingrese un numero entre {a} y {b}: '))

        if prediction < random_number:
            print('Vuelva a intentar. El numero ingresado es menor')
        elif prediction > random_number:
            print('Vuelva a intentar. El numero ingresado es mayor')

    print(f'¡Felicitaciones, el numero {random_number} es correcto!')

if __name__ == '__main__':
    run(1, 10)
