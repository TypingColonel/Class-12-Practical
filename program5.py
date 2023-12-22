def hashtag():
    a = open('/home/psanjay/Desktop/python works/class 12 programs/story.txt') #enter your directory
    while True:
        k = a.readline()
        k = k.split()
        if k:
            for i in k:
                print(i+'#',end='')
            print('')
        else:
            break
    a.close()
           
hashtag()