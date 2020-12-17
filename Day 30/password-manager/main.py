# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random
from tkinter import messagebox
from tkinter.constants import END
import tkinter as tk
import pyperclip
import json


def password_generator():
    password = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase +
                                     string.digits) for _ in range(12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    pass_dict = {
        website_name: {
            "email": email,
            "password": password
        }
    }

    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name, message=f"These are the details entered : \n\nEmail: {email} \nPassword: {password} \n\nIs it OK to save?")

        if is_ok:
            try:
                # Reading old data
                with open("passwords.json", "r") as file_data:
                    data = json.load(file_data)
            except FileNotFoundError:
                # Creating new file
                with open("passwords.json", "w") as file_data:
                    json.dump(pass_dict, file_data, indent=4)
            else:
                data.update(pass_dict)
                # Saving updated file
                with open("passwords.json", "w") as file_data:
                    json.dump(data, file_data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

EMAIL_FIELD = "email@example.com"

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website : ")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email / Username : ")
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password : ")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search = tk.Button(
    text="Search",width=13, command=find_password)
search.grid(row=1, column=2)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, pady=5, columnspan=2)
email_entry.insert(0, EMAIL_FIELD)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password = tk.Button(
    text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

add_button = tk.Button(text="Add Password", width=36, command=save)
add_button.grid(row=4, column=1, pady=5, columnspan=2)


window.mainloop()
