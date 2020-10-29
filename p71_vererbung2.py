"""
Gemeinsamkeiten zusammen
"""

class Kunde:
    def __init__(self, strasse, plz, ort):
        self.strasse = strasse
        self.plz = plz
        self.ort = ort
        self.land = 'Deutschland'

    def __str__(self):
        return self.strasse + ' ' + self.plz + ' ' + self.ort

    def get_anschrift_kopf(self):
        return 'Unbekannt'

    def get_address_label(self):
        return self.get_anschrift_kopf() + self.strasse\
               + '\n' + self.plz + ' ' + self.ort + '\n' + self.land


class PrivatKunde(Kunde):
    def __init__(self, vorname, nachname, strasse, plz, ort):
        self.vorname = vorname
        self.nachname = nachname
        super().__init__(strasse, plz, ort)

    def get_anschrift_kopf(self):
        return self.vorname + ' ' + self.nachname + '\n'


class FirmenKunde(Kunde):
    def __init__(self, firmenname, strasse, plz, ort):
        self.firmenname = firmenname
        super().__init__(strasse, plz, ort)

    def get_anschrift_kopf(self):
        return self.firmenname  + '\n'


bernd = PrivatKunde('Bernd', 'Huber', 'Teststr. 42', '80335', 'München')
bmw = FirmenKunde('BMW', 'Musterstr. 23', '80939', 'München')


print(bernd.get_address_label())
print(bmw.get_address_label())