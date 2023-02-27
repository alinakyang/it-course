class A:
    @staticmethod
    def plus(a, b):
        return [a, b, a + b]


class B:
    @staticmethod
    def minus(a, b):
        return [a, b, a - b]


class C(A, B):
    pass


obj = C()
print(obj.plus(1, 2))
print(obj.minus(20, 10))
