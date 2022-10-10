s=[int(x) for x in input().split()]
dem=0
for i in range (1,s[0]+1):
    for j in range(1,s[1]+1):
        if (i+j)%5==0:
            dem+=1
print(dem)