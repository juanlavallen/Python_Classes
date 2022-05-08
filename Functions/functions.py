### Functions ###

full_name = 'Lionel Messi'


def print_full_name():
    print(f'{full_name}')


print_full_name()


def add(a, b):
    c = int(a) + int(b)
    return print(f'El resultado es: {c}')


add(10, 13)


def subtract(a, b):
    if a > b:
        c = a - b
        return print(f'El resultado es: {c}')
    elif b > a:
        c = b - a
        return print(f'El resultado es: {c}')


subtract(250, 350)


def multiply(a, b):
    if a & b == 0:
        return print('A y B deben tener un valor mayor a 0')
    c = a * b
    return print(f'El resultado es: {c}')


number_one = int(input('Ingrese un numero:'))
number_two = int(input('Ingrese otro numero:'))

multiply(number_one, number_two)
