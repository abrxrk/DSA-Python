# Make your own list. Print the sum of all elements present in that list.
sum = 0
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(a)):
    sum = sum + a[i]
    print(sum, end=" ")
print()
print(sum)
