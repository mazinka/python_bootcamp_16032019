
#try:


    ##f.write('trzecia linia')
#print(f)
#print(f.read())

#f.close()

#with open ("pierwszy.txt", 'a', encoding="cp1250") as f:
  #  f.write('trzecia linia\n')

#print(f)


with open("drugi.txt", "w", encoding="utf8") as f:
    f.write('cos tam')

    for l in f:
        print(l)

for l in enumerate(['a','b','c'])


import sys
print(sys.argv)