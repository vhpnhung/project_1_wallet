import tkinter as tk
from tkinter import BOTH, BOTTOM, ttk



win_add = tk.Tk()
win_add.title("Wisexpend - Add")
win_add.geometry("500x500+400+80")



var = tk.IntVar()
balance = 0



def show_add():
    if var.get() == 1:
        print("show cai view + change data EARNING, dung den pan_what_view va pan_money_view, va lam them cai total income, cong lai balance")
    else:
        print("show cai view + change data EXOEND, dung den pan_what_view va pan_money_view, va lam them cai total expenditure, cong lai balance")

def add_back():
    win_add.destroy()
    from menu import win_menu
    win_menu.mainloop()


#TAO GIAO DIEN
lab_header = tk.Label(text="ADD NEW CASH", font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill=BOTH)

lab_intro_add = tk.Label(text="Manage your wallet with Wisexpend", pady=10, font="Sans 10 bold italic")
lab_intro_add.pack()

fr_add = tk.Frame(height=5, pady=80)
fr_add.pack()

fr_select = tk.Frame(fr_add, pady=20, padx=20, relief="ridge", bd=3)
fr_select.grid(row=0, column=0, columnspan=10)

fr_space = tk.Frame(fr_add) # separate fr_select and fr_view
fr_select.grid(row=0, column=10, columnspan=8)

fr_view = tk.Frame(fr_add, padx=20, pady=50, relief="ridge", bd=3)
fr_view.grid(row=0, column=18, columnspan=10)

sel_earning_add = tk.Radiobutton(fr_select, text="Earning", variable=var, value=1, command=show_add)
sel_earning_add.grid(row=0, column=0, columnspan=2)

sel_expenditure_add = tk.Radiobutton(fr_select, text="Expenditure", variable=var, value=0, command=show_add)
sel_expenditure_add.grid(row=0, column=3, columnspan=2)

lab_detail = tk.Label(fr_select, text="Detail   ", font="Roboto 8 bold")
lab_detail.grid(row=9,column=0,columnspan=1)

en_detail = tk.Entry(fr_select)
en_detail.grid(row=10, column=0, columnspan=10)

lab_money = tk.Label(fr_select, text="Amount", font="Roboto 8 bold")
lab_money.grid(row=11,column=0,columnspan=1)

en_money = tk.Entry(fr_select)
en_money.grid(row=12, column=0, columnspan=10)

lab_sep = tk.Label(fr_select, text=" ")
lab_sep.grid(row=13, column=0, columnspan=10)

b_enter_add = ttk.Button(fr_select, text=">>>")
b_enter_add.grid(row=14, column=0, columnspan=10)

pan_what_view = tk.PanedWindow(fr_view, relief="ridge", bd=2)
pan_what_view.grid(row=0, column=0, columnspan=5)

pan_money_view = tk.PanedWindow(fr_view, relief="ridge", bd=2)
pan_what_view.grid(row=0, column=6, columnspan=5)

lab_balance_view = tk.Label(fr_view, text=f"BALANCE: {balance}", font="Roboto 10 bold")
lab_balance_view.grid(row=20, column=0, columnspan=10)

b_back = ttk.Button(text="Back", command=add_back)
b_back.pack()

lab_footer = tk.Label(text="", background="#ffdb58",height=2)
lab_footer.pack(fill=BOTH, side=BOTTOM)

win_add.mainloop()