"""
@file : calc_gui.py
@brief : This file contains the GUI for the calculator
@details : The GUI is built using tkinter and includes buttons for all the operations
@author : Jakub Miženko
@date : PLACEHOLDER
@todo : Change root symbol so LaTeX can be used
"""

import tkinter as tk
from calc import insert_value, clear_entry, delete_last, calculate

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")


color1='#020f12'
color2='#05d7ff'
color3='#041c21'
color4="white"
color5='#03161a'
color_eq='#0ca2c2'
color_eq_in='#0a8fab'

root.configure(bg=color1)
root.resizable(False, False)



text_entry = tk.Text(root, height=3, fg="white",background=color1, width=20,font=("Verdana", 24),state="disabled")
text_entry.grid(columnspan=8)





def on_enter(e):
    e.widget['background'] = color5
    
def on_leave(e):
    e.widget['background'] = color3

def on_enter_spec(e):
    e.widget['background'] = color3

def on_leave_spec(e):
    e.widget['background'] = color5

def on_enter_eq(e):
    e.widget['background'] = color_eq_in

def on_leave_eq(e):
    e.widget['background'] = color_eq


def help_popup():
    """
    @brief : function to create a help popup window
    @details : The function creates a new window with a help message and an OK button to close the window.
    @param : None
    @return : None
    """
    
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_window.geometry("500x560")
    help_window.configure(bg=color1)
    help_popup_ok = tk.Button(help_window, text="OK", command=help_window.destroy, background=color3, foreground=color4, state="disabled", font=("Verdana", 12))
    help_popup_ok.pack(pady=20)
    help_label = tk.Label(help_window, text="Help", font=("Verdana", 20), background=color1, foreground=color4)
    help_label.pack(pady=20)
    help_text = tk.Text(help_window, height=45, fg="white", background=color1, width=50, font=("Verdana", 12))
    help_text.insert(tk.END, "This is a simple calculator.\n\n"
                             "Use the buttons to perform calculations.\n\n"
                             "For example:\n"
                             "1. Enter a number\n"
                             "2. Select an operation (+, -, *, /)\n"
                             "3. Enter another number\n"
                             "4. Press '=' to get the result\n\n"
                             "You can also use:\n"
                             "  - x^n for exponentiation\n"
                             "  - n√x for n-th square root of x\n"
                             "  - |x| for absolute value\n"
                             "  - n! for factorial\n"
                             "  - π for pi.\n"
                             "  - e for Euler's number.\n\n"
                             "Press 'C' to clear the entry.\n"
                             "Press 'DEL' to delete the last character.\n\n")

    help_text.pack(pady=20)
    help_window.resizable(False, False)


def about_popup():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("700x400")
    about_window.configure(bg=color1)
    about_popup_ok = tk.Button(about_window, text="OK", command=about_window.destroy, background=color3, foreground=color4, font=("Verdana", 12),state="disabled")
    about_popup_ok.pack(pady=20)
    about_label = tk.Label(about_window, text="About", font=("Verdana", 20), background=color1, foreground=color4)
    about_label.pack(pady=20)
    about_text = tk.Text(about_window, height=45, fg="white", background=color1, width=70, font=("Verdana", 12))
    about_text.insert(tk.END, "This is a simple calculator application.\n\n"
                             "It is designed to perform basic arithmetic operations.\n\n"
                             "Developed by [Alex Gajdoš, Jakub Miženko, Simon Zán, Marc Baffaluy Gesti]\n"
                             "Version 1.0\n\n"
                             "Thank you for using this calculator!")

    about_text.pack(pady=20)
    about_window.resizable(False, False)



def handle_keypress(event):
    
    key = event.char
    if key in "0123456789+-*/().,":
        insert_value(text_entry, key)
    elif key == "^":  
        insert_value(text_entry, "power(")
    elif key == "r":  
        insert_value(text_entry, "sqrt(")
    elif key == "!": 
        insert_value(text_entry, "factorial(")
    elif key == "\r":
        calculate(text_entry)
    elif key == "\b": 
        delete_last(text_entry)
    elif key == "c" or key == "C": 
        clear_entry(text_entry)


root.bind("<Key>", handle_keypress)


BTN_EXP = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="x^n", 
                width=7,
                height=2,
                font=("Verdana", 15),
                borderwidth=0,
                command=lambda: insert_value(text_entry, "power("))
BTN_EXP.grid(row=2, column=2, pady=2)


BTN_SQRT = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="n√x", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "sqrt("))
BTN_SQRT.grid(row=2, column=1,  pady=2)

BTN_BRC_R = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text=")", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, ")"))
BTN_BRC_R.grid(row=3, column=1, pady=2)

BTN_SEP = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text=",", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, ","))
BTN_SEP.grid(row=3, column=2, pady=2)

BTN_ABS = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="|x|", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "abs("))
BTN_ABS.grid(row=3, column=3, pady=2)

BTN_DEL = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="DEL", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: delete_last(text_entry))
BTN_DEL.grid(row=2, column=3, pady=2)


BTN_CLR = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="C", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: clear_entry(text_entry))
BTN_CLR.grid(row=2, column=4, pady=2)

BTN1 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="7", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 7))
BTN1.grid(row=4, column=1, pady=2)

BTN2 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="8", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 8))
BTN2.grid(row=4, column=2, pady=2)

