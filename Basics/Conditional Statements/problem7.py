#take 3 numbers from user and print the largest number amongst the three
a=int(input('Enter the first number- '))
b=int(input('Enter the second number- '))
c=int(input('Enter the third number- '))
if a>b & a>c:
    print('A is the largest number')
elif b>a and b>c:
    print('B is the largest number')
else:
    print('C is the largest number')