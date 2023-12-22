#Create the binary filein Python which should contains the student details and to search the particular student based on roll no and display the details.

from pickle import dump, load

def addrec():
    a = open('student.bin','wb+')
    print('Add Students details')
    while True:
        r = int(input("Enter the roll number of the student\t"))
        n = input("Enter the name of the student\t")
        dump([r,n],a)
        if int(input("Enter 0 to add another record otherwise enter 1\t")):
            break
    a.close()

def searchrec():
    a = open('student.bin','rb')
    r = int(input("Enter the roll number of the student\t"))
    found = 0
    try:
        while True:
            f = load(a)
            if f[0] == r:
                print("The searched roll number is found and the details are :", f)
                found = 1
                break
    except:
        a.close()
    if not found:
        print("The details of the student with that roll number is not available")

addrec()
searchrec()
