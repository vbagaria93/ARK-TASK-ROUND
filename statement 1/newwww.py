def q(a,b,x):
	for i in range (x,len(a)-len(b)+1):
		if a[i:i+len(b)]==b:
			return 0
	return 1
a=input("Enter the sequence of activities as described by the user: \n")
def w(a,c):
	for i in range (0,len(a)-c):
		d=a[i:i+c]
		if q(a,d,i+c-1)==1:
			print(d)
			return
	return w(a,c+1)
w(a,1)		
