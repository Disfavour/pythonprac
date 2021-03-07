import tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()


app = Application()
app.master.title('Application')
app.mainloop()
