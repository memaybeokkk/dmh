n=[int(x) for x in input().split()]
l=[]
for i in n:
    if 10<i<20:
        l.append(i)
print(sum(l))
