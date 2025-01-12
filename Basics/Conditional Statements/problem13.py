#Write a program to calculate bill. Ask the nal amount from the user. You have to give discount and print the nal bill after discount.
a=int(input('Enter the bill amount- '))
if a>=50000:
    print('You get 30% discount')
    a= a - (30*a/100)
    print(f'your final bill amount is {a}')
elif a>=40000 and a<49999:
    print('You get 25% discount')
    a= a - (25*a/100)
    print(f'your final bill amount is {a}')
elif a>=30000 and a<=39999:
    print('You get 20% discount')
    a= a - (20*a/100)
    print(f'your final bill amount is {a}')
elif a>=10000 and a<=29999:
    print('You get 10% discount')
    a= a - (10*a/100)
    print(f'your final bill amount is {a}')
else:
    print('You get no discount')
   
