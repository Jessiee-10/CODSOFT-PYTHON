import tkinter as tk
from tkinter import messagebox

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)

        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)

        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)

        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name:
            self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        else:
            messagebox.showwarning("Error", "Please enter a name for the contact.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "Contact List:\n"
            for name, details in self.contacts.items():
                contact_list += f"{name}: {details['Phone']}\n"
            messagebox.showinfo("Contacts", contact_list)

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        else:
            messagebox.showwarning("Error", f"Contact '{name}' not found. Cannot update.")

    def delete_contact(self):
        name = self.name_entry.get()

        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        else:
            messagebox.showwarning("Error", f"Contact '{name}' not found.")

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
