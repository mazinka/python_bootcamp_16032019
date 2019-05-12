import tkinter

def sumuj():
    arg_a_value = int(arg_a.get())
    arg_b_value = int(arg_b.get())
    w = arg_a_value + arg_b_value
    wynik.configure(text=f"wynik:{w}")

def odejmij():
    arg_a_value = int(arg_a.get())
    arg_b_value = int(arg_b.get())
    w = arg_a_value - arg_b_value
    wynik.configure(text=f"wynik:{w}")

root = tkinter.Tk()
root.columnconfigure(2, weight=1)
label_arg_a = tkinter.Label(master=root, text='a')
label_arg_a.grid(row=0, column=0)
arg_a = tkinter.Entry(master=root)
arg_a.grid(row=0, column=2)

label_arg_b = tkinter.Label(master=root, text='b')
label_arg_b.grid(row=0, column=0)
arg_b= tkinter.Entry(master=root)
arg_b.grid(row=0, column=0)

button_dodaj =tkinter.Button(master=root, text ="dodaj", command=sumuj)
button_dodaj.grid(row=0, column=0)

button_odejmij =tkinter.Button(master=root, text ="odejmij", command=odejmij)
button_odejmij.grid(row=0, column=0)

wynik =tkinter.Label(master=root, text="-")
wynik.grid(row=3, column=0)

root.title('sumator')
root.mainloop()

