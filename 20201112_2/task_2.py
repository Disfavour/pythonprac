class nestr(UserString):
    def __neg__(self):
        self.data = self.__class__("".join(str(self.data).reversed()))
        return self.data
    a = "qwerty"
    b = "asdfgh"
print(eval(input()  )
print(type(eval(input())))
