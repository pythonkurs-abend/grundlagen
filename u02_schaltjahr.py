# Schaltjahr
# jahr = input('Jahr? ')

"""
Schaltjahre:

- Sind durch 4 teilbar
- ausser sie sind durch 100 teilbar und nicht durch 400

Schaltjahre: 2020, 2016, 2000, 1600
Keine Schaltjahre: 2019, 2018, 1900, 1800
"""

# Datentyp: input erkennt den Datentyp basierend auf
# der Eingabe im Gegensatz zu raw_input() (Immer String)
# deswegen ist der int cast eigentlich überflüssig.
jahr = int(input('Jahr? '))

if jahr % 4 != 0:
    print('Kein Schaltjahr')
elif jahr % 100 == 0 and jahr % 400 != 0:
    print('Kein Schaltjahr')
else:
    print('Schaltjahr')

# Nicht so schön
if jahr % 4 == 0:
    if jahr % 100 == 0 and jahr % 400 != 0:
        print('Kein Schaltjahr')
    else:
        print('Schaltjahr')
else:
    print('Kein Schaltjahr')
