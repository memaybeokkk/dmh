n=[int(x) for x in input().split()]
print(n)
s=[0]*(max(n)+1)
for i in n:
    s[i]+=1
for i in range(0,max(n)+1):
    if s[i]!=0:
        print(i,':',s[i])
