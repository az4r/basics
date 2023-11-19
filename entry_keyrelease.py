import tkinter as tk

def aktualizacja_pola2(*args):
        entry2.delete(0, tk.END)
        wynik2 = float(entry1.get()) * 2
        entry2.insert(0, wynik2)

root = tk.Tk()
root.title("Kalkulator")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry1.bind("<KeyRelease>", aktualizacja_pola2)

label1 = tk.Label(root, text=" x 2 = ")
label1.grid(row=0, column=2)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=3)

root.mainloop()