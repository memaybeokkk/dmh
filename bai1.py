n=int(input())
dem=0
i=0
while i<n+1:
    if dem ==15:
        dem=0
        print('\n')
    if i %2 == 0:
        print(i,end='   ')
        dem+=1
    i+=1
