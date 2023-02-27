class SuperClass:
    def __init__(self, num):
        self.num = num

    def get_num(self):
        print(self.num)


class SubClass(SuperClass):
    def __init__(self, num):
        super().__init__(num)
        print('Экземпляр создан!')


obj_1 = SubClass(0)
obj_1.get_num()

obj_2 = SubClass(5)
obj_2.get_num()
