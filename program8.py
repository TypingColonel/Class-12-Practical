#Read a text file in Python and count the number of occurrence of the particular word in the file content.

def count_word():
    with open('/home/psanjay/Desktop/python works/class 12 programs/count.txt') as d: #enter your directory
        k = d.read()
        m = input("enter the word you want to count :")
        n = k.count(m)
        print("The word", m,'occurs', n,'times in the file\n\n',k)
        
count_word()
