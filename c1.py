h,a,m,b,s=[x for x in input().split()]
S=int(input('nhap so giay cong vao: '))
s=int(s)+S
s1=s%60
m=int(m)+s//60
m1=m%60
h=int(h)+m//60

print(h,m1,s1,sep=':')
