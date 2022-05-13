### Dictionary ###

data = {
    'name': 'Lionel',
    'age': 34,
    'sons': ['Mateo', 'Ciro', 'Thiago']
}

print(data['sons'])

# Cambiando el valor de 'name'
data['name'] = 'Lionel Messi'
print(data['name'])  # --> Lionel Messi

# Creando una nueva clave con un nuevo valor
data['nationality'] = 'Argetina'
print(data)

# Eliminando un elemento
del data['nationality']
print(data)
