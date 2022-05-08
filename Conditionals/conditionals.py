### Conditionals ###

number_one = int(input('Ingrese un numero:'))
number_two = int(input('Ingrese otro numero:'))

if number_one > number_two:
    print(f'{number_one} es mayor que {number_two}')
elif number_one < number_two:
    print(f'{number_one} es menor que {number_two}')
elif number_one == number_two:
    print(f'{number_one} es igual que {number_two}')


first_name = str(input('Ingrese su nombre:'))
last_name = str(input('Ingrese su apellido:'))

full_name = f'{first_name} {last_name}'
if full_name != str:
    print('Por favor ingresa los datos correspondientes')
elif full_name == 'Lionel Messi':
    print(f'¡Bienvenido {first_name}!')
else:
    print('No tenes permitido ingresar')
