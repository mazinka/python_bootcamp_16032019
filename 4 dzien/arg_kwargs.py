
def formatuj(*args,**kwargs):
    print(args)
    print(kwargs)
    zlaczone='\n'.join(args)


    for k in kwargs:

        zlaczone =zlaczone.replace(f'${k}, str(kwargs[k])")
    return zlaczone


def test_formatuj():

    x = formatuj(
        'kwota $cena PLN',
        'kwota $brutto brutto',
        cena=10,
        brutto = 12.3
        )


    assert x=='koszt 10 PLN\nkwota 12.3 brutto'