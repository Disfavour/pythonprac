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
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        """Create all the widgets"""


class App(Application):
    def create_widgets(self):
        super().create_widgets()

        self.help = tk.StringVar()
        self.help.set("Help label")

        self.text = tk.Text(self)
        self.paint = tk.Canvas(self)
        self.help_label = tk.Label(self, textvariable=self.help)

        self.run = tk.Button(self, text="RUN", command=self.run_handler)
        self.clear = tk.Button(self, text="CLEAR", command=self.clear_handler)
        self.Q = tk.Button(self, text="QUIT", command=self.master.quit)

        self.strings = [""]
        self.objects = ["oval", "rectangle", "line"]

        self.text.grid(row=0, column=0, sticky="news")
        self.paint.grid(row=0, column=1, sticky="news")
        self.help_label.grid(row=1, column=0, sticky="w")
        self.run.grid(row=2, column=0, sticky="w")
        self.clear.grid(row=1, column=1, sticky="w")
        self.Q.grid(row=3, column=0, sticky="w")

        self.text.bind("<KeyPress>", self.button_handler)
        self.text.bind("<Motion>", self.motion_handler)

        self.text.tag_config("incorrect", foreground="red")
        self.text.tag_config("correct", foreground="green")

    def button_handler(self, event):
        pass

    def motion_handler(self, event):
        pass

    def run_handler(self):
        pass

    def clear_handler(self):
        pass


app = App(title="CCL interpreter")
app.mainloop()