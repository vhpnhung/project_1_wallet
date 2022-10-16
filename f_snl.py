import tkinter as tk
from tkinter import ttk

win_snl = tk.Tk()
win_snl.title("Wisexpend - Savings Calculator")
win_snl.geometry("500x500+400+80")

var = tk.IntVar()
var_type = tk.IntVar()
var_time = tk.StringVar()

def time():
    if var.get() == 1:
        print("week")
    if var.get() == 2:
        print("month")
    if var.get() == 3:
        print("year")

def init_basics_s():
    lab_pv_savings = tk.Label(fr_savings, text="Now I have (VND)   ", font="Roboto 8 bold", pady=5)
    lab_pv_savings.grid(row=2, column=0, columnspan=3, sticky="w")

    en_pv_savings = ttk.Entry(fr_savings)
    en_pv_savings.grid(row=2, column=4, columnspan=8)

    lab_i_savings = tk.Label(fr_savings, text="Annual interest rate (%)   ", font="Roboto 8 bold", pady=5)
    lab_i_savings.grid(row=3, column=0, columnspan=3, sticky="w")

    en_i_savings = ttk.Entry(fr_savings)
    en_i_savings.grid(row=3, column=4, columnspan=8)

    lab_maturity_savings = tk.Label(fr_savings, text="Maturity   ", font="Roboto 8 bold", pady=5)
    lab_maturity_savings.grid(row=4, column=0, columnspan=1, sticky="w")

    en_maturity_savings = tk.Entry(fr_savings)
    en_maturity_savings.grid(row=4, column=1, columnspan=4, sticky="w")

    lab_year = tk.Label(fr_savings, text="year(s)", bg="#f0f0f0",pady=10, padx=20)
    lab_year.grid(row=4, column=6, columnspan=8, sticky="w")

def init_times(): #BO DI!
    global sel_maturity
    sel_maturity = tk.Radiobutton(fr_savings, text="week(s)", variable=var, value=1, command=time)
    sel_maturity.grid(row=5, column=6, columnspan=5, sticky="w")

    sel_maturity = tk.Radiobutton(fr_savings, text="month(s)", variable=var, value=2, command=time)
    sel_maturity.grid(row=6, column=6, columnspan=5, sticky="w")

    sel_maturity = tk.Radiobutton(fr_savings, text="year(s)", variable=var, value=3, command=time,bg="white")
    sel_maturity.grid(row=7, column=6, columnspan=5, sticky="w")

def choice(selection):
    a = selection

def init_time():
    var_time.set("time")
    drop= tk.OptionMenu(fr_savings, var_time, "week", "month", "year", command=choice)
    drop.grid(row=4, column=6, columnspan=5, sticky="w")

def init_fv():
    lab_fv_savings = tk.Label(fr_savings, text="In the future, I will receive (VND)  ", font="Roboto 8 bold", pady=5)
    lab_fv_savings.grid(row=6, column=0, columnspan=3, sticky="w")

    en_fv_savings = ttk.Entry(fr_savings)
    en_fv_savings.grid(row=6, column=4, columnspan=8)

def type_s():
    if var_type.get() == 1:
        init_basics_s()
        init_fv()
    else:
        init_basics_s()
        init_time()
        init_fv()
    
def snl_back():
    win_snl.destroy()
    from menu import win_menu
    win_menu.mainloop()

lab_header = tk.Label(text="SAVINGS AND LOANS CALCULATOR", font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill="both")

lab_intro_add = tk.Label(pady=10, font="Sans 10 bold italic", 
text="""Is your savings and loans' plan okay? 
Let Wisexpend help you!""")
lab_intro_add.pack()

fr_savings = tk.Frame(padx=20, pady=100)
fr_savings.pack()

lab_title_savings = tk.Label(fr_savings, text="Choose your type of savings", font="Roboto 9 italic")
lab_title_savings.grid(row=0, column=0, columnspan=10)

sel_type_savings = tk.Radiobutton(fr_savings, text="Lump-sum", variable=var_type, value=1, command=type_s)
sel_type_savings.grid(row=1, column=0, columnspan=5)

sel_type_savings = tk.Radiobutton(fr_savings, text="Periodic", variable=var_type, value=2, command=type_s)
sel_type_savings.grid(row=1, column=5, columnspan=5)

b_back = ttk.Button(text="Back", command=snl_back)
b_back.pack()

lab_footer = tk.Label(text="", background="#ffdb58",height=2)
lab_footer.pack(fill="both", side="bottom")

win_snl.mainloop()