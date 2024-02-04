def shift_zero(arr):
    non_neg= 0
    for i in range(len(arr)):
        if(arr[i]>0):
            arr[non_neg],arr[i]=arr[i],arr[non_neg]
            non_neg=non_neg+1

    for i in range(non_neg,len(arr)):
        arr[i]=0

    return arr

n=int(input("Enter number of elements: "))
arr=[]
for i in range(n):
    a=int(input("Enter the element: "))
    arr.append(a)
print("After shifting: ",shift_zero(arr))
