#comparing indices
def merge(l,r):
	ml=[]
	while len(l)>0 and len(r)>0:
		if l[0] <= r[0]:
			ml.append(l.pop(0))
		else:
			ml.append(r.pop(0))
	if len(l)>0:
		return ml+l
	else:
		return ml+r
	
def rec_merge_data(data):
	if len(data)<=1:
		return data
	else:
		m = len(data)//2
		l = rec_merge_data(data[:m]) #shorter
		r = rec_merge_data(data[m:]) 
	return merge(l,r)
		
def main():
	data = [1,2,4,3,5,6,7,8,9,10]
	print(rec_merge_data(data))

main()

# split list until len = 1 for all sub lists
# append smaller value, comparing 2 sublists at a time
# repeat^
