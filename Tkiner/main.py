from tkinter import *

window = Tk()
window.title('GUI Interface')
window.minsize(width=400, height=400)

# label
my_label = Label(text='This is label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)


def clickbutton():
    my_label.config(text=input.get())


# new button
my_button2 = Button(text='Button 2')
my_button2.grid(column=3, row=0)

# button
my_button = Button(text='click me', command=clickbutton)
my_button.grid(column=1, row=50)



# Entry
input = Entry()
input.grid(column=5, row=9)

window.mainloop()
