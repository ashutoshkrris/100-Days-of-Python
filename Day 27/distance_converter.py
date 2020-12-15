from tkinter import *


def converter():
    miles = miles_input.get()
    kms = float(miles)*1.609
    kilometres_result_label["text"] = str(kms)


window = Tk()
window.title("Miles to Kilometres Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometres_result_label = Label(text="0")
kilometres_result_label.grid(column=1, row=1)

kilometres_label = Label(text="Kms")
kilometres_label.grid(column=2, row=1)

convert_button = Button(text="Convert", command=converter)
convert_button.grid(column=1, row=2)

window.mainloop()
