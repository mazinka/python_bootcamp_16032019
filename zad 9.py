a=2019
b=int(input("podaj rok urodzenia"))

wynik=a-b
if wynik>18:
    print("jestes staruchem")
elif wynik==18:
    print('spoko jest')
else:
    print("jestes gowniarzem")