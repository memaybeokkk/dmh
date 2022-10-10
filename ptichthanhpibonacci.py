n=int(input())
a=[1,1]
i=0
while a[i+1]<n:
    a.append(a[i]+a[i+1])
    i+=1
a.pop(-1)
i=len(a)-1
while n!=0 and i>=0:
    if n-a[i]>0:
        print(a[i],',',end='')
        n=n-a[i]
    elif n-a[i]==0:
        print(a[i])
        n=n-a[i]
  
    i-=1   
