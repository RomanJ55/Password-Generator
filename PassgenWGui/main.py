from tkinter import *
import pyperclip
import random
import string

root = Tk()
root.geometry("500x320+700+300")
root.resizable(0, 0)
root.title("Passgen")

passStr = StringVar()
passLength = IntVar(root, value=4)
copyText = StringVar()


def generatePass():
    password = ""
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(passLength.get() - 4):
        password = password + \
            random.choice(string.ascii_uppercase +
                          string.ascii_lowercase+string.digits+string.punctuation)
    passStr.set(password)
    copyText.set("")


def copyPasstoClipboard():
    pyperclip.copy(passStr.get())
    copyText.set("Password copied!")


Label(root, text="Password Generator", font="arial 14").pack(pady=5)
Label(root, text="Choose the length of Your desired Password(minimum 4):").place(
    x=10, y=45)
entryBox = Entry(root, textvariable=passLength, width=6)
entryBox.focus_set()
entryBox.place(x=330, y=47)
Button(root, text="Generate Password",
       command=generatePass, width=16).place(x=30, y=80)
Label(root, textvariable=passStr).place(x=330, y=80)
Button(root, text="Copy to Clipboard",
       command=copyPasstoClipboard, width=16).place(x=30, y=120)
Label(root, textvariable=copyText, fg="red").place(x=330, y=120)
Button(root, text="Exit", command=root.quit,
       font="arial 13", width=10).pack(pady=120)

root.mainloop()
