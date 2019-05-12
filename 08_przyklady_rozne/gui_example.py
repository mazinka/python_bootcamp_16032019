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

label_arg_a = tkinter.Label(master=root, text='a')
label_arg_a.pack()
arg_a = tkinter.Entry(master=root)
arg_a.pack()

label_arg_b = tkinter.Label(master=root, text='b')
label_arg_b.pack()
arg_b= tkinter.Entry(master=root)
arg_b.pack()

button_dodaj =tkinter.Button(master=root, text ="dodaj", command=sumuj)
button_dodaj.pack()

button_odejmij =tkinter.Button(master=root, text ="odejmij", command=odejmij)
button_odejmij.pack()

wynik =tkinter.Label(master=root, text="-")

root.title('sumator') #tytuł
root.mainloop() #pętla w okienku



print('to sie dzieje koniec')