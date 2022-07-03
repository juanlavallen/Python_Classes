name = 'Lionel Messi'

print(name[6:])

print('Upper Case:' + name.upper())
print('Lower Case:' + name.lower())

# Split

split_method = name.split('|')  # Separa por espacios == split()
split_method = name.split('e')  # Separa por "e"

print(split_method)

# Interpolation & .format()
string = 'string'

print('This is a text {}'.format('string'))
print(f'This is a text {string}')
