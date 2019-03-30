produkty={'ziemniaki': 1.99,
          'bataty':5.99,
            'pomidory': 6}
magazyn={'ziemniaki': 40,
          'bataty':20,
            'pomidory': 15}
koszyk={}

print('uruchiles program kasjer. przyszedl klinet[k] czy chcesz dodac do magazynu m')
komenda=input()


if komenda=='k':
    print("witaj w nasazym sklepie oto fajna oferta, taniej niz w biedronce")
    for pr in produkty:
        print(f'{pr} w cenie: {produkty[pr]} za kg')

    while True:...

    for pr in koszyk:
        print(f'za {pr}: {koszyk[pr]PLN')
    print("="*30)
    print(f'suma: sum(koszyk.values())}')


co_kupi = input('co chcesz kupic')


while True:
    print()
    co_kupi=input('co chcesz kupic [k-koniec]?')
    if co_kupi =='k':
        break
    if co_kupi in produkty:
        ile=float(input(f'ile chcesz [{co_kupi}]:'))
        if ile > magazyn[co_kupi]:
            print('nie ma tyle produktu')
        else:
            cena = float(ile) * produkty [co_kupi]
            koszyk[co_kupi] = koszyk.get(co_kupi,0) + round(cena,2)
            magazyn[co_kupi] -= ile
    else:
        print ('sorki zabrakło')


for pr in koszyk:
    print(f'za {pr}: {koszyk[pr]} PLN')
    print("="*30)
print(f'suma: {sum(koszyk.values())}')

#for pr in input:
  #  if pr=='ziemniaki':
   # print(produkty[ziemniaki])
   # elif pr=='bataty'
   # print(produkty[bataty])
   # elif pr == 'pomidory'
   # print(produkty[pomidory])
#else:
   # print('zabrakło na magazynie, szukaj gdzie indziej')

#ile_produktu = input ("wpisz wage")
#    if pr == 'ziemniaki':
 #   print([ziemniaki]*input(ile_produktu))
  #  elif pr == 'bataty'
   # print([bataty]*input(ile_produktu))
    #elif pr == 'pomidory'
    #print([pomidory]*input(ile_produktu))