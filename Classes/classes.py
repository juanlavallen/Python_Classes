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


person = Person('Lionel Messi', 34, 'Argentina')  # Instancia de la clase
print(person)

print(person.name)  # --> Lionel Messi
print(person.age)  # --> 34
print(person.nationality)  # --> Argentina
