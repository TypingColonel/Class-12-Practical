from pickle import dump,load

def addrec():
    a = open('student2.bin','wb')
    while True:
        r = int(input("Enter the roll number of the student\t"))
        n = input("Enter name of the student\t")
        m = input("Enter the total marks of the student\t")
        dump([r,n,m],a)
        if int(input("To add another record enter 0 otherwise enter 1\t")):
            print("Records stored successfully")
            break
    a.close
    
def searchrec():
    a = open('student2.bin','rb+')
    p = int(input("Enter the roll number of the student you are searching for\t"))
    found = 0
    try:
        while True:
            k = load(a)
            l = a.tell()
            if k[0] == p:
                print("Record found")
                k[2] = int(input("Enter the updated marks\t"))
                a.seek(l)
                dump(k,a)
                print('The marks of the student',k[1],'has been updated')
                found = 1
                break
    except:
        a.close()
    if not found:
        print("The student with the given roll number is not present")

addrec()
searchrec()