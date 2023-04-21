
def bubble(l):
	for i in range(len(l)-1):
		k = l[i]
		if l[i+1]<k:
			l[i]=l[i+1]
			l[i+1]=k
			bubble(l)
	return l
			
def main():
	print(bubble([7,2,1,4,5]))
	
main()

# comparing n index with n+1 index
