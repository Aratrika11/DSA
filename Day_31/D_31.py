def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    
    left=merge_sort(left)
    right=merge_sort(right)
    
    return merge(left,right)

def merge(left,right):
    merged=[]
    left_idx,right_idx=0,0
    
    while left_idx <len(left) and right_idx<len(right):
        if left[left_idx]<right[right_idx]:
            merged.append(left[left_idx])
            left_idx+=1
        else:
            merged.append(right[right_idx])
            right_idx+=1
    
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

arr=[]
n=int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Unsorted Array: ",arr)
sort=merge_sort(arr)
print("Sorted array:",sort)
