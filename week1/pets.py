class Pet:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'I am {self.name}'


class Dog(Pet):

    def sound(self):
        return 'Woof'

    def greeting(self):
        return f'{self.sound()}, I am {self.name}'


class Cat(Pet):

    def sound(self):
        return "Meow"


cat = Cat('Lord Purr')
dog = Dog('Peaches')
print(cat.greeting() + dog.greeting())
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, ")
print("sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
print("Ut enim ad minim veniam, ")
print("quis nostrud exercitation ullamco laboris nisi ut ")
print("aliquip ex ea commodo consequat.")
print("Duis aute irure dolor in reprehenderit in ")
print("voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
print("Excepteur sint occaecat cupidatat non proident, ")
print("sunt in culpa qui officia deserunt mollit anim id est laborum.")
