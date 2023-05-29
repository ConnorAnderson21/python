def area():    
    l = input("length")
    w = input("width")
    a = int(l) * int(w)
    return(a)

area()


from math import pi

def circumference():
    r = input("radius")
    c = 2.0 * pi * float(r)
    return(c)

circumference()