class D:
    @staticmethod
    def stat_print_dict(obj):
        print(obj.__dict__)

    def cls_print_dict(self):
        print(self.__dict__)


obj = D()
obj.cls_print_dict()
obj.stat_print_dict(D)
