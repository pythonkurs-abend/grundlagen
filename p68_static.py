class A:
    @staticmethod
    def print_a():
        print('Hello')


# a1 = A()
# Falsch a1.print_a()

# Statische Methoden funktionieren ohne Instanz
A.print_a()


class B:
    # Statische Variable
    anzahl_instanzen = 0

    def __init__(self):
        B.erhoehe_anzahl_instanzen()
        self.zahl = 10

    @staticmethod
    def erhoehe_anzahl_instanzen():
        B.anzahl_instanzen += 1


b1 = B()
b2 = B()

print(b1.anzahl_instanzen)
print(b2.anzahl_instanzen)
print(B.anzahl_instanzen)
b2.zahl = 42

print(b1.zahl)
print(b2.zahl)

