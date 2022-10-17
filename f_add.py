import tkinter as tk
from tkinter import BOTH, BOTTOM, END, ttk
from data_add import list_of_type, add

win_add = tk.Tk()
win_add.title("Wisexpend - Add")
win_add.geometry("500x500+400+80")

var = tk.IntVar()
type_add = tk.StringVar()


# khong cho nguoi dung nhap, chi duoc xem sheet
def nothing():
    b_enter_add.destroy()
    en_detail.delete(0, END)
    en_detail.config(state="disable")
    en_money.delete(0, END)
    en_money.config(state="disable")

# hien thi income
def i_view():
    # gan gia tri
    i_type = "income"
    i_choice = combo_type_add.get().lower()
    i_detail = en_detail.get().lower()
    i_money = int(en_money.get())
    # calculate
    add.count(i_type, i_choice, i_detail, i_money)
    # view
    for what in add.income[i_choice]:
        lab_what_view = tk.Label(fr_what_view, text=what)
        lab_what_view.pack(side="left")
        lab_money_view = tk.Label(fr_what_view, text=add.income[i_choice][what])
        lab_money_view.pack(side="right")
    # balance
    lab_balance_view.config(text=add.balance(i_type,i_detail))
    # reset lai sau khi da nhap xong
    def reset():
        en_detail.config(state="normal")
        en_money.config(state="normal")
        b_reset.destroy()
        lab_what_view.destroy()
        lab_money_view.destroy()
    nothing()
    b_reset.config(command=reset)
    b_reset.grid(row=18, column=0, columnspan=10)

def show_add():
    if var.get() == 1: # CHON INCOME
        # combobox
        combo_type_add["value"]=list_of_type.list_of_income
        combo_type_add.config(state="readonly")
        # input
        b_enter_add.grid(row=18, column=0, columnspan=10)
        print("show cai view + change data EARNING, dung den pan_what_view va pan_money_view, va lam them cai total income, cong lai balance")
    else: # CHON EXPENSE
        combo_type_add["value"]=list_of_type.list_of_expense
        combo_type_add.config(state="readonly")
        print("show cai view + change data EXOEND, dung den pan_what_view va pan_money_view, va lam them cai total expenditure, cong lai balance")

def add_back():
    win_add.destroy()
    from menu import win_menu
    win_menu.mainloop()


# TAO GIAO DIEN
lab_header = tk.Label(text="ADD NEW CASH", font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill=BOTH)

lab_intro_add = tk.Label(text="Manage your wallet with Wisexpend", pady=10, font="Sans 10 bold italic")
lab_intro_add.pack()

fr_add = tk.Frame(height=5, pady=80)
fr_add.pack()

fr_select = tk.Frame(fr_add, pady=20, padx=20, relief="ridge", bd=3)
fr_select.grid(row=0, column=0, columnspan=10)

b_enter_add = ttk.Button(fr_select, text=">>>", command=i_view)
b_reset = ttk.Button(fr_select, text="Continue")

fr_space = tk.Frame(fr_add) # separate fr_select and fr_view
fr_select.grid(row=0, column=10, columnspan=8)

fr_view = tk.Frame(fr_add, padx=20, pady=50, relief="ridge", bd=3)
fr_view.grid(row=0, column=18, columnspan=10)

# KHUNG ADD
sel_earning_add = tk.Radiobutton(fr_select, text="Earning", variable=var, value=1, command=show_add)
sel_earning_add.grid(row=0, column=0, columnspan=2)

sel_expenditure_add = tk.Radiobutton(fr_select, text="Expenditure", variable=var, value=0, command=show_add)
sel_expenditure_add.grid(row=0, column=3, columnspan=2)

combo_type_add = ttk.Combobox(fr_select, textvariable=type_add)
combo_type_add.grid(row=9,column=1,columnspan=4)

lab_detail = tk.Label(fr_select, text="Detail   ", font="Roboto 8 bold")
lab_detail.grid(row=11,column=0,columnspan=1)

en_detail = tk.Entry(fr_select)
en_detail.grid(row=13, column=0, columnspan=10)

lab_money = tk.Label(fr_select, text="Amount", font="Roboto 8 bold")
lab_money.grid(row=15,column=0,columnspan=1)

en_money = tk.Entry(fr_select)
en_money.grid(row=16, column=0, columnspan=10)

lab_sep = tk.Label(fr_select, text=" ")
lab_sep.grid(row=17, column=0, columnspan=10)


# KHUNG VIEW
fr_what_view = tk.Frame(fr_view)
fr_what_view.grid(row=0, column=0, columnspan=5)

fr_money_view = tk.Frame(fr_view)
fr_money_view.grid(row=0, column=6, columnspan=5)

lab_balance_view = tk.Label(fr_view, text="0", font="Roboto 10 bold")
lab_balance_view.grid(row=20, column=0, columnspan=10)

b_back = ttk.Button(text="Back", command=add_back)
b_back.pack()

lab_footer = tk.Label(text="", background="#ffdb58",height=2)
lab_footer.pack(fill=BOTH, side=BOTTOM)

win_add.mainloop()