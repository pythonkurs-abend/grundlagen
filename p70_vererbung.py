class A:
    def print_a(self):
        print('a')


# Klasse B erbt von Klasse A
# class B extends A
class B(A):
    def print_b(self):
        print('b')


b1 = B()
b1.print_a()
b1.print_b()


class C(B):
    pass


c1 = C()

c1.print_a()
c1.print_b()





