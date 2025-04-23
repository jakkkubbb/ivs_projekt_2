import tkinter as tk
from math_lib import sum, sub, mul, div, power, abs_v, root, factorial


ans = None
calculated = False

def insert_value(entry_widget, value):
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
    entry_widget.config(state="normal")
    entry_widget.delete("1.0", "end")
    entry_widget.config(state="disabled")


def delete_last(entry_widget):
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
    global ans
    if ans is None:
        return "0"
    return ans
    

def calculate(entry_widget):
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


 