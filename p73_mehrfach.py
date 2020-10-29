class A:
    def __init__(self, z1):
        self.z1 = z1

    def print_a(self):
        print('a', self.z1)


class B:
    def __init__(self, z2):
        self.z2 = z2

    def print_b(self):
        print('b', self.z2)


class C(B, A):
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2


c1 = C(42, 20)

c1.print_a()
c1.print_b()


# VORSICHT: Sollte nicht mit Klassen verwendet
# werden die Pflichtfelder (im Konstruktor)haben