def sdt(x):
    s=0
    for i in range(1,x//2+1):
        if x%i==0:
            s+=i
    return s
n=int(input())
for i in range(n,10000):
    if sdt(i)>i:
        print(i)
        break
