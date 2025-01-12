#Write a program to check if number is divisible by 2 and 3 but not 8.
a=int(input('Enter the required number- '))
if a%2==0 and a%3==0 and a%8 !=0:
    print('The required number satisfies the condition')
else:
    print('The number does not satisfy the given condition')