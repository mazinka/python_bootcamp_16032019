zdanie="ale ma <kotajhyttgb>, a kot ma ale"

nawias="<>"
licznik=0
czy_zliczac=False



for el in zdanie:
   if el==">":
       czy_zliczac=False
   elif el=="<":
       czy_zliczac=True
   elif czy_zliczac:
       licznik+=1

print(licznik)
