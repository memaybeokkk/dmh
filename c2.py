a,b=[int(x) for x in input().split()]
s=0
a=str(a)
b=str(b)
for i in range(len(a)):
    for j in range(len(b)):
        s+=int(a[i])*int(b[j])
print(s)

