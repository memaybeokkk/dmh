a=[int(i) for i in input().split()]
dem=0
min=a[0]
for i in range(len(a)):
    if a[i] <= min:
        min=a[i]
        dem=i
max=max(a)
a[a.index(max)]=a[dem]
a[dem]=max
print(a)
