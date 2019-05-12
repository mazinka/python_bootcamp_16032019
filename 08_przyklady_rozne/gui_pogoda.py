import tkinter

from pogoda import get_location_id, get_location_weather


def pogoda():
    localization_name = localization.get()
    location_id = get_location_id(localization_name)
    weather = get_location_weather(location_id)
    description ='''
    pogoda w {location_name}:
    temperatura: {weather["the_temp"]}
    ciśnienie: {weather["air_pressure"]}
    '''


root = tkinter.Tk()
localization =tkinter.Entry(master=root)
localization.pack()
button =tkinter.Button(master=root, text="pobierz pogode", command=pogoda)
button.pack()


pogoda_label = tkinter.Label(master=root, text=',')
pogoda_label.pack()
root.mainloop()
