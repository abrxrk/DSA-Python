# Write a program to reverse the order of words.
a = "python is good"
my_list = a.split(" ")
reverse = my_list[::-1]
ans = " ".join(reverse)
print(ans)
