

data=[1,2,3,4,5,6,7]
start=lambda x:x>3
stop =lambda x:x==6


def przytnij():
    out=[]
    for el in data:
        if el==start:
            out.append(el)
        else:
            el==stop
            out.append(el)
    return data

def test_przytnij():
    assert data=[1,2,3,4,5,6,7][4,5,6]
    assert start=lambda x:x>3
    assert stop = lambda x:x==6