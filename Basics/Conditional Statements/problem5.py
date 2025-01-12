# Write a program that takes two numbers as input and checks if the 1st number is divisible by the second.
a=int(input('Enter the first number- '))
b=int(input('Enter the second number- '))
if a%b==0:
    print('The number is divisible.')
else:
    print('The number is not divisible')