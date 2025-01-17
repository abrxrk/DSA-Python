"""
Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        odd.append(a[i])
    if a[i] % 2 == 0:
        even.append(a[i])
print(f"the odd numbers in the list are {odd}")
print(f"the even numbers in the list are {even}")
