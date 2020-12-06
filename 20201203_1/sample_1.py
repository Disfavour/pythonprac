from types import FunctionType
class T(type):
    def __init__(self,*ap, **an):
        print("Init", self, ap, an)
        for attr, obj in vars(self).items():
            if isinstance(obj, FunctionType):
                print("*", attr)
        super().__init__(*ap, **an)

        def __new__(metacl, name, parents, namespace):
            print("New", name, parents, namespace)
            cls = super().__new__(metacl, name, parents, namespace)
            return cls

        def __call__(self, *ap, **an):
            print("Call", self, ap, an)
            super().__call__(*ap, **an)

class C(metaclass=T):
    A = 100500
    def fun(self): pass


