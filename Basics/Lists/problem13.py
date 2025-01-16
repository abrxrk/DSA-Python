# Make your own list. Print the smallest number present in that list.
a = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
smallest = a[0]
for i in range(0, len(a)):
    if a[i] < smallest:
        smallest = a[i]
print(smallest)
