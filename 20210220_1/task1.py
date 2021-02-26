import tkinter as tk
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.time = tk.StringVar()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeButton = tk.Button(self, text="Time", command=self.settime)
        self.timeLabel = tk.Label(self, textvariable=self.time)

        self.timeButton.grid()
        self.quitButton.grid(row=0, column=1)
        self.timeLabel.grid(columnspan=2)

    def settime(self):
        self.time.set(time.strftime("%c"))


app = Application()
app.master.title('Sample timer application')
app.mainloop()
