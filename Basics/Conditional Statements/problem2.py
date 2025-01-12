#take an input of physics and chem marks and print pass only if passed in both 
a=int(input('Enter the marks of physics- '))
b=int(input('Enter the marks of chemistry- '))
if a&b>=37:
    print('You have passed')
else:
    print('You have failed')
print('Thank you')