from math import sqrt
a,b,c=[int(x) for x in input('nhap do dai cac canh').split()]
tg='tam giac thuong'
chuvi=a+b+c
p=chuvi/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
    tg='tam giac vuong'
if a==b or b==c or a==c:
    tg='tam gia can'
print(round(chuvi,2),round(s,2),round(2*s/a,2),round(2*s/b,2),round(2*s/c,2),tg)
