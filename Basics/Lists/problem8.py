# Make your own list. Count how many numbers are divisible by both 2 and 5 in that list.
count = 0
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(a)):
    if a[i] % 2 == 0 and a[i] % 5 == 0:
        count = count + 1
print(count)
