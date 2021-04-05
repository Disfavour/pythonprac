import tkinter as tk


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
        analyze = self.register(self.analyze)

        self.label_text = tk.StringVar()
        self.label_text.set("Default")

        self.choice = tk.StringVar()
        self.options = ["One", "Two", "Three"]
        self.choice.set(self.options[0])

        self.editor = tk.Entry(
                self, validate='all', validatecommand=(analyze, "%P"))
        self.editor.grid()

        self.menu = tk.OptionMenu(self, self.choice, *self.options)
        self.menu.grid()

        self.insert = tk.Button(self, text='Insert', command=self.insert_func)
        self.insert.grid()

        self.show = tk.Button(self, text='Show', command=self.show_func)
        self.show.grid()

        self.label = tk.Label(
                self, textvariable=self.label_text, takefocus=1,
                highlightthickness=2)
        self.label.bind("<Enter>", self.in_label)
        self.label.bind("<Leave>", self.out_label)
        self.label.grid()

    def analyze(self, new):
        if len(new) > 10:
            return False
        else:
            return True

    def insert_func(self):
        self.editor.insert(tk.END, self.choice.get())

    def show_func(self):
        self.label_text.set(self.editor.get())

    def dump(self, *args, **kwargs):
        print(args, kwargs)
        print(123)

    def in_label(self, a):
        self.label_text.set("Hi Mouse")

    def out_label(self, a):
        self.label_text.set("Bye Mouse")


def main():
    app = App(title="Sample application")
    app.mainloop()


if __name__ == "__main__":
    main()
