# Make your own list. Print how many positive and negative numbers are here.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]
positive = 0
negative = 0
for i in range(0, len(a)):
    if a[i] > 0:
        positive += 1
    if a[i] < 0:
        negative += 1
print(positive)
print(negative)
