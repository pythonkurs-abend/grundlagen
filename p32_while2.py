i = 0

while i < 10:
    i += 1

    if i % 3 == 0:
        # Springe zur nächsten Zahl
        continue

    print('Durchlauf', i)


while True:
    antwort = input('Zahl? ')
    print(type(antwort))

    if antwort == '42':
        break

    print('Du bist noch auf der Suche')


print('Du hast den Sinn gefunden')