# Write a Python code to nd the second largest element in a list without sorting.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
largest = 0
second_largest = 0
for i in a:
    if i > largest:
        largest = i
a.remove(largest)
for i in a:
    if i > second_largest:
        second_largest = i
print(second_largest)
