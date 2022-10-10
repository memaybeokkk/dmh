s=input()
s1=s[:-2]
print(s1)
if len(s1)>4:
	print('KHONG')
elif len(s1)==4:
	if (int(s[2:4]) in [1,3,5,7,8,10,12] and int(s[:2])<=31) or (int(s[2:4]) in [4,6,9,11] and int(s[:2])<=30) or (int(s[2:4])==2 and int(s[:2])<=29):
			print('ngay',s[:2],'thang',s[2:4],'nam','20'+str(s[4:]))
	else:
		print('KHONG')
elif len(s1)==2:
	print('ngay',s[0],'thang',s[1],'nam','20'+str(s[2:]))
else:
	print('ngay',s[0],'thang',s[1:3],'nam','20'+str(s[3:]))
	print('ngay',s[:2],'thang',s[2],'nam','20'+str(s[3:]))