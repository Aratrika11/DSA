def selection_sort(arr,n):
    for i in range(n):
        mini=i
        for j in range(i + 1, n):
            if arr[j]<arr[mini]:
                mini=j

        arr[i],arr[mini]=arr[mini],arr[i]

arr=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    a=int(input("Enter the element: "))
    arr.append(a)
    
print("Original array:", arr)
selection_sort(arr,n)
print("Sorted array:", arr)
