def ast(m):
    n=m;
    tong=0;kt=False
    l=len(str(n))
    while n>0:
        du=n%10
        tong+=du**l
        n=n//10
    if tong==m:
        kt=True
    
    return kt
for i in range(100,9999):
    if ast(i):
        print(i)

