# Die ersten Tausend Primzahlen ausgeben
# -> In kleine Teile zerbrechen
# Was ist eine Primzahl und wie kann ich für eine beliebe Zahl ermitteln
# ob sie eine ist

zahl = 3
gefundePrimzahlen = 0
# 2 und 12

while gefundePrimzahlen < 1000:
    isPrime = True

    for i in range(2, zahl // 2 + 1):
        if zahl % i == 0:
            isPrime = False
            break

    if isPrime:
        print(zahl, end=', ')
        gefundePrimzahlen += 1

        if gefundePrimzahlen % 20 == 0:
            print('')

    # Immer erhöhen
    zahl += 1
