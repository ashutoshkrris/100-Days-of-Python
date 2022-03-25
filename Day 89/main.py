from tkinter import Tk, Label, Text
from tkinter.constants import END, WORD, CENTER

timer = None


class DisappearingTextApp:

    def __init__(self):
        self.window = Tk()
        self.window.config(bg='#F6E7D8', padx=80, pady=30)
        self.window.title('Disappearing Text Writing App')
        self.display_heading()
        self.display_textbox()
        self.display_timer()

    ######## UI Methods Start ########

    def display_heading(self):
        heading_label = Label(text='Disappearing Text App', font=(
            "Courier", 16, 'bold'), bg='#F6E7D8', fg='#874356')
        heading_label.grid(row=0, column=1, pady=10)

    def display_textbox(self):
        self.textbox = Text(width=80, height=20, wrap=WORD,
                            padx=10, pady=10, bd=5)
        self.textbox.tag_config('green', foreground='green')
        self.textbox.tag_config('yellow', foreground='yellow')
        self.textbox.tag_config('red', foreground='red')
        self.textbox.bind('<KeyRelease>', self.callback)
        self.textbox.grid(row=1, column=0, columnspan=3)

    def display_timer(self):
        self.timer_label = Label(text='', font=(
            "Courier", 16, 'bold'), bg='#F6E7D8', fg='#874356')
        self.timer_label.grid(row=2, column=1, pady=10)

    ######## UI Methods End ########

    ######## Utility Methods Start ########

    def delete_text(self):
        self.window.after_cancel(timer)
        self.timer_label.config(text='Your Text Has Been Deleted!', fg='red')
        self.textbox.delete(1.0, END)

    def count(self, time):
        global timer

        for tag in self.textbox.tag_names():
            self.textbox.tag_remove(tag, "1.0", "end")

        self.timer_label.config(text=f'Time Left: {time}', fg='#874356')

        if time == 3:
            self.textbox.tag_add('green', '1.0', 'end')
        elif time == 2:
            self.textbox.tag_add('yellow', '1.0', 'end')
        elif time == 1:
            self.textbox.tag_add('red', '1.0', 'end')

        if time > 0:
            timer = self.window.after(1000, self.count, time-1)
        else:
            self.delete_text()

    def callback(self, *args):
        if timer:
            self.window.after_cancel(timer)
        if len(self.textbox.get(1.0, END)) != 1:
            self.count(5)

    ######## Utility Methods End ########


if __name__ == '__main__':
    app = DisappearingTextApp()
    app.window.mainloop()
