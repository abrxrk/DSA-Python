#take 5 inputs from user calculate the percentage and print the grades accordingly
maths= int(input('Enter the marks of maths- '))
science= int(input('Enter the marks of science- '))
history= int(input('Enter the marks of history- '))
graphics= int(input('Enter the marks of graphics- '))
bee = int(input('Enter the marks of BEE- '))
total = maths + science + history + graphics + bee
percentage= total/500 * 100
print(f'The percentage is {percentage}%')
if percentage>=90 and percentage<=100 :
    print('A grade')
elif percentage<=90 and percentage>=75:
    print('B grade')
elif percentage<= 75 and percentage>=60:
    print('C grade')
elif percentage<=60 and percentage>=45:
    print('D grade')
elif percentage<=45 and percentage >=35:
    print('Just Pass')
elif percentage<35:
    print('Fail')
else:
    print('Invalid Percentage.')