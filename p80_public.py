class A:
    def __init__(self, zahl):
        self.__zahl = zahl

    def get_zahl(self):
        return self.__zahl

    def set_zahl(self, zahl):
        if zahl > 1000:
            zahl = 1000
            # raise ValueError('Glaub ich nicht')

        self.__zahl = zahl

    def _berechne_xy(self):
        pass

    def hole_xy(self):
        self._berechne_xy()


a1 = A(42)
print(a1.get_zahl())
a1.set_zahl(99999)

# ZUgriff auf protected (SCHLECHT)
# print(a1._zahl)

# Private (Ganz schlecht)
print(a1._A__zahl)

'test'.isupper()
