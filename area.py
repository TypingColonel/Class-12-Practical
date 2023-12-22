from math import pi

def square(a):
    return a*a

def rectangle(l,b):
    return l*b

def triangle(b,h):
    return 0.5*b*h

def circle(r):
    return pi*r**2

def cube(a):
    return 6*a*a

def cylinder(r,h):
    return 2*pi*r*(r+h)

def cone(r,h):
    return pi*r**2+h

def sphere(r):
    return (4/3)*pi*r**2