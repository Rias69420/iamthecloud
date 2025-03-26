import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class TheUh(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("The Uh")
        self.geometry("400x400")
        
        self.label = tk.Label(self, text="The Uh")
        self.label.pack()
        
        self.image_label = tk.Label(self)
        self.image_label.pack()
        
        self.image_button = tk.Button(self, text="Select Image", command=self.load_image)
        self.image_button.pack()
        
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()
    
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

app = TheUh()
app.mainloop()
