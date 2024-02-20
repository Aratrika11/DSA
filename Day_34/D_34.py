a=int(input("Enter total no. of lines: "))
n=a//2
for i in range(1,n+1,2):
    for k in range(i,n):
        print(" ",end=" ")
    for j in range(1,i*2):
        if(j%2==0):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")
for i in range(n,0,-2):
    for k in range(i,n):
        print(" ",end=" ")
    for j in range(1,i*2):
        if(j%2==0):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("\n")
