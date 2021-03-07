import tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quit_button = tkinter.Button(self, text='Quit', command=self.quit_button_func)
        self.label_1 = tkinter.Label(self, text="<MenuItem>")
        self.next_item_button = tkinter.Button(self, text='Next item', command=self.next_item_handler)

        self.quit_button.grid()
        self.label_1.grid()
        self.next_item_button.grid()

    def quit_button_func(self):
        """Завершает выполнение программы"""
        pass

    def next_item_handler(self):
        """Обработчик нажатия кнопки Next item"""
        pass


app = Application()
app.master.title('Application')
app.mainloop()
