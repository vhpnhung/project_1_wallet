import tkinter as tk
from tkinter import ttk
from snl import formula

win_snl = tk.Toplevel() #############################
win_snl.title("Wisexpend - Savings Calculator")
win_snl.geometry("500x500+400+80")

var_type = tk.IntVar() # lump-sum, periodical
var_value = tk.IntVar() # pv,fv

def init_pv():
    lab_fv.grid(row=5, column=0, columnspan=5, sticky="w")
    en_fv.grid(row=5, column=5, columnspan=3, sticky="w")

    lab_time.grid(row=6, column=0, columnspan=5, sticky="w")
    en_time.grid(row=6, column=5, columnspan=3, sticky="w")    

    lab_i.grid(row=7, column=0, columnspan=5, sticky="w")
    en_i.grid(row=7, column=5, columnspan=3, sticky="w")

def init_fv():
    lab_pv.grid(row=5, column=0, columnspan=5, sticky="w")
    en_pv.grid(row=5, column=5, columnspan=3, sticky="w")

    lab_time.grid(row=6, column=0, columnspan=5, sticky="w")
    en_time.grid(row=6, column=5, columnspan=3, sticky="w")    

    lab_i.grid(row=7, column=0, columnspan=5, sticky="w")
    en_i.grid(row=7, column=5, columnspan=3, sticky="w")    

def collapse():
    lab_fv.destroy()
    en_fv.destroy()
    lab_time.destroy()
    en_time.destroy()
    lab_i.destroy()
    en_i.destroy()
    lab_pv.destroy()
    en_pv.destroy()
    lab_result.config(text="")

def new():
    global lab_fv
    global en_fv
    global lab_time
    global en_time
    global lab_i
    global en_i
    global lab_pv
    global en_pv
    lab_fv = tk.Label(fr_savings, text="I want to have (VND)")
    en_fv = tk.Entry(fr_savings)
    lab_time = tk.Label(fr_savings, text="after (years)")
    en_time = tk.Entry(fr_savings)
    lab_i = tk.Label(fr_savings, text="with the nterest rate of (%)")
    en_i = tk.Entry(fr_savings)
    lab_pv = tk.Label(fr_savings, text="Now I have (VND)")
    en_pv = tk.Entry(fr_savings)

def reset():
    collapse()
    new()
    b_start.config(text="Confirm", command=init_format)

def init_format():
    if var_value.get() == 1: # PV
        init_pv()
    else: # FV
        init_fv()
    b_start.config(text="Show result", command=snl)

def snl():
    global lab_result
    i = float(en_i.get())/100
    t = int(en_time.get())
    if var_type.get() == 1: # LUMP-SUM
        choice = "lump-sum"
        if var_value.get() == 1: # pv
            fv = int(en_fv.get())
            pv = formula.pv(choice, fv, i, t) 
            lab_result.config(text=f"Today I need to put {pv} in savings", font="Roboto 11 italic bold", pady=5)
        else: #fv
            pv = int(en_pv.get())
            fv = formula.fv(choice, pv, i, t)
            lab_result.config(text=f"I will have {fv} in {t} years", font="Roboto 11 italic bold", pady=5) 
            #########
    else: # PERIODIC
        choice = "periodic"
        if var_value.get() == 1: # annuity
            fv = int(en_fv.get())
            pv = formula.pv(choice, fv, i, t)
            lab_result.config(text=f"Each year I need to put {pv} in savings", font="Roboto 11 italic bold", pady=5)
        else: # future value
            pv = int(en_pv.get())
            fv = formula.fv(choice, pv, i, t)
            lab_result.config(text=f"I will have {fv} in {t} years", font="Roboto 11 italic bold", pady=5)
    lab_result.grid(row=10, column=0, columnspan=10)
           

def snl_back():
    win_snl.withdraw()

lab_header = tk.Label(win_snl, text="SAVINGS AND LOANS CALCULATOR", font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill="both")

lab_intro_add = tk.Label(win_snl, pady=10, font="Sans 10 bold italic", 
text="""Is your savings plan okay? 
Let Wisexpend help you!""")
lab_intro_add.pack()

fr_savings = tk.Frame(win_snl, padx=20, pady=40)
fr_savings.pack()

# GIAO DIEN CHON VALUE
lab_title_type = tk.Label(fr_savings, text="What do you want to know?", font="Roboto 9 italic bold")
lab_title_type.grid(row=0, column=0, columnspan=8)

sel_pv = tk.Radiobutton(fr_savings, text="Present value", variable=var_value, value=1, pady=5, command=reset)
sel_pv.grid(row=1, column=0, columnspan=4)

sel_fv = tk.Radiobutton(fr_savings, text="Future value", variable=var_value, value=2, pady=5, command=reset)
sel_fv.grid(row=1, column=4, columnspan=4)

# GIAO DIEN CHON TYPE
lab_title_savings = tk.Label(fr_savings, text="Choose your type of savings", font="Roboto 9 italic bold")
lab_title_savings.grid(row=2, column=0, columnspan=8)

sel_type_savings = tk.Radiobutton(fr_savings, text="Lump-sum", variable=var_type, value=1, pady=5, command=reset)
sel_type_savings.grid(row=3, column=0, columnspan=4)

sel_type_savings = tk.Radiobutton(fr_savings, text="Periodic", variable=var_type, value=2, pady=5, command=reset)
sel_type_savings.grid(row=3, column=4, columnspan=4)

# NUT ENTER
b_start = ttk.Button(fr_savings, text="Confirm", command=init_format)
b_start.grid(row=40, column=0, columnspan=16)

b_back = ttk.Button(win_snl, text="Back", command=snl_back)
b_back.pack()

# GIAO DIEN ENTRY
new()

lab_result = tk.Label(fr_savings)

lab_footer = tk.Label(win_snl, text="", background="#ffdb58",height=2)
lab_footer.pack(fill="both", side="bottom")