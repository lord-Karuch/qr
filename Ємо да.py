import qrcode
from tkinter import *
from PIL import Image, ImageTk

def aa(event):
    cc = a.get()
    ddd = "aaa.png"
    dd = qrcode. make(cc)
    dd.save(ddd)

    image = Image.open(r"aaa.png")
    photo = ImageTk.PhotoImage(image)

    label = Label(mainloop_worker, image=photo)
    label.image = photo
    label.grid(row=3)


mainloop_worker = Tk()
mainloop_worker.geometry("400x400")
a = Entry(mainloop_worker)
a.grid(row=2, column=0)
b = Button(mainloop_worker, text="result")
b.grid(row=1, column=0)
b.bind("<Button-1>", aa)


mainloop_worker.mainloop()