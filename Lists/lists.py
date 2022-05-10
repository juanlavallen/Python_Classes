### Arrays ###

colors = ['Red', 'White', 'Blue', 'Black', 'Orange']
print(colors[0])  # [0] --> Red
print(colors[2])  # [2] --> Blue
print(colors[4])  # [4] --> Orange

new_color = str(input('Agrega otro color: '))
colors.append(new_color)  # ['Red', 'White', 'Blue', 'Black', 'new_color']
print(colors)

delete_color = str(input('Elimina un color: '))  # Pink
colors.remove(delete_color)  # ['Red', 'White', 'Blue', 'Black']
colors.pop()  # ['Red', 'White', 'Blue', 'Black'] --> last position
print(colors)

colors.reverse()  # --> ['Orange', 'Black', 'Blue', 'White', 'Red']
print(colors)

colors.copy()  # returns a copy --> ['Red', 'White', 'Blue', 'Black', 'Orange']
print(colors)

colors.sort()  # sort A --> Z
print(colors)

print(len(colors))