class A:
    def __init__(self, zahl):
        self.zahl = zahl

    def __add__(self, other):
        self.zahl += other

        # Chaining Pattern
        return self

a1 = A(20)

a1 = a1 + 10 + 12

print(a1.zahl)
