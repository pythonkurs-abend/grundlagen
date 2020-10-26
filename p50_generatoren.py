from random import random


def my_generator():
    for i in range(3):
        print('Generiere Zufall')
        yield random()


generator = my_generator()

print(next(generator, None))
print(next(generator, None))
print(next(generator, None))
print(next(generator, None))
