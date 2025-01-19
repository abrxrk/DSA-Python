# Make a program that takes a list of integers and returns the product of all the elements.
a = []
for i in range(1, 6):
    c = int(input("enter a number- "))
    a.append(c)
print(a)
product = 1
for i in a:
    product = product * i
print(product)
