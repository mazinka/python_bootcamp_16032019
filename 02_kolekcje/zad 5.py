x=[]
i=0

print("", end="")

for i in range(10):
    for i in range(10):
        print(f"{i:3}", end=" ")
    print()


for j in range(10):
    for j in range(10):
        print(f"{j*i:3}", end=" ")
    print()
