import math

# Variablen in Module kann ich bearbeiten
math.pi = 5

print(math.pi)
print(id(math))

import math

# Module sind Singletons


print(math.pi)

print(id(math))


class A:
    instance = None

    def __init__(self, zahl):
        self.zahl = zahl
        # Config Datei laden würde

    @staticmethod
    def get_instance():
        if A.instance is None:
            A.instance = A(42)

        return A.instance


a1 = A.get_instance()
a2 = A.get_instance()

print(id(a1))
print(id(a2))

print()
print()

A.get_instance()
