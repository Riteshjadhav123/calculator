import tkinter as tk

# --- Functions ---
def click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: ÷0")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid")

def key_input(event):
    key = event.char
    if key in '0123456789+-*/.':
        click(key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace
        backspace()

# --- GUI Setup ---
window = tk.Tk()
window.title("Unique Calculator")
window.geometry("320x500")
window.configure(bg='#1e1e1e')
window.bind("<Key>", key_input)

# --- Entry Field ---
entry = tk.Entry(window, font=('Consolas', 24), bg="#2d2d2d", fg="#00ffcc", bd=0, justify="right", insertbackground="white")
entry.pack(pady=20, ipadx=8, ipady=15, padx=15, fill='x')

# --- Button Setup ---
buttons = [
    ['C', '←', '(', ')'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# --- Button Frame ---
btn_frame = tk.Frame(window, bg='#1e1e1e')
btn_frame.pack(expand=True, fill='both')

def build_button(text, row, col):
    def on_click():
        if text == 'C':
            clear()
        elif text == '=':
            calculate()
        elif text == '←':
            backspace()
        else:
            click(text)
    
    btn = tk.Button(btn_frame, text=text, font=('Segoe UI', 16, 'bold'),
                    fg='white', bg='#333333', activebackground='#444444',
                    activeforeground='#00ffcc', bd=0, command=on_click)
    btn.grid(row=row, column=col, sticky='nsew', padx=3, pady=3, ipadx=10, ipady=15)

# Create buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        build_button(char, r, c)

# Grid resizing
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
    btn_frame.columnconfigure(i, weight=1)

# --- Run the App ---
window.mainloop()
