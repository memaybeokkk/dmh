sb='truongnguyendu'
se='nguyenduquannhat'
dmax=0
for i in range(len(sb)):
	if sb[i:]==se[:len(sb)-i]:
		max=sb[i:]
		break
print(max)                                