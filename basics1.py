import tkinter as tk

def calculate_product():
    try:
            value11 = float(entry11.get())
            value12 = float(entry12.get())

            result1 = value11 + value12
            entry13.delete(0, tk.END)
            entry13.insert(0, str(result1))
        
    except ValueError:
            entry13.delete(0, tk.END)
            entry13.insert(0, "")
    
    try:
            value21 = float(entry21.get())
            value22 = float(entry22.get())

            result2 = value21 - value22
            entry23.delete(0, tk.END)
            entry23.insert(0, str(result2))
    except ValueError:
            entry23.delete(0, tk.END)
            entry23.insert(0, "")

    try:
            value31 = float(entry31.get())
            value32 = float(entry32.get())

            result3 = value31 * value32
            entry33.delete(0, tk.END)
            entry33.insert(0, str(result3))
    except ValueError:
            entry33.delete(0, tk.END)
            entry33.insert(0, "")

    try:
            value41 = float(entry41.get())
            value42 = float(entry42.get())

            result4 = value41 / value42
            entry43.delete(0, tk.END)
            entry43.insert(0, str(result4))
    except ValueError:
            entry43.delete(0, tk.END)
            entry43.insert(0, "")

root = tk.Tk()
root.title("Prosty kalkulator")
root.geometry("500x250")

label1 = tk.Label(root, text="Liczba 1:")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Liczba 2:")
label2.grid(row=0, column=2, padx=10, pady=10)

label3 = tk.Label(root, text="Wynik:")
label3.grid(row=0, column=4, padx=10, pady=10)

label4 = tk.Label(root, text="+")
label4.grid(row=1, column=1, padx=10, pady=10)

label5 = tk.Label(root, text="=")
label5.grid(row=1, column=3, padx=10, pady=10)

label6 = tk.Label(root, text="-")
label6.grid(row=2, column=1, padx=10, pady=10)

label7 = tk.Label(root, text="=")
label7.grid(row=2, column=3, padx=10, pady=10)

label8 = tk.Label(root, text="*")
label8.grid(row=3, column=1, padx=10, pady=10)

label9 = tk.Label(root, text="=")
label9.grid(row=3, column=3, padx=10, pady=10)

label10 = tk.Label(root, text="/")
label10.grid(row=4, column=1, padx=10, pady=10)

label11 = tk.Label(root, text="=")
label11.grid(row=4, column=3, padx=10, pady=10)

entry11 = tk.Entry(root)
entry11.grid(row=1, column=0, padx=10, pady=10)

entry12 = tk.Entry(root)
entry12.grid(row=1, column=2, padx=10, pady=10)

entry13 = tk.Entry(root)
entry13.grid(row=1, column=4, padx=10, pady=10)

entry21 = tk.Entry(root)
entry21.grid(row=2, column=0, padx=10, pady=10)

entry22 = tk.Entry(root)
entry22.grid(row=2, column=2, padx=10, pady=10)

entry23 = tk.Entry(root)
entry23.grid(row=2, column=4, padx=10, pady=10)

entry31 = tk.Entry(root)
entry31.grid(row=3, column=0, padx=10, pady=10)

entry32 = tk.Entry(root)
entry32.grid(row=3, column=2, padx=10, pady=10)

entry33 = tk.Entry(root)
entry33.grid(row=3, column=4, padx=10, pady=10)

entry41 = tk.Entry(root)
entry41.grid(row=4, column=0, padx=10, pady=10)

entry42 = tk.Entry(root)
entry42.grid(row=4, column=2, padx=10, pady=10)

entry43 = tk.Entry(root)
entry43.grid(row=4, column=4, padx=10, pady=10)

calculate_button = tk.Button(root, text="OBLICZ", command=calculate_product)
calculate_button.grid(row=5, column=2, pady=10)

root.mainloop()
