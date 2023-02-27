class Counter:

    def __init__(self, start=None, end=None):
        self.start = start
        self.current = start
        self.end = end

    def increase(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            return 'Выход за границу счетчика'

    def decrease(self):
        if self.current > self.start:
            self.current -= 1
            return self.current
        else:
            return 'Выход за границу счетчика'


obj = Counter(1, 10)

print(obj.increase())
print(obj.decrease())
print(obj.decrease())
