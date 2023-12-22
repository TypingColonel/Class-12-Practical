def count():
    with open('/home/psanjay/Desktop/python works/class 12 programs/story.txt') as a: #Enter your path
        c=v=u=l=0
        n = a.read()
        for i in n:
            if str(i).isalpha():
                if i.isupper():
                    u += 1
                else:
                    l += 1
                if i.lower() in 'aeiou':
                    v += 1
                else:
                    c += 1
    print("The text file is\n",n,'\nThe total number of Consonants in the file :', c,'\nThe total number of Vowels in the file :', v,'\nThe total number of Upper Case characters in the file:',u,'\nThe total number of Lower case characters in the file :',l)        

count()