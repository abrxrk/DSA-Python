#outer loop-no of rows
for i in range(1,6):
    #inner loop- no of spaces
    for j in range(i,5):
        print(' ', end=' ')
    #inner loop- no of coloumns
    for k in range(1,i+1):
        print('*',end=' ')
    print()
