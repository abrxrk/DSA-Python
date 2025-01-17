"""
Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the user.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
n = int(input("enter the old number- "))
new = int(input("enter the new number- "))
for i in range(0, len(a)):
    if n == a[i]:
        a[i] = new
print(a)
