class A:
    a = 42

    def print_a(self):
        print('a')

    def print_b(self):
        print('b')

    def print_c(self):
        print('c')


buchstabe = 'b'

a1 = A()

# if buchstabe == 'a':
#     a1.print_a()
# elif buchstabe == 'b':
#     a1.print_b()
# elif buchstabe == 'c':
#     a1.print_c()

methoden_name = 'print_' + buchstabe

if hasattr(a1, methoden_name):
    func = getattr(a1, methoden_name)
    func()
