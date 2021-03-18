import tkinter as tk
import re


full_num = re.compile(r"[-+]?(?:(?:\d*\.\d+)|(?:\d+\.?))?", re.ASCII)


class Application(tk.Frame):
    """Sample tkinter application class"""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize"""
        super().__init__(master, **kwargs)
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


class App(Application):
    def create_widgets(self):
        num = self.register(self.num)
        self.S = tk.StringVar()

        self.E = tk.Entry(self, textvariable=self.S, validate='all', validatecommand=(num, "%P", "%S", "%V"))
        self.E.grid(columnspan=2)

        self.L = tk.Label(self, text="only int or float")
        self.L.grid(row=1, column=0)

        self.Q = tk.Button(self, text="Quit", command=self.big_quit)
        self.Q.grid(row=1, column=1)

    def big_quit(self):
        answer = self.S.get()
        if answer in ["", "-", "+"]:
            print(0)
        else:
            print(eval(answer))
        self.quit()

    def num(self, new, text, act):
        #print(new, text, act)
        if act == "key":
            matching = full_num.fullmatch(new)
            #print(matching)
            if matching:
                return True
            else:
                return False
        else:
            return True


app = App(title="Sample application")
app.mainloop()
