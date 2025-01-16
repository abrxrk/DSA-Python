# . Make your own list. Print the largest number present in that list.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = 0
# if a[0] >= largest:
#     largest = a[0]
for i in range(0, len(a)):
    if a[i] > largest:
        largest = a[i]
print(largest)
