import tkinter as tk
from tkinter import ttk

def update_dropdown_text():
    selected_items = [item for item, var in checkboxes.items() if var.get()]
    dropdown_var.set(', '.join(selected_items))

root = tk.Tk()
root.title('Dropdown with Checkboxes')

checkboxes = {}
dropdown_var = tk.StringVar()

dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=(), state='readonly')
dropdown.pack()

checkbox_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

def show_checkboxes():
    menu = tk.Menu(root, tearoff=0)
    for item in checkbox_items:
        checkboxes[item] = tk.BooleanVar()
        menu.add_checkbutton(label=item, variable=checkboxes[item], command=update_dropdown_text)
    menu.tk_popup(dropdown.winfo_rootx(), dropdown.winfo_rooty() + dropdown.winfo_height())
    # set the values of the dropdown based on the selected items
    selected_items = [item for item, var in checkboxes.items() if var.get()]
    dropdown_var.set(', '.join(selected_items))

dropdown.configure(values=checkbox_items)
dropdown.bind('<Button-1>', lambda e: show_checkboxes())

root.mainloop()
