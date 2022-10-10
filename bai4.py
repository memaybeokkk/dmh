from math import sqrt
n=int(input())
kt=True

if n %2 ==0:
    print(n,' la so chan')
else:
    print(n,' la so le')

for i in range(2, int(sqrt(n)+1)):
    if n%i==0:
        kt=False
        break
if kt==True:
    print(n,' la so nto')
else:
    print(n, 'k la so nto')

s=0
for i in range(1,int(n/2 +1 )):
    if n%i==0:
        s+=i
if s==n:
    print(n,' la so hh')
else:
    print(n,' k la so hh')
