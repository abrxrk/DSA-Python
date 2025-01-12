""""
ask a number from userr
Print “Fizz” if the number is divisible by 3.
Print “Buzz” if the number is divisible by 5.
Print “FizzBuzz” if the number is divisible by 3 and 5.
Print the number itself if none of the conditions are true.
"""
a=int(input('Enter a number= '))
if a%3==0 and a%5!=0:
    print('Fizz')
elif a%5==0 and a%3!=0:
    print('Buzz')
elif a%3==0 and a%5==0:
    print('FizzBuzz')
else:
    print(a)