# Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
a = []
b = []
for i in range(1, 11):
    c = int(input(f"enter the {i} number- "))
    a.append(c)
print(a)
for i in range(len(a) - 1, -1, -1):
    b.append(a[i])
print(b)
