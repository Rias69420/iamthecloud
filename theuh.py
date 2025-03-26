import tkinter as tk

class TheUh(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("The Uh")
        self.geometry("400x300")
        self.label = tk.Label(self, text="The Uh")
        self.label.pack()
        self.button = tk.Button(self, text="Quit", command=self.quit)
        self.button.pack()
        

app = TheUh()
app.mainloop()