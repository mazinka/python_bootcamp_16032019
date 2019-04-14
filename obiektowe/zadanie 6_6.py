class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'vector({self.x},{self.y})'

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return vector(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return vector(self.x * other.x, self.y * other.y)
        # return self * other # inny zapis tego ww
        #return self.__mul__(other) # inny zapis tego ww


    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)


    def __eg__(self, other):
        return (self.x ** 2 + self.y ** 2) == (other.x ** 2 + other.y ** 2)

    def __le__(self, other):
        return (self.x ** 2 + self.y ** 2) <= (other.x ** 2 + other.y ** 2)

if __name__ =='__main__':
    v1 = Vector(1,2)
    assert (v1)


    print(vector(1,2) + vector(1,2))
    print(vector(1,2)*3)
    print(3*vector(1,2))
    print(vector(1,2) < vector(3,2))
    print(vector(1, 2) >= vector(1,2)

