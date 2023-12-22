from area import square, rectangle ,triangle ,circle ,cube ,cylinder ,cone ,sphere

print("\nProgram to check the area")
while True:
    p = int(input("\n 1. Square\t2. Rectangle\t3. Triangle\t4. Circle\t5. Cube\t6. Cylinder\t7. Cone\t8. Sphere\t9. Exit\t"))
    if p == 1:
        a = float(input("\nEnter the perimeter of one side\t"))
        print("\nThe area of the square with side", a,"is",sphere(a))
    elif p == 2:
        l = float(input("\nEnter the length of the reactangle\t"))
        b = float(input("\nEnter the breath of the rectangle\t"))
        print("\nThe area of the rectangle with length", l,"and breath", b,"is given by",rectangle(l,b))
    elif p == 3:
        b = float(input("\nEnter the base of the triangle\t"))
        h = float(input("\nEnter the height of the triangle\t"))
        print("\nThe area of the triangle with the base", b,"and height", h,"is", triangle(b,h))
    elif p == 4:
        r = float(input("\nEnter the radius of the circle\t"))
        print("\nThe area of the circle with radius",r,"is", circle(r))
    elif p == 5:
        r = float(input("\nEnter the radius of the cylinder\t"))
        h = float(input("\nEnter the height of the cylinder\t"))
        print("\nThe area of the cylinder with radius", r,"and height",h,"is",cylinder(r,h))
    elif p == 6:
        r = float(input("\nEnter the radius of the cone\t"))
        h = float(input("\nEnter the height of the cone\t"))
        print("\nThe area of the cone with radius",r,"and height",h,"is",cone(r,h))
    elif p == 7:
        r = float(input("\nEnter the radius of the sphere\t"))
        print("\nThe area of the sphere with radius",r,"is",sphere(r))
    elif p == 8:
        print("\nThanks for using this program")
        break
    else:
        print("\nInvalid option, try again")
        