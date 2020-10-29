class A:
    def print_a(self):
        print('a')


class B(A):
    def print_a(self):
        print('b')



a1 = A()
a1.print_a()

b1 = B()
b1.print_a()

print(isinstance(b1, A))
