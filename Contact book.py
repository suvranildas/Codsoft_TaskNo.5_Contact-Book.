import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Contact Book")

# Contact storage
contacts = {}

# Functions to handle contact book operations
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone and email:
        contacts[name] = {"Phone": phone, "Email": email}
        messagebox.showinfo("Success", "Contact added!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name in contacts:
        if phone and email:
            contacts[name] = {"Phone": phone, "Email": email}
            messagebox.showinfo("Success", "Contact updated!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showwarning("Error", "Contact not found!")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted!")
    else:
        messagebox.showwarning("Error", "Contact not found!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['Phone']}, {details['Email']}")

# Set up the UI components
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Add", command=add_contact)
add_button.grid(row=3, column=0)

update_button = tk.Button(root, text="Update", command=update_contact)
update_button.grid(row=3, column=1)

delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=3, column=2)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=4, column=0, columnspan=3)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=5, column=0, columnspan=3)

# Run the main event loop
root.mainloop();