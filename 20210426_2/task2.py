import tkinter as tk
import math


class View(tk.Frame):
    """Sample tkinter application class"""

    def __init__(self, master=None, model=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize"""
        super().__init__(master, **kwargs)
        self.model = model
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            for row in range(self.grid_size()[1]):
                self.columnconfigure(column, weight=1)
                self.rowconfigure(row, weight=1)

    def create_widgets(self):
        """Create all the widgets"""
        self.answer = tk.StringVar()
        self.answer.set("result here")

        self.a = tk.Entry(self)
        self.a.grid(row=0, column=0)

        self.label_a = tk.Label(self, text="x^2 + ")
        self.label_a.grid(row=0, column=1)

        self.b = tk.Entry(self)
        self.b.grid(row=0, column=2)

        self.label_a = tk.Label(self, text="x + ")
        self.label_a.grid(row=0, column=3)

        self.c = tk.Entry(self)
        self.c.grid(row=0, column=4)

        self.label_a = tk.Label(self, text=" = 0")
        self.label_a.grid(row=0, column=5)

        self.lebel_answer = tk.Label(self, textvariable=self.answer)
        self.lebel_answer.grid(row=1, column=1, columnspan=4)

        self.calc = tk.Button(self, text="Вычислить", command=self.get_answer)
        self.calc.grid(row=1, column=0)

    def get_answer(self):
        a = self.a.get()
        b = self.b.get()
        c = self.c.get()
        a = float(a)
        b = float(b)
        c = float(c)
        self.answer.set(self.model.calculate(a, b, c))


class Model:
    def setup(self, view):
        self.view = view

    def calculate(self, a, b, c):
        self.answer = None
        self.analyze(a, b, c)
        return self.answer

    def analyze(self, a, b, c):
        if a != 0:
            self.answer = self.full(a, b, c)
        elif b != 0:
            self.answer = self.linear(b, c)
        elif c == 0:
            self.answer = "∞"
        else:
            self.answer = "∅"

    def full(self, a, b, c):
        D = b * b - 4 * a * c
        if D > 0:
            x1 = (-b - math.sqrt(D)) / (2 * a)
            x2 = (-b + math.sqrt(D)) / (2 * a)
            ans = f"{min(x1, x2)} {max(x1, x2)}"
            return ans
        elif D == 0:
            x = -b / (2 * a)
            return f"{x}"
        else:
            return "∅"

    def linear(self, b, c):
        x = -c / b
        return f"{x}"


if __name__ == "__main__":
    m = Model()
    v = View(model=m, title="quadratic equation")
    m.setup(v)
    v.mainloop()
