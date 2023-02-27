class D:
    @staticmethod
    def stat_print_dict(obj):
        print(obj.__dict__)

    def cls_print_dict(self):
        print(self.__dict__)


class E(D):
    e = "Класс E"

obj_1 = D()
obj_1.cls_print_dict()
obj_1.stat_print_dict(D)

obj_2 = E()
obj_2.cls_print_dict()
obj_2.stat_print_dict(E)
