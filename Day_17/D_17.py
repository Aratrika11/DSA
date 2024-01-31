def next_permutation(arr):
    n=len(arr)
    i=n-2
    while i>=0 and arr[i]>=arr[i + 1]:
        i-=1
    if i<=0:
        arr.sort()
        return arr
    
    j=n-1
    while arr[j]<=arr[i]and j>i:
        j-=1

    arr[i],arr[j]=arr[j],arr[i]

    arr[i+1:]=reversed(arr[i+1:])

    return arr



arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

print("Output :", next_permutation(arr))
