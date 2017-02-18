
#binary search with list sorted in ascending order
alist=[0,10,30,56,345,555,1000,4342,4545] # list of elements
found=false
def binarysearch-recursive(initial,final):
	mid=(initial+final)//2
	if alist[mid]==element:
		found=True
		return found,mid
	elif alist[mid]<element:
		initial=mid+1
		return binarysearch-recursive(initial,final)
	elif alist[mid]>element:
		final=mid-1
		return binarysearch-recursive(initial,final)
	return found		

element=0
final=len(alist)-1
print(binarysearch-recursive(0,final)


