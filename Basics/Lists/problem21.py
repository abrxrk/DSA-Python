# Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 100]
b = int(input("enter a number- "))
for i in range(0, len(a)):
    if a[i] == b:
        print(i)
if b not in a:
    print("-1")
