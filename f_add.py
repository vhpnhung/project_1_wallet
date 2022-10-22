import tkinter as tk
from tkinter import BOTH, BOTTOM, END, ttk
from data_add import list_of_type, add

win_add = tk.Toplevel()
win_add.title("Wisexpend - Add")
win_add.geometry("500x500+400+80")

var = tk.IntVar()
type_add = tk.StringVar()


# khong cho nguoi dung nhap, chi duoc xem sheet
def cannot_enter():
    en_detail.delete(0, END)
    en_detail.config(state="disable")
    en_money.delete(0, END)
    en_money.config(state="disable")
    sel_earning_add.config(state="disable")
    sel_expenditure_add.config(state="disable")
    combo_type_add.config(state="disable")


def reset():
    en_detail.config(state="normal")
    en_money.config(state="normal")
    lab_what_view.config(text="")
    lab_money_view.config(text="")
    var.set(None)
    type_add.set(None)
    b_enter_add.config(state="disable", text="Add")
    sel_earning_add.config(state="normal")
    sel_expenditure_add.config(state="normal")
    combo_type_add.config(state="normal")
    # type = show_add()
    # if type == "income":
    #     b_enter_add.config(text="Add", command=i_view)
    # else:
    #     b_enter_add.config(text="Add", command=e_view)
    
# hien thi income
def i_view():
    # gan gia tri
    i_choice = combo_type_add.get().lower()
    i_detail = en_detail.get().lower()
    i_money = int(en_money.get())
    # them vao dsach
    add.count(type, i_choice, i_detail, i_money)
    # in ra man hinh
    i_text = ""
    i_number = ""
    for what in add.income[i_choice]:
        i_text = i_text + what +"""
"""
        i_number = i_number + str(add.income[i_choice][what]) + """
"""
    lab_what_view.config(text=i_text)
    lab_what_view.pack(side="left")
    lab_money_view.config(text=i_number)
    lab_money_view.pack(side="right")
    # balance
    lab_balance_view.config(text=f"Balance = {add.balance()}")
    cannot_enter()
    # reset lai sau khi da nhap xong
    b_enter_add.config(text="Add more",command=reset)
    
def e_view():
    # gan gia tri
    e_choice = combo_type_add.get().lower()
    e_detail = en_detail.get().lower()
    e_money = int(en_money.get())
    # them vao dsach
    add.count(type, e_choice, e_detail, e_money)
    # view
    e_text = ""
    e_number = ""
    for what in add.expense[e_choice]:
        e_text = e_text + what +"""
"""
        e_number = e_number + str(add.expense[e_choice][what]) + """
"""
    lab_what_view.config(text=e_text)
    lab_what_view.pack(side="left")
    lab_money_view.config(text=e_number)
    lab_money_view.pack(side="right")
    # balance
    lab_balance_view.config(text=f"Balance = {add.balance()}")
    cannot_enter()
    # reset lai sau khi da nhap xong
    b_enter_add.config(text="Add more",command=reset)

def show_add():
    global type
    if var.get() == 1: # CHON INCOME
        # combobox
        combo_type_add["value"]=list_of_type.list_of_income
        combo_type_add.config(state="readonly")
        b_enter_add.config(command=i_view)
        type = "income"
    else: # CHON EXPENSE
        # combo box
        combo_type_add["value"]=list_of_type.list_of_expense
        combo_type_add.config(state="readonly")
        b_enter_add.config(command=e_view)
        type = "expense"
    b_enter_add.config(state="normal")
    b_enter_add.grid(row=18, column=0, columnspan=10)

def add_back():
    win_add.withdraw()


# TAO GIAO DIEN
lab_header = tk.Label(win_add,text="ADD NEW CASH", font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill=BOTH)

lab_intro_add = tk.Label(win_add, text="Manage your wallet with Wisexpend", pady=10, font="Sans 10 bold italic")
lab_intro_add.pack()

fr_add = tk.Frame(win_add, height=5, pady=80)
fr_add.pack()

fr_select = tk.Frame(fr_add, pady=20, padx=20, relief="ridge", bd=3)
fr_select.grid(row=0, column=0, columnspan=10)

b_enter_add = ttk.Button(fr_select, text="Add", state="disable")

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

lab_what_view = tk.Label(fr_what_view)
lab_money_view = tk.Label(fr_money_view)

lab_balance_view = tk.Label(fr_view, text="0", font="Roboto 10 bold")
lab_balance_view.grid(row=20, column=0, columnspan=10)

b_back = ttk.Button(win_add, text="Back", command=add_back)
b_back.pack()

lab_footer = tk.Label(win_add, text="", background="#ffdb58",height=2)
lab_footer.pack(fill=BOTH, side=BOTTOM)
