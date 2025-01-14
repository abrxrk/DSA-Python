#outer loop- no of rows
for i in range(5,0,-1):
    #inner loop- no of coloumns
    for j in range(5,i-1, -1):
        print(j, end=' ')
    print()