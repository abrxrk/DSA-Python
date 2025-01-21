# Ask a string from user. Count the number of uppercase and lowercase characters in that String.
a = input("enter a string- ")
upper_count = 0
lower_count = 0
for i in a:
    if i.isupper():
        upper_count = upper_count + 1
    if i.islower():
        lower_count = lower_count + 1
print(upper_count)
print(lower_count)
