import tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.choice = tkinter.StringVar()
        self.option_list = ('One', 'Two', 'Three', "Four")
        self.choice.set(self.option_list[0])

        self.quit_button = tkinter.Button(self, text='Quit', command=self.quit_button_func)
        self.label_1 = tkinter.Label(self, textvariable=self.choice)
        self.next_item_button = tkinter.Button(self, text='Next item', command=self.next_item_handler)
        self.drop_down = tkinter.OptionMenu(self, self.choice, *self.option_list)

        self.quit_button.grid()
        self.label_1.grid()
        self.next_item_button.grid()
        self.drop_down.grid()

    def quit_button_func(self):
        """Завершает выполнение программы"""
        self.quit()

    def next_item_handler(self):
        """Обработчик нажатия кнопки Next item"""
        self.choice.set(self.option_list[(self.option_list.index(self.choice.get()) + 1) % len(self.option_list)])


app = Application()
app.master.title('Application')
app.mainloop()
