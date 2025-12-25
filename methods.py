class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
    
    def subtraction(self,a,b):
        return a-b

calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(4, 2))
print(calc.subtraction(1, 3))