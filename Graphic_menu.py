import tkinter as tk
from tkinter import messagebox
from Polynomial import Polynomial

class PolynomialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Polynomial GUI")
        
        self.poly = Polynomial()

        for all in range(2):
            master.grid_columnconfigure(all, weight=1)

        tk.Label(master, text="Coefficient:").grid(row=0, column=0, sticky='e')
        self.coeff_entry = tk.Entry(master)
        self.coeff_entry.grid(row=0, column=1, sticky='w')

        tk.Label(master, text="Exponent:").grid(row=1, column=0, sticky='e')
        self.exp_entry = tk.Entry(master)
        self.exp_entry.grid(row=1, column=1, sticky='w')

        tk.Button(master, text="Add Term", command=self.add_term).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Organize Polynomial", command=self.organize_polynomial).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Simplify Polynomial", command=self.simplify_polynomial).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Show Polynomial", command=self.show_polynomial).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Exit", command=master.quit).grid(row=6, column=0, columnspan=2, pady=5)

    def add_term(self):
        try:
            coef = int(self.coeff_entry.get())
            exp = int(self.exp_entry.get())
            self.poly.add_term(coef, exp)
            messagebox.showinfo("Success", "Term added successfully.")
            self.coeff_entry.delete(0, tk.END)
            self.exp_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for coefficient and exponent.")

    def organize_polynomial(self):
        self.poly.organize_polynomial()
        messagebox.showinfo("Success", "Polynomial organized successfully.")

    def simplify_polynomial(self):
        self.poly.simplify_polynomial()
        messagebox.showinfo("Success", "Polynomial simplified successfully.")

    def show_polynomial(self):
        result = self.poly.print_polinomial()
        messagebox.showinfo("Polynomial", f"P(x) = {result}")
