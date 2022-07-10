### Variables ###

first_name = 'Juan'
last_name = 'Lavallen'
age = 19
male = True

print(f'Type: {type(first_name)}')  # <class 'str'>
print(f'Type: {type(last_name)}')  # <class 'str'>
print(f'Type: {type(age)}')       # <class 'int'>
print(f'Type: {type(male)}')     # <class 'bool'>

print(f'First Name: {first_name}')
print(f'Last  Name: {last_name}')
print(f'Age: {age}')

PI = 3.10
LANG = 'ES'

print(PI)
print(LANG)

# full_name = first_name + ' ' + last_name
full_name = f'{first_name} {last_name}'
print(full_name)

### Inputs ###

color   = input('Ingrese un color')
country = input('Ingrese un Pais')
car     = input('Ingrese una marca de Autos')

print(f'El Color ingresado es: {color}')
print(f'El Pais  ingresado es: {country}')
print(f'La marca ingresada es: {car}')
