"""
Write a program that prompts the user to specify the length of a list
and then requests numbers to populate that list. Display the nal list as
the output.
"""

a = int(input("Enter the length of the list- "))
result = []
for i in range(0, a):
    n = int(input("enter a value- "))
    result.append(n)
print(result)
