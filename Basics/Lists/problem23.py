# Write a program to nd the average of all the numbers present in the list. (Do on your own)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in a:
    sum = sum + i
print(f"the sum of the elements present in the list is- {sum}")
avg = sum / len(a)
print(f"the avg of the elements present in the list is- {avg}")
