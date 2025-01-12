#Write a program to check if the last digit of a number is divisible by 5 or not.
a=int(input('Enter a number= '))
result = a%10
if result%5 == 0:
    print('The number is divisble by 5')
else:
    print('The number is not divisible by 5')