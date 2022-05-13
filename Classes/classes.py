### Classes ###

class Person:
    def __init__(self, name, age, nationality) -> None:  # constructor
        self.name = name
        self.age = age
        self. nationality = nationality

    def write(self):
        data = f'''
        Name: {self.name}
        Age: {self.age}
        Nationality: {self.nationality}
        '''
        print(data)

    def __str__(self) -> str:
        return f'Person: {self.name}, {self.age}, {self.nationality}'


person_one = Person('Lionel Messi', 34, 'Argentina')  # Instancia de la clase
person_two = Person('Thiago Messi',  9, 'Argentina')
print(person_one)
print(person_two)

print(person_one.name)  # --> Lionel Messi
print(person_one.age)  # --> 34
print(person_one.nationality)  # --> Argentina

# Accendiendo a los metodos
person_one.write()
person_two.write()
