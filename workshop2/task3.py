class A:
    """Класс А"""

    def set_a(self, num):
        self.a = num

    def get_a(self):
        return self.a


print(A.__doc__)

obj_1 = A()
obj_1.set_a(15)

print(obj_1.get_a())

obj_2 = A()
obj_2.a = 200
print(obj_2.get_a())
