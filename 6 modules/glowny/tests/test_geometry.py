from mathematica.geometry.figures import square_area, triangle_area


def test_square_area():
    assert square_area(3) == 9
    assert square_area(5) == 25


def test_traingle_area():
    assert triangle_area(2,2) ==0,5*2*2