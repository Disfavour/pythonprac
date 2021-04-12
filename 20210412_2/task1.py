"""Module for something."""
import tkinter as tk
import logic


class Application(tk.Frame):
    """Sample tkinter application class."""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize."""
        self.logic = logic.Logic()
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
        """Create all the widgets."""


class App(Application):
    """Sample tkinter application class."""

    def create_widgets(self):
        """Create all the widgets."""
        analyze = self.register(self.logic.logic_analyze)

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

    def insert_func(self):
        """Insert text in entry."""
        self.logic.logic_insert_func(self.editor, tk.END, self.choice.get())

    def show_func(self):
        """Print text in label."""
        self.logic.logic_label(self.label_text, self.editor.get())

    def in_label(self, event):
        """Print text in label."""
        self.logic.logic_label(self.label_text, "Hi Mouse")

    def out_label(self, event):
        """Print text in label."""
        self.logic.logic_label(self.label_text, "Bye Mouse")


def main():
    """Do all work."""
    app = App(title="Sample application")
    app.mainloop()


if __name__ == "__main__":
    main()
