# Make your own list. Count the number of all the even numbers present in the list.
count = 0
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        count += 1
print(count)
