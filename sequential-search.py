
#if the list is not sorted
alist=[0,534,-1,24,3,4,777,222,456] # list of elements
def sequentialsearch(templist,element):
	position=0
	found=False
	length=len(templist)
	while position<length:
		if element==templist[position]:
			found=True
			print("element found at position,",position)
			break
		else:
			position=position+1
	return found

print("unsorted list:",alist)			
element=int(input("enter the number you wanna search in the list:"))			
print(sequentialsearch(alist,element))							