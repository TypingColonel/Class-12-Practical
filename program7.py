#write a python program to read lines from a text file "Sample.txt" and copy those lines into another file “new.txt” which are starting with an alphabet 'a' or 'A'. 

def copypaste():
    with open('/home/psanjay/Desktop/python works/class 12 programs/sample.txt') as d:
        with open('/home/psanjay/Desktop/python works/class 12 programs/new.txt','w') as k:
            c = d.readlines()
            for i in c:
                if i.lower().startswith('a'):
                    k.write(i)
    print("All the sentences starting with 'a' or 'A' in 'sample.txt' has been copied to 'new.txt'")
    
copypaste()
