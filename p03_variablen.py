# Python ist bei der Definition von Variablen untypisiert
# In Python sind alle Datentypen Objekte
# int zahl = 42;

# Zahlendatentypen

# ubyte byte
# 2^8 = 256 - 0-255, -128 bis +127
# IPv4 42.42.42.42
# rgb (255, 0, 0)

# short
# 2^16 = 65536
# Ports
# User / Prozesse

# 2^32 = 4.290.000.000
# int, int32

# 2^64 1.84e^20
# long, int64, int

zahl = 42

print(type(zahl))
# print(9999999999999999999999999999999 + 1)
# print(2 ** 64)
# print(2 ** 128)
# print(2 ** 256)
# print(2 ** 512)

# TypeHints python37:int = 42

# float -> 2^32
# double -> 2^64
pi = 3.1415924

import math

print(math.pi)
print(type(pi))

print(99999999.1234567890123456789)
print(0.5 + 0.5)
print(0.5 + 0.3 + 0.2)
print(0.5 + 0.2 + 0.2 + 0.1)
print(0.5 + 0.2 + 0.1)
print(round(0.5 + 0.2 + 0.1))

# Strings
# einEinzelnesZeichen
ein_einzelnes_zeichen = 'a'
print(type(ein_einzelnes_zeichen))

wort = 'Hallo Python'
print(type(wort))

# Boolean (ucfirst)
wahr = True
falsch = False

print(42 == 'sinn')

# null
nicht_zugwiesen = None

print(type(nicht_zugwiesen))

# test = None

"""
int test;

if (42 == 42) {
   test = 42;
}

"""

test = None

if 42 == 42:
    test = 'belegt'


if test:
    print('Test hat einen gültigen Wert')

print(test)


def print_hallo_welt():
    print('Hallo Welt')


print(type(print_hallo_welt))


class Auto:
    pass


print(type(Auto))

# Audi audi = new Auto();
audi = Auto()


print(type(audi))


import math


print(type(math))


# Array -> List
# String[] namen = {"Bernd", "Tanja", "Florian"};
namen = ["Bernd", "Tanja", "Florian"]

print(type(namen))

namen[1] = 'VERÄNDERT'

print(namen)

# Tuple -> Immutable List
namen_tuple = ("Bernd", "Tanja", "Florian")

# Geht beim Tuple nicht
# namen_tuple[1] = 'VERÄNDERT'

print(namen_tuple)
print(type(namen_tuple))

# Dictionaries (Assoziative Array)
kunde = {'vorname': 'Bernd', 'nachname': 'Huber'}

print(kunde['vorname'])
print(kunde.get('vorname'))

print(type(kunde))

"""
Regeln Variablen:



"""



