#Write a program to create a phone contact book and also to do search,update and delete contact.

pb = {}

def addcontact():
    a = input("Enter the name of the contact\t")
    b = int(input("Enter the phone number\t"))
    if len(str(b)) == 10:
        print('the con2tact is been saved')
    else:
        print("the number entered is invaild, try again")
    pb[a] = b

def updatecontact():
    k = input("enter the name whose contact you want to change\t")
    if k in pb:
        l = int(input("Enter the updated phone number\t"))
        if len(str(l)) == 10:
            pb[k] = l
    else: 
        print("the entered name is not avalible")

def searchcontact():
    k = input("Enter the name of the contact you want to search for\t")
    if k in pb:
        print("The number of the contact",k,"is",pb[k])
    else:
        print("The given contact is not available")
        
def deletecontact():
    k = input("Enter the contact you want to delete\t")
    if k in pb:
        del pb[k]
        print("\nThe entered contact has been deleted")
    else:
        print("The given contact is not available")

print("\ncontact book program")
while True:
    k = int(input("\n1. Add contact\n2. Update contact\n3. Search contact\n4. Delete contact\n5. quit program\t")) 
    if k == 1:
        addcontact()
    elif k == 2:
        updatecontact()
    elif k == 3:
        searchcontact()
    elif k == 4:
        deletecontact()
    elif k == 5:
        print("Thanks for using this program")
        break
    else:
        print("Invalid option, try again")