BTN3 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="9", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 9))
BTN3.grid(row=4, column=3, pady=2)

BTN4 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="4", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 4))
BTN4.grid(row=5, column=1, pady=2)

BTN5 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="5", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 5))
BTN5.grid(row=5, column=2, pady=2)

BTN6 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="6", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 6))
BTN6.grid(row=5, column=3)

BTN7 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="1", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 1))
BTN7.grid(row=6, column=1, pady=2)

BTN8 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="2", 
                width=7,
                height=2,
                borderwidth=0,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 2))
BTN8.grid(row=6, column=2, pady=2)

BTN9 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="3", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 3))
BTN9.grid(row=6, column=3, pady=2)

BTN0 = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="0", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, 0))
BTN0.grid(row=7, column=2, pady=2)

BTN_PLUS = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="+", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "+"))
BTN_PLUS.grid(row=4, column=4, pady=2)

BTN_SUB = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="-", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "-"))
BTN_SUB.grid(row=5, column=4, pady=2)

BTN_DIV = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="/", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "/"))
BTN_DIV.grid(row=6, column=4, pady=2)

BTN_MUL = tk.Button(root,
                background=color5,
                foreground=color4,
                activebackground=color5,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="*", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "*"))
BTN_MUL.grid(row=3, column=4, pady=2)

BTN_DOT = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text=".", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "."))
BTN_DOT.grid(row=7, column=3, pady=2)

BTN_FAC = tk.Button(root,
                 background=color3,
                foreground=color4,
                activebackground=color1,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="n!", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: insert_value(text_entry, "fac("))
BTN_FAC.grid(row=7, column=1, pady=2)

BTN_EQ = tk.Button(root,
                 background=color_eq,
                foreground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="=", 
                width=7,
                borderwidth=0,
                height=2,
                font=("Verdana", 15),
                command=lambda: calculate(text_entry))
BTN_EQ.grid(row=7, column=4, pady=2)

BTN_HELP = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color3,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="Help", 
                width=6,
                height=1,
                font=("Verdana", 15),
                command=help_popup)
BTN_HELP.grid(row=8, column=4, pady=2)



BTN_ABOUT = tk.Button(root,
                background=color3,
                foreground=color4,
                activebackground=color3,
                activeforeground=color4,
                highlightthickness=2,
                highlightcolor='white',
                text="About", 
                width=6,
                height=1,
                font=("Verdana", 15),
                command=about_popup)
BTN_ABOUT.grid(row=8, column=1, pady=2)


BTN0.bind("<Enter>", on_enter)
BTN0.bind("<Leave>", on_leave)
BTN1.bind("<Enter>", on_enter)
BTN1.bind("<Leave>", on_leave)
BTN2.bind("<Enter>", on_enter)
BTN2.bind("<Leave>", on_leave)
BTN3.bind("<Enter>", on_enter)
BTN3.bind("<Leave>", on_leave)
BTN4.bind("<Enter>", on_enter)
BTN4.bind("<Leave>", on_leave)
BTN5.bind("<Enter>", on_enter)
BTN5.bind("<Leave>", on_leave)
BTN6.bind("<Enter>", on_enter)
BTN6.bind("<Leave>", on_leave)
BTN7.bind("<Enter>", on_enter)
BTN7.bind("<Leave>", on_leave)
BTN8.bind("<Enter>", on_enter)
BTN8.bind("<Leave>", on_leave)
BTN9.bind("<Enter>", on_enter)
BTN9.bind("<Leave>", on_leave)
BTN_PLUS.bind("<Enter>", on_enter_spec)
BTN_PLUS.bind("<Leave>", on_leave_spec)
BTN_SUB.bind("<Enter>", on_enter_spec)
BTN_SUB.bind("<Leave>", on_leave_spec)
BTN_MUL.bind("<Enter>", on_enter_spec)
BTN_MUL.bind("<Leave>", on_leave_spec)
BTN_DIV.bind("<Enter>", on_enter_spec)
BTN_DIV.bind("<Leave>", on_leave_spec)
BTN_DOT.bind("<Enter>", on_enter)
BTN_DOT.bind("<Leave>", on_leave)
BTN_FAC.bind("<Enter>", on_enter)
BTN_FAC.bind("<Leave>", on_leave)
BTN_EQ.bind("<Enter>", on_enter_eq)
BTN_EQ.bind("<Leave>", on_leave_eq)
BTN_EXP.bind("<Enter>", on_enter_spec)
BTN_EXP.bind("<Leave>", on_leave_spec)
BTN_SQRT.bind("<Enter>", on_enter_spec)
BTN_SQRT.bind("<Leave>", on_leave_spec)
BTN_BRC_R.bind("<Enter>", on_enter_spec)
BTN_BRC_R.bind("<Leave>", on_leave_spec)
BTN_SEP.bind("<Enter>", on_enter_spec)
BTN_SEP.bind("<Leave>", on_leave_spec)
BTN_ABS.bind("<Enter>", on_enter_spec)
BTN_ABS.bind("<Leave>", on_leave_spec)
BTN_DEL.bind("<Enter>", on_enter_spec)
BTN_DEL.bind("<Leave>", on_leave_spec)
BTN_CLR.bind("<Enter>", on_enter_spec)
BTN_CLR.bind("<Leave>", on_leave_spec)




root.mainloop()







