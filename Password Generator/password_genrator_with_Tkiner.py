import json
from tkinter import *
from tkinter import messagebox
import random


# -----------------------------------------------------------------------------------------------------------------
def GeneratePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letter = random.randint(8, 10)
    nr_number = random.randint(2, 4)
    nr_symbol = random.randint(2, 4)

    password_list = []
    [password_list.append(random.choice(letters)) for char in range(nr_letter)]
    [password_list.append(random.choice(numbers)) for char in range(nr_number)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbol)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(0, password)
    return password


# -----------------------------------------------------------------------------------------------------------------
window = Tk()
window.title('Password Generator')
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text='Website')
web_label.grid(row=1, column=0)
email_user_label = Label(text='Email/Username')
email_user_label.grid(row=2, column=0)
pass_label = Label(text='Password')
pass_label.grid(row=3, column=0)

# entries
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1, padx=20)
email_user_entry = Entry(width=35)
email_user_entry.insert(0, "asmahin8@gmail.com")
email_user_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)


def save():
    web_data = web_entry.get()
    email_data = email_user_entry.get()
    pass_data = pass_entry.get()
    new_data = {
        web_data: {
            "email": email_data,
            "password": pass_data
        }
    }
    if len(web_data) == 0 or len(pass_data) < 8:
        messagebox.askretrycancel(title="Message", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# Search Function





# button
generate_button = Button(text="Generate Password", command=GeneratePassword)
generate_button.grid(row=3, column=2)
add_button = Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search")
search_button.grid(row=1, column=2)

window.mainloop()
