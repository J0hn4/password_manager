from tkinter import*
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)



def password_generator():
    password_entry.delete(0, 'end')

    password_list = []

    password_letters = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    password_symbols = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    password_numbers = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]



    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    pyperclip.copy(password)
    password_entry.insert(0, password)
    # print(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        is_ok = False
        messagebox.showinfo(title="Missing Information", message="You have not entered a website.\n Please input a website.")
    elif len(password) == 0:
        is_ok = False
        messagebox.showinfo(title="Missing Information", message="You have not entered a password.\n Please input a password.")
    elif len(email) == 0:
        is_ok = False
        messagebox.showinfo(title="Missing Information", message="You have not entered an email.\n Please input an email.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website_entry.get()} | ")
                f.write(f" {email_entry.get()} | ")
                f.write(f"{password_entry.get()} \n")
            website_entry.delete(0,'end')
            email_entry.delete(0,'end')
            email_entry.insert(0, "john@doe.com")
            password_entry.delete(0,'end')

#open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.geometry("250x250")
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, highlightthickness= 0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
# canvas.create_text(103, 130, text="00:00", fill="white", font=(f'{FONT_NAME} 35 bold'))
# timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)
# canvas.pack()


#website label
website_label = Label(text="Website: ")
# fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
website_label.grid(column=0, row=1)
# website_label.config(padx=10, pady=10)

#Email/username: Label
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row = 2)
# email_label.config(padx=10, pady=10)

#Password: label
password_label = Label(text="Password: ")
password_label.grid(column=0, row = 3)
# password_label.config(padx=10, pady=10)


# website entry input 0
website_entry = Entry(width=35)
print(website_entry.get())
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

# email input 1
email_entry = Entry(width=35)
print(email_entry.get())
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0,"john@doe.com")

# password input 2
password_entry = Entry(width=16)
print(password_entry.get())
password_entry.grid(column=1, row=3, sticky="EW")

#generate password button
generate_button = Button(text="Generate Password", width=16, command = password_generator)
generate_button.grid(column=2, row=3, sticky="EW")

#add button
add_button = Button(text="Add", width= 33, command=save)
add_button.grid(column=1, row=4, columnspan = 2, sticky="EW")


window.mainloop()