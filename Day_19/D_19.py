def varient(arr,trgt):
    pos=p=[]
    c=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]+arr[j]==trgt):
                p=[(i,j)]
                pos.append(p)
                c=c+1
    if(c>0):
        print("1st varient: YES")
        for p in pos:
            print("2nd Varient: Array Index: ",p)
    else:
        print("Target not found")


arr=[]
n=int(input("Enter the number of elements: "))
print("Enter ",n," array elements: \n")
for i in range(n):
    el=int(input("Enter element: "))
    arr.append(el)
t=int(input("Enter the target value: "))
varient(arr,t)
