from tkinter import *

window = Tk()
window.title('Mile to KM Converter')
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)


def calculation():
    miles = float(input.get())
    km = miles*1.609
    label3.config(text = f"{km}")


# Enteries

input = Entry(width=10)
input.grid(row=0, column=3, sticky=W, padx=150)

# Text
label1 = Label(text='miles')
label1.grid(row=0, column=11)

# label

label = Label(text='')
label.grid(column=0, row=0)

label2 = Label(text='is equal to')
label2.grid(row=2, column=0)

label3 = Label(text='0')
label3.grid(row=2, column=3)

# button

button = Button(text='Calculate', command=calculation)
button.grid(row=5, column=3, pady=20)

window.mainloop()
