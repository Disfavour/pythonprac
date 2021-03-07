import tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quit_button = tkinter.Button(self, text='Quit', command=self.quit_button_func)
        self.quit_button.grid()

    def quit_button_func(self):
        """Завершает выполнение программы"""
        pass


app = Application()
app.master.title('Application')
app.mainloop()
