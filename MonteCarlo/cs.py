class A(object):
    def __init__(self):
        self.a = 1

a = A()
b = a
b.a += 1
print(a.a, b.a)
