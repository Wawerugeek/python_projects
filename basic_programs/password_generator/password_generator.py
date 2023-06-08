#!/usr/bin/python3

import random
import tkinter as tk
import string
import pyperclip

def password_generate(leng):
    valid_char = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.digits) + random.choice(string.ascii_letters) + random.choice(string.punctuation)
    r_length = leng - 2
    password += ''.join(random.sample(valid_char, r_length))
    password_see.config(text=password)

def copy_password():
    password = password_see.cget("text")
    pyperclip.copy(password)

def get_len():
    if len1.get() == 1:
        password_generate(4)
    elif len2.get() == 1:
        password_generate(6)
    elif len3.get() == 1:
        password_generate(8)
    else:
        password_generate(6)

window = tk.Tk()
window.title('Password Generator')
window.geometry('500x500')

password_see = tk.Label(window, font=('normal', 10), text='')
password_see.pack()


len1 = tk.IntVar()
len2 = tk.IntVar()
len3 = tk.IntVar()

generate_button = tk.Button(window, text='Generate', font=('normal', 10), bg='yellow', command=get_len)
generate_button.pack()

checkbutton1 = tk.Checkbutton(window, text='4 characters', variable=len1, onvalue=1, offvalue=0)
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(window, text='6 characters', variable=len2, onvalue=1, offvalue=0)
checkbutton2.pack()

checkbutton3 = tk.Checkbutton(window, text='8 characters', variable=len3, onvalue=1, offvalue=0)
checkbutton3.pack()

copy_button = tk.Button(window, text='Copy Password', font=('normal', 10), bg="blue", command=copy_password)
copy_button.pack()

window.mainloop()

