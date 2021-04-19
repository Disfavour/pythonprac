import tkinter as tk
import gettext


gettext.install("click", ".", names=("ngettext",))


class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
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
        '''Create all the widgets'''

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.Q = tk.Button(self, text=_("Quit"), command=self.master.quit)
        self.Q.grid()

        self.press_me = tk.Button(self, text=_("Press me"), command=self.press)
        self.press_me.grid()
        
        self.count = 0
        self.text = tk.StringVar()
        self.text.set(ngettext("%d time clicked", "%d times clicked", self.count) % (self.count,))

        self.label = tk.Label(self, textvariable=self.text)
        self.label.grid()

    def press(self):
        self.count += 1
        self.text.set(ngettext("%d time clicked", "%d times clicked", self.count) % (self.count,))


app = App(title=_("Sample application"))
app.mainloop()

