def rec_insertion(arr,n):
    if n <= 1:
        return
    rec_insertion(arr,n-1)

    last_ele=arr[n-1]
    j=n-2
    
    while(j>=0 and arr[j]>last_ele):
        arr[j+1]=arr[j]
        j-=1
    
    arr[j+1]=last_ele


arr=[]
n=int(input("Enter number of elements: "))
print("Enter array elements: ")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Unsorted array: ",arr)
rec_insertion(arr, n)
print("Sorted array is: ", arr)
