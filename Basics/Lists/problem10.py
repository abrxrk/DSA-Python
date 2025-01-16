# Make your own list. Find the sum of all numbers divisible by 3 or 4.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 24]
sum = 0
for i in range(0, len(a)):
    if a[i] % 3 == 0 and a[i] % 4 == 0:
        sum = sum + a[i]
print(sum)
