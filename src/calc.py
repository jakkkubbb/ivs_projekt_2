import tkinter as tk
from math_lib import sum, sub, mul, div, power, abs_v, root, factorial


def insert_value(entry_widget, value):
    entry_widget.config(state="normal")
    current = entry_widget.get("1.0", "end").strip()
    entry_widget.delete("1.0", "end")
    entry_widget.insert("1.0", current + str(value))
    entry_widget.config(state="disabled")

def clear_entry(entry_widget):
    entry_widget.config(state="normal")
    entry_widget.delete("1.0", "end")
    entry_widget.config(state="disabled")


def delete_last(entry_widget):
    entry_widget.config(state="normal")
    current = entry_widget.get("1.0", "end").strip()
    entry_widget.delete("1.0", "end")
    entry_widget.insert("1.0", current[:-1])
    entry_widget.config(state="disabled")


def calculate(entry_widget):
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