def gt(x):
	if x==1:
		return 1
	else:
		return x*gt(x-1)
print(gt(3))