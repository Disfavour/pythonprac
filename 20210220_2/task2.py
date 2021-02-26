import tkinter as tk
import subprocess


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.x = tk.StringVar()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.dir_button = tk.Button(self, text="dir", command=self.dir_func)
        self.date_button = tk.Button(self, text="date", command=self.date_func)
        self.git_button = tk.Button(self, text="git", command=self.git_func)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)

        self.funcplace = tk.Label(self, textvariable=self.x)

        self.dir_button.grid()
        self.date_button.grid()
        self.git_button.grid()
        self.funcplace.grid()
        self.quitButton.grid()

    def dir_func(self):
        process = subprocess.run("dir", capture_output=True)
        self.x.set(process.stdout.decode()[:-1])

    def date_func(self):
        process = subprocess.run("date", capture_output=True)
        self.x.set(process.stdout.decode()[:-1])

    def git_func(self):
        process = subprocess.run("git", capture_output=True)
        self.x.set(process.stdout.decode()[:-1])


app = Application()
app.master.title('Sample application')
app.mainloop()
