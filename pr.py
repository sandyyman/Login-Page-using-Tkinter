import os
from tkinter import *
from functools import partial




def validateLogin(username, password):
    print("username entered:", username.get())
    print("password entered:", password.get())
    return

#
Sup = Tk()

NamImjVav = PhotoImage(file="background32.png")
Label(Sup, image=NamImjVav ,width=900 ,height=1265).pack()

Sup.title("LOGIN")
Sup.title("Window Login")
Sup.geometry("1265x900")
Sup.configure(background="#a588fd")

# img = Image.open("D:\Programs\Project\background.gif")
# bg = Image.PhotoImage(img)
# label2 = Label(Sup, image=bg)
# Label.place(x=0, y=0)


label1 = Label(
    Sup,
    text="SIGN IN USING THE CREDENTIALS",
    font={"Open Sans"},
    borderwidth=0,
    height=0,
    width=30
    # background="#a588fd",
)
label1.place(x=450)
usernameLabel = Label(Sup, text="USERNAME").place(x=350, y=300)
username = StringVar()
usernameEntry = Entry(Sup, textvariable=username, width=80).place(x=450, y=300)

PasswordLabel = Label(Sup, text="PASSWORD").place(x=350, y=350)
password = StringVar()
passwordEntry = Entry(Sup, textvariable=password, show="*", width=80).place(
    x=450, y=350
)

partial(validateLogin, username, password)
validateLogin = partial(validateLogin, username, password)


loginButton = Button(Sup, text="LOGIN", command=validateLogin).place(x=450, y=400)



Sup.mainloop()
