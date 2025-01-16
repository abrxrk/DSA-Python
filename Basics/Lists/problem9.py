# . Make your own list. Find the sum of all even numbers present in that list.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        sum = sum + a[i]
print(sum)
