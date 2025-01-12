#Write a program to check if the number is ODD, EVEN or Equal to Zero.
a=int(input('Enter the given number- '))
if a%2 == 0 and a!=0:
    print('The number is even ')
elif a==0:
    print('The number is zero')
else:
    print('The number is odd' )