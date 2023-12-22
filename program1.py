#PROGRAM -1: Write the program to find the given string is palindrome or not

print("\npalindrom checking program")
l = input("\nEnter a check to check for\t")
if l[::-1] == l:
    print("\nThe string",l,'is a palindrome string')
else:
    print("\nThe string",l, 'is NOT a palindrom string')
