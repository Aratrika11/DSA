def anagram(str,st):
    c=0
    n=len(str)
    if(n==len(st)):
        for i in str:
            for j in st:
                if(i==j):
                    c=c+1
        if(c==n):
            print(st," ",str," are anagrams of each other.")
    if(c==0 or c<n):
        print(st,"&",str," are not anagrams")

s1=input("Enter a word: ")
s2=input("Enter another word: ")
anagram(s1,s2)
