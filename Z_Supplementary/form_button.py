from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x200")

# Main frame
frm = ttk.Frame(root, padding=10)
frm.grid(sticky="nsew")

# Allow resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Configure frm's grid columns
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.rowconfigure(9, weight=1)   # Add vertical stretch to row 9

# Content
ttk.Label(frm, text="Hello World!").grid(column=0, row=0, columnspan=2, sticky="w")

# Submit button INSIDE frm, bottom-right 
submit_btn = ttk.Button(frm, text="Submit")
submit_btn.grid(row=10, column=1, sticky="e", pady=(0,10), padx=(0, 10))

root.mainloop()
