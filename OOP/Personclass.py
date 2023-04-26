class person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def speak(self):
        print(f'My name is {self.name} and i am {self.age} years old')

    def greet(self, person):
        if person.name == 'Rogers':
            print("Hey mann")
        else:
            print(f'Hi im {person.name}')


bob = person('bob', 12, 234)
sally = person('sally', 13, 134)

bob.greet()
