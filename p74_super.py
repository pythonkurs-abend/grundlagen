class A:
    def print_a(self):
        print('a')


class B(A):
    def print_a(self):
        print('b')
        super().print_a()


b1 = B()
b1.print_a()


'test'.upper()
