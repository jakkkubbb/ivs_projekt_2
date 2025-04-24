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

"""
@var ans
@brief variable to store the last calculated value
"""
ans = None
"""
@var calculated
@brief variable to store if the last calculation was successful
"""
calculated = False


def insert_value(entry_widget, value):
    """
    @brief inserts a value into the entry widget
    @details the value is appended to the current value in the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the entry widget to insert the value into
    @param value the value to insert
    @return the function does not return anything, it only modifies the entry widget
    """
    global ans,calculated

    entry_widget.config(state="normal")
    current = entry_widget.get("1.0", "end").strip()
    
    

    if calculated:
        if str(value).isdigit() or str(value)=="ans":
            current=""
        calculated = False

    if current == "0" or current == "Error":
        entry_widget.delete("1.0", "end")
        current = ""
    


    entry_widget.delete("1.0", "end")
    entry_widget.insert("1.0", current + str(value))
    entry_widget.config(state="disabled")

def clear_entry(entry_widget):
    """
    @brief clears the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the widget to clear
    @return the function does not return anything, it only modifies the entry widget
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
    @return the function does not return anything, it only modifies the entry widget
    """
    global ans,calculated
    calculated = False
    entry_widget.config(state="normal")
    
    current = entry_widget.get("1.0", "end").strip()

    
    if len(current) >= 3:
        if current[-3:] == "ans":
            current = current[:-2]
        elif current[-4:] == "abs(":
            current = current[:-3]
        elif current[-6:] == "power(":
            current = current[:-5]
        elif current[-5:] == "sqrt(":
            current = current[:-4]
        elif current[-4:] == "fac(":
            current = current[:-3]
        

    entry_widget.delete("1.0", "end")
    entry_widget.insert("1.0", current[:-1])
    entry_widget.config(state="disabled")


def get_ans(entry_widget):
    """
    @brief returns the last calculated value
    @details if there was not a calculation yet, it returns 0
    @param entry_widget the widget to get the last calculated value from
    @return the last calculated value
    """
    global ans
    if ans is None:
        return "0"
    return ans
    

def calculate(entry_widget):
    """
    @brief calculates the result of the expression in the entry widget
    @details the state of the entry widget is set to normal before inserting the value
    then it is set to disabled again
    @param entry_widget the widget to calculate the result from
    @return the function does not return anything, only inserts the result into the entry widget
    """
    global ans,calculated
    entry_widget.config(state="normal")
    try:
        expression = entry_widget.get("1.0", "end").strip()

        
        expression = expression.replace("power", "power")  
        expression = expression.replace("sqrt", "root")  
        expression = expression.replace("abs", "abs_v")  
        expression = expression.replace("fac", "factorial")
        expression = expression.replace("ans", str(get_ans(entry_widget)))
        
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
        
        ans = result
        calculated= True

        entry_widget.delete("1.0", "end")
        entry_widget.insert("1.0", str(result))
    except Exception as e:
        entry_widget.delete("1.0", "end")
        entry_widget.insert("1.0", "Error")
    entry_widget.config(state="disabled")


 