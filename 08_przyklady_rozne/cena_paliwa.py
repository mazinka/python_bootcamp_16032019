import tkinter


def dystans():
    dystans = float(arg_a.get())
    km = float(arg_b.get())
    cena = float(arg_c.get())
    w = (dystans/100) * cena * km
    wynik.configure(text=f"wynik:{w}")

root = tkinter.Tk()
root.columnconfigure(2, weight=1)
label_arg_a = tkinter.Label(master=root, text='dystans') #nazwa wiersza
label_arg_a.grid(row=0, column=0)
arg_a = tkinter.Entry(master=root) #robi pasek
arg_a.grid(row=0, column=2) #pozycjonowanie

label_arg_b = tkinter.Label(master=root, text='km')
label_arg_b.grid(row=1, column=0)
arg_b= tkinter.Entry(master=root)
arg_b.grid(row=1, column=2)


label_arg_c = tkinter.Label(master=root, text='cena')
label_arg_c.grid(row=2, column=0)
arg_c= tkinter.Entry(master=root)
arg_c.grid(row=2, column=2)


button_oblicz = tkinter.Button(master=root, text ="oblicz", command = dystans)
button_oblicz.grid(row=7, column=2)


wynik =tkinter.Label(master=root, text="-")
wynik.grid(row=3, column=0)

root.title('zuzycie paliwa')
root.mainloop()