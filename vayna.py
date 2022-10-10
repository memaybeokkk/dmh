n,x=[int(x) for x in input().split()]
a=[int(x) for x in input().split()][:n]
s=abs(sum(a))
print(s//x+s%x)
