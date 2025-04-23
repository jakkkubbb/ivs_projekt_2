"""
@file calc.py
@brief This file contains the main logic for the calculator GUI
@details The calculator supports basic operations, has a "help" button
with a pop-up window, and input can be given with buttons or keyboard.
@author Jakub Miženko
@date 2025-04-18
"""

import tkinter as tk
from math_lib import sum, sub, mul, div, power, abs_v, root, factorial


def insert_value(entry_widget, value):
    """
    @brief inserts a value into the entry widget
    @details the value is appended to the current value in the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the entry widget to insert the value into
    @param value the value to insert
    @return None
    """
    entry_widget.config(state="normal")
    current = entry_widget.get("1.0", "end").strip()
    entry_widget.delete("1.0", "end")
    entry_widget.insert("1.0", current + str(value))
    entry_widget.config(state="disabled")

def clear_entry(entry_widget):
    """
    @brief clears the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the widget to clear
    @return None
    """
    entry_widget.config(state="normal")
    entry_widget.delete("1.0", "end")
    entry_widget.config(state="disabled")


def delete_last(entry_widget):
    """
    @brief deletes the last character of the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the widget to delete the last character from
    @return None
    """
    entry_widget.config(state="normal")
    current = entry_widget.get("1.0", "end").strip()
    entry_widget.delete("1.0", "end")
    entry_widget.insert("1.0", current[:-1])
    entry_widget.config(state="disabled")


def calculate(entry_widget):
    """
    @brief calculates the result of the expression in the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the widget to calculate the result from
    @return None
    """
    entry_widget.config(state="normal")
    try:
        expression = entry_widget.get("1.0", "end").strip()

        
        expression = expression.replace("power", "power")  
        expression = expression.replace("sqrt", "root")  
        expression = expression.replace("abs", "abs_v")  
        expression = expression.replace("fac", "factorial")
        
        result = eval(expression, {"__builtins__": None}, {
            "sum": sum,
            "sub": sub,
            "mul": mul,
            "div": div,
            "power": power,
            "abs_v": abs_v,
            "root": root,
            "factorial": factorial
        })

        
        entry_widget.delete("1.0", "end")
        entry_widget.insert("1.0", str(result))
    except Exception as e:
        entry_widget.delete("1.0", "end")
        entry_widget.insert("1.0", "Error")
    entry_widget.config(state="disabled")