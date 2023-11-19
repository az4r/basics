import tkinter as tk
from tkinter import ttk

def entry1_calculate():
    try:
        result1.config(text=f"{float(entry1.get()) + 2} kN")
    except ValueError:
        result1.config(text=f" - ")

def entry2_calculate():
    try:
        result2.config(text=f"{float(entry2.get()) - 2} kN")
    except ValueError:
        result2.config(text=f" - ")

def oblicz():
    entry1_calculate()
    entry2_calculate()

root = tk.Tk()
root.title("Kalkulator kN")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Dane")

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Wyniki")

discription1 = ttk.Label(tab1, text="Dodawanie (x+2): ")
discription1.grid(row=0, column=0, sticky="e")

discription2 = ttk.Label(tab1, text="Odejmowanie (x-2): ")
discription2.grid(row=1, column=0, sticky="e")

entry1 = ttk.Entry(tab1)
entry1.grid(row=0, column=1)

entry2 = ttk.Entry(tab1)
entry2.grid(row=1, column=1)

resultdiscription1 = ttk.Label(tab2, text="Wynik dodawania: ")
resultdiscription1.grid(row=0, column=0, sticky="e")

resultdiscription2 = ttk.Label(tab2, text="Wynik odejmowania: ")
resultdiscription2.grid(row=1, column=0, sticky="e")

result1 = ttk.Label(tab2, text=" - ")
result1.grid(row=0, column=1, sticky="w")

result2 = ttk.Label(tab2, text=" - ")
result2.grid(row=1, column=1, sticky="w")

calculate_button = ttk.Button(tab1, text="Oblicz", command=oblicz)
calculate_button.grid(row=3, column=0, sticky="NSEW")

root.mainloop()