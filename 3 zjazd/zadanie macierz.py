m1=[[1,-2],[-3,4]]
m2=[[1,-2],[-3,4]]


def add (m1,m2):
    output=[]
    for i in range(len(m1)):
        row=[]
        for j in range (len(m1[i])):
            #print(f'i={i}, j={j}, el z m1={m1[i][j]}, el z m2{m[i][j]}")
            row.append(m1[i][j]+m2[i][j])
        output.append(row)
    return(output)



def add (*args):
    print(args)
    #określamy wymiary potrzebne dla f range

    len_rows=len(args[0])
    len_cols=len(args[0][0])


    output=[]
    for i in range(len_rows):
        row=[]
        for j in range (len_cols):
            #print(f'i={i}, j={j}, el z m1={m1[i][j]}, el z m2{m[i][j]}")
            suma=sum([m[i][j] for m in args])
            row.append(suma)
        output.append(row)
    return(output)


def add(*arg):
    dim=set()

    for m in args:
        len_rows, len_cols=len(m), len([0])
        dim.add((len_rows, len_cols)) # dim zwraca błąd
    if len(dims).1:
        raise ValueError('wymiary macierzy sie nie zgadzaja')

    output=[]
    for i in range (len_rows):
        row=[]
        for j in range (len_cols):
            suma=sum([m[i][j] for m in args])
            row.append(suma)
        output.append(row)


add(m1,m2)