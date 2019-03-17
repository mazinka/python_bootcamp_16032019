x=[1,-10,20,-30,40,50,60]
liczb_dodatnich=0
liczb_ujemnych=0


for el in x:
    if el>=0:
        liczb_dodatnich +=1
    elif el<=0:
        liczb_ujemnych +=1

    print(f"""liczb dodatnich {liczb_dodatnich},liczb ujemnych {liczb_ujemnych}""")