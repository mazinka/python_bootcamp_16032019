liczby=input("podaj 2 wymiary rozdzielając je przecinkiem")


a,b =liczby.split(",")
a,b=int(a),int(b)
dzialanie=input("dzialanie")

if dzialanie=="+":
    print(a+b)
elif dzialanie=="-":
    print(a-b)
elif dzialanie=="*":
    print(a*b)
elif dzialanie=="%":
    print(a%b)
else:
    print("zrobiles cos magicznego")

print(f"wynik=dzialanie")
