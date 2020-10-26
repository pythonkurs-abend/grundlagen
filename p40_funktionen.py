# DRY -> Don't repeat yourself


def print_hello():
    print('Hello Python')


print_hello()
print_hello()
print_hello()


def print_addiere(zahl1, zahl2, zahl3=0):
    print(zahl1 + zahl2 + zahl3)


print_addiere(20, 22)
print_addiere(20, 22, 10)
# print_addiere('asfd', 22)


# Keine Überladung in Python
# def print_addiere(zahl1, zahl2, zahl3):
#     print(zahl1 + zahl2 + zahl3)

# Default Werte nur am Ende
# def falsch(z1,  z2=42, z3,):
#     pass
