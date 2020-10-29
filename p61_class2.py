from random import random


def print_auto_info(hersteller, modell, ps, farbe):
    pass


class Auto:
    # public String hersteller = null;

    # Constructor public Auto(String hersteller, String model)
    def __init__(self, hersteller, modell, ps, farbe='schwarz'):
        print('Konstruktor Aufruf')
        # Dynamische Erstellung von Variablen
        self.hersteller = hersteller
        self.modell = modell
        self.ps = ps
        self.farbe = farbe
        self.lenkrad = 'hat eins'

    # Methoden
    def fahren(self):
        # self -> this
        return self.ps * random()

    def print_info(self):
        print(self.hersteller, self.modell, '(' + str(self.ps) + ')', self.farbe)

    def set_farbe(self, farbe):
        self.farbe = farbe

    def __str__(self):
        return self.hersteller + ' ' + self.modell


ford = Auto('Ford', 'Galaxy', 140)
hyundai = Auto('Hyundai', 'Tuscon', 170)

ford.ps = 99999999

print(id(ford))
print(id(hyundai))

print('Ford', ford.fahren())
print('Hyundai', hyundai.fahren())

hyundai.set_farbe('silber')

ford.print_info()
hyundai.print_info()

# Leeres Auto
# Geht nicht mehr, wegen den 3 Pflichtfeldern
# leer = Auto()
#
# leer.print_info()

print(ford)
print(hyundai)
