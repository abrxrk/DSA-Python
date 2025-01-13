#Ask a number from user. Print the multiplication table of that number.
n=int(input('enter the number- '))
i=1
while i<=10:
    print(f'{n} * {i} = {n*i}')
    i=i+1