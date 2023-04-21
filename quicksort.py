import random

def quick_sort(data):
	if len(data)<=1:
		return data
	else:
		pivot = random.choice(data)
		data.remove(pivot)
		s=[]
		g=[]
		for e in data:
			if e <=pivot:
				s.append(e)
			else:
				g.append(e)
		return quick_sort(s)+[pivot]+quick_sort(g)
							
def main():
	data = [2,8,5,3,4,7,9]
	print(quick_sort(data))
		
main()

# select a pivot
# greater than, less than lists
# repeat
