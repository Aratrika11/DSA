import sys
arr=[]
floor=-1
ceil=99999
n=int(input("Enter number of elements: "))
print("Enter array elements:")
for i in range(n):
    a=int(input())
    arr.append(a)
arr=sorted(arr)
x=int(input("Enter a number for comaprison: "))

for i in range(0,n):
    if(arr[i]<=x):
        floor=max(floor,arr[i])
    if(arr[i]>=x):
        ceil=min(ceil,arr[i])

print("Floor:",floor)
print("Ceil:",ceil)

        
        
