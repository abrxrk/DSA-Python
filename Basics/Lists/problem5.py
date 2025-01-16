# Make your own list. Print all the elements present at even index position.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")
