class B:
    """Класс B"""

    def __init__(self, b):
        self.b = b

    def get_b(self):
        return self.b


print(B.__doc__)

obj = B(5)

print(obj.get_b())
