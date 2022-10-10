a=int(input())
phep=input()
b=int(input())
if phep=='cong':
	tp=a+b 
elif phep=='tru':
	tp=a-b
elif phep=='nhan':
	tp=a*b
else:
	tp=a//b
print(tp)
np=''
while tp>0:
	np+=str(tp%2)
	tp//=2
print(np[::-1])