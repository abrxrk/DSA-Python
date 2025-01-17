"""
 Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("enter a number- "))

for i in a:
    if i % n == 0:
        a.remove(i)
print(a)
