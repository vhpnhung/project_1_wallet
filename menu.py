import tkinter as tk
from tkinter import BOTH, BOTTOM, TOP, ttk
from datetime import date


win_menu = tk.Tk()
win_menu.title("Wisexpend")
win_menu.geometry("500x500+400+80")


username = "nhung"
now = date.today().strftime("%B %d, %Y")
photo_add = tk.PhotoImage(file = r"E:\Nhung\Data Analyst\Python\Codegym\Case\image\m_wallet.png")
photo_snl = tk.PhotoImage(file = r"E:\Nhung\Data Analyst\Python\Codegym\Case\image\m_snl.png")
photo_report = tk.PhotoImage(file = r"E:\Nhung\Data Analyst\Python\Codegym\Case\image\m_report.png")

def again_add():
    from f_add import win_add
    win_add.deiconify()
def again_report():
    from f_report import win_rud
    win_rud.deiconify()
def again_snl():
    from f_snl import win_snl
    win_snl.deiconify()


def menu_add():
    import f_add
    b_add_menu.config(command=again_add)
def menu_report():
    import f_report
    b_report_menu.config(command=again_report)
def menu_snl():
    import f_snl
    b_snl_menu.config(command=again_snl)

def menu_quit():
    win_menu.destroy()
    import signin

lab_header = tk.Label(text=now, font="Arial 10 bold", fg="white", background="#ffdb58",height=2)
lab_header.pack(fill=BOTH)

lab_title_menu = tk.Label(text=f"Welcome back, {username}!", font="bold")
lab_title_menu.pack(fill=BOTH)

fr_menu = tk.Frame(height=5, pady=150)
fr_menu.pack()

b_add_menu = ttk.Button(fr_menu, text="   New transaction   ", image=photo_add, compound=TOP, command=menu_add)
b_add_menu.grid(row=0, column=0)

b_report_menu = ttk.Button(fr_menu, text="   Wallet Manager   ", image=photo_report, compound=TOP, command=menu_report)
b_report_menu.grid(row=0, column=1)

b_snl_menu = ttk.Button(fr_menu, text="   Savings Calculation   ", image=photo_snl, compound=TOP, command=menu_snl)
b_snl_menu.grid(row=0, column=3)

b_signout = ttk.Button(text="Sign out", command=menu_quit)
b_signout.pack()

lab_footer = tk.Label(text="", background="#ffdb58",height=2)
lab_footer.pack(fill=BOTH, side=BOTTOM)


win_menu.mainloop()