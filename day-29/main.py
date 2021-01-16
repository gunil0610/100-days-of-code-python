from tkinter import Tk, Canvas, PhotoImage, Entry, Label, Button, messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, 'end')
    password_input.insert(0, f"{password}")
    pyperclip.copy(f'{password}')
    messagebox.showinfo(
        title='Copied', message="Generated Password is copied to your clipboard!\nYou can paste it by Ctrl+V")

# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(
            title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f'These are the details entered: \nEmail:{email}\nPassword: {password}\nIs it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as file_object:
                file_object.write(f'{website} | {email} | {password}\n')
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0, pady=(0, 10))

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0, pady=(0, 10))

password_label = Label(text='Password:')
password_label.grid(row=3, column=0, pady=(0, 10))

# Entries
website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2,
                   sticky="WE", ipady=5, pady=(0, 10), padx=(10, 0))
website_input.focus()

email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2,
                 sticky="WE", ipady=5, pady=(0, 10), padx=(10, 0))
email_input.insert(0, 'example@example.com')

password_input = Entry(width=30)
password_input.grid(row=3, column=1, sticky="WE",
                    ipady=5, pady=(0, 10), padx=10)

# Buttons
generate_password_btn = Button(
    text='Generate Password', justify="left", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky="we", pady=(0, 10), ipady=2)

add_button = Button(text='Add', width=35, command=save_file)
add_button.grid(row=4, column=1, columnspan=2,
                sticky="we", pady=(0, 10), ipady=2, padx=(10, 0))


window.mainloop()
