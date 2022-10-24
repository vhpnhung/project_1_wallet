import re
import tkinter as tk
from tkinter import ttk
from data_add import list_of_type,add

#reset
#view del + edit


win_rud = tk.Toplevel()
win_rud.title("Wisexpend - Add")
win_rud.geometry("600x500+400+80") #rud = read, update, delete

var = tk.IntVar()
var_choice = tk.IntVar()
type_add = tk.StringVar()
item_add = tk.StringVar()


def i_view():
    # gan gia tri
    i_choice = combo_type_rud.get().lower()
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

def e_view():
    global e_choice
    # gan gia tri
    e_choice = combo_type_rud.get().lower()
    # in ra man hinh
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


def view_rud():
    global type
    if var.get() == 1: # CHON INCOME
        # combobox
        combo_type_rud["value"]=list_of_type.list_of_income
        combo_type_rud.config(state="readonly")
        b_enter_rud.config(command=i_view)
        type = "income"
    else: # CHON EXPENSE
        # combo box
        combo_type_rud["value"]=list_of_type.list_of_expense
        combo_type_rud.config(state="readonly")
        b_enter_rud.config(command=e_view)
        type = "expense"
    b_enter_rud.grid(row=18, column=0, columnspan=10)
    b_enter_rud.config(state="normal")

def check_item():
    global category_choice
    category_choice = combo_type_rud.get().lower()
    en_money_edit.config(state="normal")
    en_item_edit.config(state="normal")
    if var.get() == 1: # CHON INCOME
        combo_item["value"]=add.income[category_choice]
    else:
        combo_item["value"]=add.expense[category_choice]
    combo_item.config(state="normal")
    if var_choice.get() == 2: # CHON EDIT
        b_enter_rud.config(state="normal", command=done_edit)
    elif var_choice.get() == 3: #  CHON REMOVE
        b_enter_rud.config(state="normal", command=done_remove)
        lab_item_edit.config(text="Remove item")
        en_money_edit.config(state="disable")

def select_item():
    selected_item = combo_item.get()
    removed_characters=[r"'", ":", " "]
    for i in range(0,10):
        selected_item = selected_item.replace(str(i),"")
    for k in removed_characters:
        selected_item = selected_item.replace(k, "")
    return selected_item

def done_edit():
    # ham sua ttin
    new = en_money_edit.get()
    selected_item = en_item_edit.get().lower()
    # ham chinh
    add.update(type, category_choice, selected_item, new)
    # show
    if var.get() == 1: # CHON INCOME
        i_view()
    else:
        e_view()

def done_remove():
    # khai bao
    selected_item = en_item_edit.get().lower()
    # ham
    add.remove(type,category_choice, selected_item)
    # show
    if var.get() == 1: # CHON INCOME
        i_view()
    else:
        e_view()

def edit_rud():
    global type
    if var.get() == 1: # CHON INCOME
        # combobox
        combo_type_rud["value"]=list_of_type.list_of_income
        combo_type_rud.config(state="readonly")
        type = "income"
    else: # CHON EXPENSE
        # combo box
        combo_type_rud["value"]=list_of_type.list_of_expense
        combo_type_rud.config(state="readonly") 
        type = "expense"
    b_enter_rud.config(state="normal")
    b_enter_rud.grid(row=18, column=0, columnspan=10)
    b_check_item.config(state="normal", command=check_item)

def reset():
    var.set(None)
    type_add.set(None)
    item_add.set(None)
    lab_money_view.config(text="")
    lab_what_view.config(text="")
    b_enter_rud.config(state="disable")
    combo_item.config(state="disable")
    b_check_item.config(state="disable")
    en_money_edit.delete(0, "end")
    en_money_edit.config(state="disable")
    en_item_edit.delete(0, "end")
    en_item_edit.config(state="disable")
    

