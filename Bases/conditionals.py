### Conditionals ###

hunger = True
thirst = True

if hunger and not thirst:
    print('Tengo hambre')
elif hunger and thirst:
    print('Tengo hambre y sed')
else:
    print('Tengo sed')

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


amount_available = 50000
amount_min = 1000
bank = str(input('Ingrese su Banco'))
amount = int(input('Ingrese el monto que desea retirar'))

if amount > amount_available:
    print(f'No puede retirar: ${amount} - Disponible ${amount_available}')
elif amount < amount_min:
    print(f'El monto minomo a retirar es de: ${amount_min}')
elif amount == amount_available:
    confirm = print('¿Esta seguro que desea retirar todo el dinero?')
    if confirm == 'Si':
        print(f'Operacion realizada correctamente, su saldo es de $0')
else:
    print('Operacion cancelada')