a=[int(x) for x in input().split()]
dem=0
min=a[0]
for i in range(len(a)):
    if a[i] <= min:
        min=a[i]
        dem=i
print(dem)
