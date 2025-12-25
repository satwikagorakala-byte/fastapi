class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


p = Person("Satwika")
p.greet()

class Person2:
    def greet(self, name):
        print(f"Hello, my name is {name}")


p2 = Person2()
p2.greet('Satwika')


