#Calculate how many numbers are divisible by 7 from 1 to 100.
i=1
while i<=100:
    if i%7==0:
        print(i, end=' ')
    i=i+1