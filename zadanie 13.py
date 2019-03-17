temperatura=int(input("podaj temp w danym dniu"))


a,b,c,d,e=temperatura.split(",")
a,b,c,d,e=int(a), int(b), int(c), int(d), int(e)


i=0
temperatura =0
while i!=7:
    temperatura +=i
    i +=1
    print(i, temperatura)

print("srednia",temperatura/i)


i=0
suma_temperatur=0

while True:
    komenda=input ("podaj temperature lub zakoncz")
    if komenda=="k":
        break
suma_temperatur += float(komenda)
i=i+1
print(i, suma_temperatur)

print("srednia", suma_temperatur,i, suma_temperatur/i)


