def verdopple(zahl):
    return zahl * 2


lambda_verdoppeln = lambda x: x * 2

print(verdopple(4))
print(lambda_verdoppeln(4))


def format_zahl(zahl, format_function):
    return format_function(zahl)


print(format_zahl(42, lambda x: 'Zahl: ' + str(x)))


def format_fun(zahl):
    return 'Zahl: ' + str(zahl)


print(format_zahl(42, format_fun))


def test(zahl):
    # return zahl * 3
    return (lambda x, y: x * y)(zahl, 4)


print(test(5))
