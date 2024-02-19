def partition(arr,low,high):
	pivot=arr[high]
	i=low-1
	for j in range(low,high):
		if arr[j]<=pivot:
			i=i+1
			(arr[i],arr[j])=(arr[j],arr[i])

	(arr[i+1],arr[high])=(arr[high],arr[i+1])
	return i+1

def quickSort(arr,low,high):
	if(low<high):
		pi = partition(arr,low,high)

		quickSort(arr,low,pi-1)
		
		quickSort(arr,pi+1,high)


n=int(input("Enter the number of elements: "))
arr=[]
print("Enter the elements")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Unsorted Array")
print(arr)

quickSort(arr,0,n-1)

print('Sorted Array in Ascending Order:')
print(arr)
