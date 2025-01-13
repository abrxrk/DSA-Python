#Calculate factorial of a number entered by user.
n=int(input('enter the number- '))
i=n
product=1
while i>=1:
    product=product*i
    i=i-1
print(product)