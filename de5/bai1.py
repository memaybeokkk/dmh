f2=open('bai1.out','w')

def doixung(s):
	for i in range(len(s)//2):
		s=s.rstrip('\n')
		if s[i]!=s[len(s)-i-1]:
			return False
	return True
with open('bai1.inp','r') as f1:
	n=f1.readline()
	for i in range(int(n)):
		if doixung(f1.readline()):
			f2.write('CO')
			f2.write('\n')
		else:
			f2.write('KHONG')
			f2.write('\n')
f2.close()
