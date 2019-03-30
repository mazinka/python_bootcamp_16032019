liczby =[5,2,1,4,3] # liczby [1,2,5,4,3]

# tu będziemy modyfikować liczby

i_max=liczby.index(max(liczby))
i_min=liczby.index(min(liczby))




#temp=liczby[i_min] #tu jest jedynka
#liczby[i_min}=liczby[i_max]  #tam gdzie 1wrzucam 5
#liczby[i_max]=temp #tam gdzie 5 wrzeucam 1 z temp
#print(liczby)
#assert lista==[5,2,1,4,3]

#liczby[i_min], liczby[i_max] = liczby[i_max], liczby[i_min]

#print(i_max,i_min)

temp_max=liczby[0]
temp_min=liczby[0]
#symulujemy działanie max tu są zapisywane wartości liczb
#for el in liczby:
 #   if el>temp_max:
   #     temp_max=el
  #  if el< temp_min:
   #     temp_min=el

#teraz chcemy użyc indeksów ale bez używania fuknjci index

#for el in range(len(liczby)):
   # if liczby[el]>temp_max:
    #    temp_max=liczby[el]
      #  temp_max_i=el
 #   if liczby[el]< temp_min:
    #    temp_min=liczby[el]
     #   temp_min_i=el

#enumerate

for i, v in enumerate(liczby):
    print(i,v)