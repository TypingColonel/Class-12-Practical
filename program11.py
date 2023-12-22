#Create the binary file in Python which should contains the student details and to delete the particular student based on roll no. 

from os import remove,rename
from pickle import load,dump

def addrec():
    a = open('student3.bin','wb')
    while True:
        f = int(input("Enter the roll number of the student\t"))
        r = input("Enter the name of the student\t")
        n = int(input("Enter the total marks of the student\t"))
        dump([f,r,n],a)
        if int(input("To add another record press 0 otherwise enter 1\t")):
            print("The records have been entered")
            break
    a.close()
    
def searchrec():
    a = open('student3.bin','rb+')
    m = open('tempstudent3.bin','wb+')
    r = int(input("Enter the roll number of the student you want to delete\t"))
    found = 0
    print("Displaying all records")
    try:
        while True:
            i = load(a)
            print(i)
            if i[0] == r:
                found = 1
                print("The record with the roll number",r,"has been deleted")
            else:
                dump(i,m)
    except:
        a.close()
        m.close()
        remove('student3.bin')
        rename('tempstudent3.bin','student3.bin')
        
    if not found:
        print("The record of the student with the roll number",r,'is not available')
        
addrec()
searchrec()
