# Ask a string from user. Count how many alphabets are there in that string.
a = input("enter a string- ")
count = 0
for i in a:
    if i.isalpha():
        count = count + 1
print(count)
