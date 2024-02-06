def find_median(arr,r,c):
    med=[]
    for i in range(r):
        for j in range(c):
            med.append(arr[i][j])
    med=sorted(med)
    print(med)
    median=int(((r*c)-1)/2)
    print("The median of the array is: ",med[median])


arr=[]

row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
print("Enter array elements ")
for i in range(row):
    a=[]
    for j in range(col):
        n=int(input("Enter element: "))
        a.append(n)
    arr.append(a)
find_median(arr,row,col)



        
