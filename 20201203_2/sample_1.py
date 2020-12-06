class C:
    A: int = 100500
    def __init__(self, var: int):
        self.A = var
    def fun(self, par: int, other: str) -> str:
        return (self.A+par) * other

