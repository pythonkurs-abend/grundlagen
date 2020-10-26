i = 0

while i < 10:
    print('Durchlauf', i)
    i += 1


zahl = 10000
counter = 0

while zahl > 9:
    zahl /= 3
    print(zahl)
    counter += 1


print('Zahl ist nach', counter, 'Durchläufen kleiner 10')
