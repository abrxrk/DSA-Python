# Write a program to nd and print all odd numbers within a given list.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in a:
    if i % 2 == 1:
        b.append(i)
print(b)
