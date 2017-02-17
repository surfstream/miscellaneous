
#binary search with list sorted in ascending order
alist=[0,10,30,56,345,555,1000,4342,4545] # list of elements
def binarysearch(templist,element):
	final=len(templist)-1
	initial=0
	mid=(initial+final)//2
	found=False
	while initial<=final and not found:
		if templist[mid]==element:
			found=True
			return found,mid
		elif templist[mid]<element:
			initial=mid+1
			mid=(initial+final)//2
		elif templist[mid]>element:
			final=mid-1
			mid=(initial+final)//2	
				
	return found		

print(alist)
element=int(input("enter the element you wanna search:"))
print(binarysearch(alist,element))

