class A:
    """Класс А"""

    def set_a(self, num):
        self.a = num

    def get_a(self):
        return self.a


class F(A):
    """Класс F"""

    def set_a(self, a):
        super().set_a(a)
        print("Атрибут a установлен! = ", a)

print(F.__doc__)
obj = F()
obj.set_a(5)