def choice(): ### MENU CHINH
    reset()
    if var_choice.get() == 1: # CHON VIEW
        sel_earning_rud.config(command=view_rud)
        sel_expenditure_rud.config(command=view_rud)
    elif var_choice.get() == 2: # CHON EDIT
        lab_combo2.grid(row=5, column=1, columnspan=2, sticky="w")
        combo_item.grid(row=5,column=3,columnspan=3)
        lab_item_edit.grid(row=6, column=1, columnspan=3, sticky="w")
        en_item_edit.grid(row=6,column=4)
        lab_money_edit.grid(row=7, column=1, columnspan=3, sticky="w")
        en_money_edit.grid(row=7,column=4)
        b_check_item.grid(row=5, column=0)
        sel_earning_rud.config(command=edit_rud)
        sel_expenditure_rud.config(command=edit_rud)
    else: # CHON DELETE
        lab_combo2.grid(row=5, column=1, columnspan=2, sticky="w")
        combo_item.grid(row=5,column=3,columnspan=3)
        sel_earning_rud.config(command=edit_rud)
        sel_expenditure_rud.config(command=edit_rud)
        b_check_item.grid(row=5, column=0)
        lab_item_edit.grid(row=6, column=1, columnspan=3, sticky="w")
        en_item_edit.grid(row=6,column=4)
    sel_earning_rud.config(state="normal")
    sel_expenditure_rud.config(state="normal")
    

def rud_back():
    win_rud.withdraw()


# TAO GIAO DIEN
lab_header = tk.Label(win_rud, text="ADD NEW CASH", font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill="both")

lab_intro_add = tk.Label(win_rud, text="View your wallet", pady=10, font="Sans 10 bold italic")
lab_intro_add.pack()

fr_rud = tk.Frame(win_rud, height=5, pady=50)
fr_rud.pack()

fr_interact = tk.Frame(fr_rud, padx=20, pady=20)
fr_interact.grid(row=1, column=0, columnspan=6)

fr_visual = tk.Frame(fr_rud, padx=20, pady=20, relief="ridge", bd=2)
fr_visual.grid(row=1, column=7, columnspan=6, sticky="w")

lab_choice = tk.Label(fr_interact, text="Choose function: ")
lab_choice.grid(row=0, column=0)

sel_choice_read = tk.Radiobutton(fr_interact, text="View", variable=var_choice, value=1 ,command=choice)
sel_choice_read.grid(row=0, column=3)

sel_choice_update = tk.Radiobutton(fr_interact, text="Edit", variable=var_choice, value=2 ,command=choice)
sel_choice_update.grid(row=0, column=4)

sel_choice_delete = tk.Radiobutton(fr_interact, text="Remove", variable=var_choice, value=3 ,command=choice)
sel_choice_delete.grid(row=0, column=5)

sel_earning_rud = tk.Radiobutton(fr_interact, text="Earning", variable=var, value=1, state="disable")
sel_earning_rud.grid(row=1, column=0, sticky="w")

sel_expenditure_rud = tk.Radiobutton(fr_interact, text="Expenditure", variable=var, value=0, state="disable")
sel_expenditure_rud.grid(row=2, column=0, sticky="w")

lab_combo1 = tk.Label(fr_interact, text="Category", font="Roboto 8 bold")
lab_combo1.grid(row=4, column=1, columnspan=2, sticky="w")

combo_type_rud = ttk.Combobox(fr_interact, textvariable=type_add, state="disable")
combo_type_rud.grid(row=4,column=3,columnspan=3)

combo_item = ttk.Combobox(fr_interact, textvariable=item_add, state="disable")

b_enter_rud = ttk.Button(fr_interact, text="Execute", state="disable")
b_check_item = ttk.Button(fr_interact, text=">>>", state="disable")

# phan view
lab_what_view = tk.Label(fr_visual)
lab_money_view = tk.Label(fr_visual)



# phan edit
lab_combo2 = tk.Label(fr_interact, text="List of item(s)", font="Roboto 8 bold")

lab_item_edit = tk.Label(fr_interact, text="Change item", font="Roboto 8 bold")

lab_money_edit = tk.Label(fr_interact, text="Change amount to", font="Roboto 8 bold")

en_money_edit = tk.Entry(fr_interact, state="disable")
en_item_edit = tk.Entry(fr_interact, state="disable")


# phan delete



b_back = ttk.Button(win_rud, text="Back", command=rud_back)
b_back.pack()

lab_footer = tk.Label(win_rud, text="", background="#ffdb58",height=2)
lab_footer.pack(fill="both", side="bottom")