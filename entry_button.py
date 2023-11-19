import tkinter as tk

def aktualizacja_pola2():
        entry2.delete(0, tk.END)
        entry2.insert(0, float(entry1.get()) * 2)

root = tk.Tk()
root.title("ILOCZYN")
root.resizable(False, False)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label1 = tk.Label(root, text=" x 2 = ")
label1.grid(row=0, column=2)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=3)

calculate_button = tk.Button(root, text="Oblicz", command=aktualizacja_pola2)
calculate_button.grid(row=1, column=2)

root.mainloop()
