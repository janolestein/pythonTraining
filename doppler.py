def doppler(func):
    def g(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return g

# bestimmt diese Funktion gleichzeitg auch die Parameter Anzahl die an g übergegen werden kann?
def test_f(x,y,z):
    return(x+y+z)

g = doppler(test_f) #Hier wird mit Hilfe von doppler aus der Funktion f die Funktion g

assert g(1,2,3) == 12, "((1+2+3)*2 should equal 12"
print(g(1,2,3))
assert g(-1,0,1) == 0, "((-1+0-1)*2 should equal 0"
print(g(-1,0,1))
assert g(-1,0,1) == 0, "((-1+0-1)*2 should equal 0"
print(g(-1,0,1))
assert g(x=1,y=2,z=3) == 12, "((1+2+3)*2 should equal 12"
print(g(x=1, y=2, z=3))
assert g(1,y=2,z=3) == 12, "((1+2+3)*2 should equal 12"
print(g(9, y=2, z=3))
