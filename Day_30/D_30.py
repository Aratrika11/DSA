def bubble_sort(arr,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    a=int(input("Enter the element:"))
    arr.append(a)
print("Unsorted Array is:",arr)
bubble_sort(arr,n)

print("Sorted array is:")
for i in range(n):
    print(arr[i],end=" ")
