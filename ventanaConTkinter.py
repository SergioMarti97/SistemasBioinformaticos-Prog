from tkinter import *
import numpy as np
from PIL import Image, ImageTk

#print("Creando la ventana con tkinter")
#window = tk.Tk()

#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()

#window.mainloop()
w, h = 800, 600

root = Tk()
c = Canvas(root, width=w, height=h)
c.pack()

data = np.zeros((w, h, 3), dtype=np.uint8)

x, y = 1, 0

data[x][y] = 0xffff

img = Image.fromarray(data, 'RGB')
tkImage = ImageTk.PhotoImage(img)
c.create_image(20, 20, image=tkImage, anchor=NW)

mainloop()