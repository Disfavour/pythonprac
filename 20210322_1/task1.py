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
        self.strings = self.text.get("1.0", tk.END).split("\n")
        for i, s in enumerate(self.strings):
            words = s.split(" ")
            if s.startswith("#") or words[0] in self.objects:
                self.set_tag("incorrect", "correct", i)
            else:
                self.set_tag("correct", "incorrect", i)

    def set_tag(self, tag_rem, tag_set, ind):
        self.text.tag_remove(tag_rem, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")
        self.text.tag_add(tag_set, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")

    def motion_handler(self, event):
        coords = self.text.index(tk.CURRENT).split('.')
        curx, words = int(coords[0]), [""]
        if self.strings[0] != '':
            words = self.strings[curx-1].split(" ")
        if words[0] in self.objects:
            if words[0] == "oval" or words[0] == "rectangle":
                self.help.set("Draw " + words[0] + ": " + words[0] + " x0 y0 x1 y1 outline='color' fill='color' width='width'")
            elif words[0] == "line":
                self.help.set("Draw line: line x0 y0 x1 y1 width='width' fill='color'")
        elif words[0].startswith("#"):
            self.help.set("Comment")
        elif self.strings[0] != '' and self.strings[curx-1].isspace() is True or words[0] == '':
            self.help.set("Empty string")
        else:
            self.help.set("Not CCL string")

    def draw_objects(self):
        self.strings = self.text.get("1.0", tk.END).split("\n")
        for i, s in enumerate(self.strings):
            words = s.split(" ")
            if words[0] in self.objects:
                try:
                    eval(f"self.paint.create_{words[0]}({','.join(words[1:])})")
                    self.set_tag("incorrect", "correct", i)
                except:
                    self.set_tag("correct", "incorrect", i)
            elif s.startswith("#"):
                self.set_tag("incorrect", "correct", i)
            else:
                self.set_tag("correct", "incorrect", i)

    def run_handler(self):
        self.clear_handler()
        self.draw_objects()

    def clear_handler(self):
        for fid in self.paint.find_all():
            self.paint.delete(fid)


app = App(title="CCL interpreter")
app.mainloop()
