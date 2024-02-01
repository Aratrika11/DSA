def set_mat_zero(arr,r,c):
    zero_pos=[]
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                zero_pos.append((i, j))

    for position in zero_pos:
        r,c=position
        for i in range(0,r+2):
            arr[i][c]=0
        for j in range(0,c+2):
            arr[r][j]=0

    return arr


row=int(input("Enter number of rows: "))	
col=int(input("Enter number of columns: "))
arr=[]
for i in range(0,row):
    a=[]
    for j in range(0,col):
        n=int(input("Enter a number"))
        a.append(n)
    arr.append(a)

output_matrix = set_mat_zero(arr,row,col)
print("OUTPUT: ",output_matrix)
