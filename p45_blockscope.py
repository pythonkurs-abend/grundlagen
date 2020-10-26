def create_zahl():
    zahl = 42
    # Ab hier existiert die LOKALE Variable zahl nicht mehr


create_zahl()
# Hier gilt der Blockscope print(zahl)

zahl = 0

if False:
    zahl = 42

# Hier nicht
print(zahl)

for i in range(10):
    pass

print(i)

zahlen = [2, 3, 4]


for i in zahlen:
    print(i)
