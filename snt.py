from math import sqrt
a=[True]*1000000000
a[0]=a[1]=False
for i in range(2, int(sqrt(1000000000)+1)):  
    if a[i]== True:
        for j in range(2,1000000000//i):
            a[i*j]=False
print(a[10001])