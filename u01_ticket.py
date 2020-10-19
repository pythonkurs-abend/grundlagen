alter = int(input('Alter? '))

print('Eingabe: ', alter)

# Kinderticket (u18), Seniorenticket (ab 65), Erwachseneticket

if alter < 18:
    print('kinder')
elif alter < 65:
    print('erwachsen')
else:
    print('senioren')

if alter < 18:
    print('kinder')
elif alter > 64:
    print('senioren')
else:
    print('erwachsen')


if alter < 65 and alter > 18:
    print('erwachsenen')
elif alter > 64:
    print('rentner')
else:
    print('kinder')
