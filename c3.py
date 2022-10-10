a=[x for x in input().split()]
max=0
tmax=''
dem=0
for i in a:
    dem+=1
    if len(i)>max:
        max=len(i)
        tmax=i
print(dem,'\n',tmax)
