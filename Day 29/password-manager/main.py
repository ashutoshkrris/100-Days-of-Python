# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random
from tkinter import messagebox
from tkinter.constants import END
import tkinter as tk
import pyperclip

def password_generator():
    password = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase +
                                     string.digits) for _ in range(12))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name, message=f"These are the details entered : \n\nEmail: {email} \nPassword: {password} \n\nIs it OK to save?")

        if is_ok:
            with open("passwords.txt", "a") as file_data:
                file_data.write(f"{website_name} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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
