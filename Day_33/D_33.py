n=int(input("Input value of N for N-dimensional Triangle:"))
print(n,"-Dimensional Triangle is as follows:")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
