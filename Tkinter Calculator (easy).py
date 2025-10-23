import tkinter as tk
import math

root = tk.Tk()
root.title("A3tria Calculator")
root.geometry("500x500")
root.resizable(False, False)

light_theme = {
    "bg": "#f5f5f5",
    "fg": "#000000",
    "button_bg": "#ffffff",
    "button_fg": "#000000",
    "special_bg": "#4CAF50",
    "special_fg": "#ffffff",
}

dark_theme = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "button_bg": "#2c2c2c",
    "button_fg": "#ffffff",
    "special_bg": "#00C853",
    "special_fg": "#ffffff",
}

theme = light_theme

def apply_theme():
    root.configure(bg=theme["bg"])
    entry.configure(bg=theme["button_bg"], fg=theme["fg"], insertbackground=theme["fg"])
    for b in buttons:
        b.configure(bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["special_bg"])
    clear_button.configure(bg=theme["special_bg"], fg=theme["special_fg"])
    equal_button.configure(bg=theme["special_bg"], fg=theme["special_fg"])
    theme_button.configure(bg=theme["special_bg"], fg=theme["special_fg"])

def button_click(value):
    entry.insert(tk.END, value)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get().replace("^", "**")
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def scientific_function(func):
    try:
        val = float(entry.get())
        if func == "sin":
            result = math.sin(math.radians(val))
        elif func == "cos":
            result = math.cos(math.radians(val))
        elif func == "tan":
            result = math.tan(math.radians(val))
        elif func == "sqrt":
            result = math.sqrt(val)
        elif func == "square":
            result = val ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(round(result, 8)))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def toggle_theme():
    global theme
    theme = dark_theme if theme == light_theme else light_theme
    apply_theme()

entry = tk.Entry(root, width=12, font=("Segoe UI", 20), borderwidth=0, relief="flat", justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=15, padx=20, ipady=8, sticky="ew")

buttons = []
layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sin", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("cos", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("tan", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("^", 4, 2), ("+", 4, 3), ("√", 4, 4),
    ("x²", 5, 0)
]

for (text, row, col) in layout:
    if text in ["sin", "cos", "tan"]:
        cmd = lambda f=text: scientific_function(f)
    elif text == "√":
        cmd = lambda: scientific_function("sqrt")
    elif text == "x²":
        cmd = lambda: scientific_function("square")
    else:
        cmd = lambda t=text: button_click(t)
    b = tk.Button(root, text=text, width=5, height=2, font=("Segoe UI", 13), borderwidth=0, command=cmd)
    b.grid(row=row, column=col, padx=4, pady=4)
    buttons.append(b)

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Segoe UI", 13), borderwidth=0, command=button_clear)
clear_button.grid(row=5, column=1, padx=4, pady=4)

equal_button = tk.Button(root, text="=", width=5, height=2, font=("Segoe UI", 13), borderwidth=0, command=button_equal)
equal_button.grid(row=5, column=2, padx=4, pady=4)

theme_button = tk.Button(root, text="🌗", width=5, height=2, font=("Segoe UI", 13), borderwidth=0, command=toggle_theme)
theme_button.grid(row=5, column=3, padx=4, pady=4)

# filler for symmetry (blank cell)
tk.Label(root, text="", bg=theme["bg"]).grid(row=5, column=4)

apply_theme()
root.mainloop()
