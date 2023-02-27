class A:
    """Класс А"""

    def set_a(self, num):
        self.a = num

    def get_a(self):
        return self.a


class B:
    """Класс B"""

    def __init__(self, b):
        self.b = b

    def get_b(self):
        return self.b


class C(A, B):
    """Класс C = A + B"""

    def __init__(self, a, c):
        # В задании не указано каким значением инициализировать объекты класса B.
        super().__init__(0)
        self.a = a
        self.c = c

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_c(self):
        return self.c


print(C.__doc__)

obj = C(1, 2)

print("a = %s, b = %s, c = %s" % (obj.get_a(), obj.get_b(), obj.get_c()))
