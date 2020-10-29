class Kunde:
    def __init__(self, kdnr, name):
        self.kdnr = kdnr
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.kdnr == other

        if not isinstance(other, Kunde):
            return False

        return self.kdnr == other.kdnr


k1 = Kunde('10001', 'Huber')
k2 = Kunde('10002', 'Schröder')
k3 = Kunde('10001', 'Huber')

print(k1 == k2)
print(k1 == k3)

print(id(k1))
print(id(k2))
print(id(k3))

print(k1 == 42)
print(isinstance(k1, Kunde))
print(isinstance(k1, int))

print(k1 == '10001')
# print(k1 > k2)