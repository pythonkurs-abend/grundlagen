def addiere(*zahlen):
    return sum(zahlen)


print(addiere(10, 22, 10))


def print_kunde(**kunde):
    print(kunde.get('vorname', 'unbekannt'))
    print(kunde.get('nachname', 'unbekannt'))
    print(kunde.get('alter', 'unbekannt'))
    print(kunde.get('strasse', 'unbekannt'))
    print(kunde.get('plz', 'unbekannt'))
    print(kunde.get('ort', 'unbekannt'))


print_kunde(vorname='Bernd', strasse='Bla', nachname='Huber')


numbers = [3, 5, 6, 11, 12]
ueber_5 = [number for number in numbers if number > 5]
print(ueber_5)
