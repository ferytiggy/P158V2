from tkinter import *
from tkinter.messagebox import*
from PIL import ImageTk, Image

root=Tk()
root.title("Autentificación de tarjeta de crédito")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("credit.jpg"))
label = Label(root, image=img)


def authentication():
        input_value = int(input_box.get())
        showinfo("Alerta","Se acepta la tarjeta de crédito.")
        try:
            
            get_info = input_box.get
            
        except:
            
            showinfo("Aceptada", "Su tarjeta ha sido aceptada")
        
        
btn = Button(root, text = "comprobar la tarjeta de crédito", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()