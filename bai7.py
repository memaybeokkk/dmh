import time
tb=time.time()
n=9999999
a=[]
while n>0:
    du=n%10
    a.append(du)
    n=n//10
print(sum(a))
print(time.time()-tb)
