n=int(input())
j=1

d1=0
for i in range(1,1000000):
    d2=0
    while d2<i:
        if j%i==0:
            d1+=1
            d2+=1
            j+=i
        else:
            j+=1
        
    if d1==n:
        print(j-i)
        break

