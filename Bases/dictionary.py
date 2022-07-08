### Dictionary ###

data = {
    'name': 'Lionel',
    'age': 34,
    'sons': ['Mateo', 'Ciro', 'Thiago']
}

print(data['sons'])  # ['Mateo', 'Ciro', 'Thiago']
print(data['sons'][2])  # Thiago
print(data['sons'][2].upper())  # THIAGO

# Cambiando el valor de 'name'
data['name'] = 'Lionel Messi'
print(data['name'])  # --> Lionel Messi

# Creando una nueva clave con un nuevo valor
data['nationality'] = 'Argetina'
print(data)

# Eliminando un elemento
del data['nationality']
print(data)

print(data.items())  # Separa los elementos --> Tuple

print(data.values())  # Devuelve solo el valor de cada elemento

# Keys
print(data.keys())  # Retorna todas las Keys

# Values
print(data.values())  # Retorna todos los valores
