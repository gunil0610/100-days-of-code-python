from tkinter import *

# window = Tk()
# window.title('GUI')
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# my_label = Label(text='I am a label', font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)


# def button_clicked():
#     my_label.config(text=input.get())


# button = Button(text='Click Me', command=button_clicked)
# button.grid(column=1, row=1)

# new_button = Button(text='Click Me', command=button_clicked)
# new_button.grid(column=2, row=0)

# input = Entry(width=10)
# input.grid(column=3, row=2)


window = Tk()
window.title('Mile to Km Converter')
# window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

input = Entry(width=7)
input.grid(column=1, row=0)

label_1 = Label(text='Miles')
label_1.grid(column=2, row=0)

label_2 = Label(text='is equal to')
label_2.grid(column=0, row=1)

label_3 = Label(text='Km')
label_3.grid(column=2, row=1)

kilometer = Label(text='0')
kilometer.grid(column=1, row=1)


def on_click():
    kilometer.config(text=round(float(input.get())*1.609, 2))


button = Button(text='Calculate', command=on_click)
button.grid(column=1, row=2)

window.mainloop()
