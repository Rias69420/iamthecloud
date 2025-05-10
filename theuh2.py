import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk # vajadzīgs lai varētu likt bildes iekša tkinter GUI
import os # importē os lai varētu tikt pie datora failiem

class TheUh(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tic Tac Toe")
        self.geometry("400x400")
        self.maxsize(400, 400) # Nosaka maximālo izmēru
        self.minsize(400, 400) # Nosaka minimālo izmēru
        
        self.label = tk.Label(self, text="Tic Tac Toe")
        self.label.pack()

        # Izveido kanvu priekšs zimēšans
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        # Saistīt peles klikšķus ar zīmējumu
        self.canvas.bind("<Button-1>", self.draw_x)  # Left-click priekšs "X"
        self.canvas.bind("<Button-3>", self.draw_o)  # Right-click priekšs "O"

        # Nosaka "path" priekšs bildes lai varētu lietot tic-tac-toe laukumu/zonu
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "theuh.jpg")
        self.auto_load_image(downloads_path)
    
    def auto_load_image(self, file_path): # automātiski ielāde bildi
        try:
            image = Image.open(file_path)
            image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Pārmaina izmēru bilde lai aizpildītu visu GUI zonu
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)  # zīme bilde jeb kanvu
        except Exception as e:
            print(f"Error loading image: {e}")

    def draw_x(self, event): # def lai varētu zīmet
        """Draws an X at the clicked position"""
        size = 40  # X izmērs
        self.canvas.create_line(event.x - size, event.y - size, event.x + size, event.y + size, width=3, fill="red")
        self.canvas.create_line(event.x + size, event.y - size, event.x - size, event.y + size, width=3, fill="red")

    def draw_o(self, event):
        """Draws an O at the clicked position"""
        size = 40  # Apļa rādius jeb izmērs
        self.canvas.create_oval(event.x - size, event.y - size, event.x + size, event.y + size, width=3, outline="blue")

app = TheUh()
app.mainloop()
