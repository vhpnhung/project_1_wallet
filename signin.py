import tkinter as tk
from tkinter import BOTH, ttk


win_signin = tk.Tk()
win_signin.title("Wisexpend - Sign in")
win_signin.geometry("300x150+500+200")
frame = ttk.Frame(win_signin, borderwidth=5, relief="ridge")


var_signin = tk.IntVar()
username = "nhung"
password = "123"



def signin_hide_pass():
    if var_signin.get() == 1:
        en_pass_signin.config(show="")
    else:
        en_pass_signin.config(show="*")
    
def check_signin():
    input_username = en_user_signin.get()
    input_password = en_pass_signin.get()
    if input_username == "" or input_password == "":
        lab_message_signin.config(text="Missing information")
    elif input_username != username:
        lab_message_signin.config(text="Username does not exist")
    elif input_password != password:
        lab_message_signin.config(text="Password is incorrect")
    else:
        win_signin.destroy()
        import menu
        import f_add
        import f_report
        import f_snl



lab_signin = tk.Label(text="Login")
lab_signin.grid(row=0, column=0, columnspan=11)

lab_message_signin = tk.Label(text="Please sign in")
lab_message_signin.grid(row=1, column=0, columnspan=11)

lab_user_signin = tk.Label(text="Username")
lab_user_signin.grid(row=3, column=0, columnspan=4)

en_user_signin = tk.Entry()
en_user_signin.grid(row=3, column=4, columnspan=5)

lab_pass_signin = tk.Label(text="Password")
lab_pass_signin.grid(row=4, column=0, columnspan=4)

en_pass_signin = tk.Entry(show="*")
en_pass_signin.grid(row=4, column=4, columnspan=5)

cb_hide_signin = ttk.Checkbutton(text="Show password", command=signin_hide_pass, variable=var_signin, onvalue=1, offvalue=2)
cb_hide_signin.grid(row=4, column=9, columnspan=2)

b_signin = ttk.Button(text="Sign in", command=check_signin)
b_signin.grid(row=6, column=0, columnspan=11) 


win_signin.mainloop()