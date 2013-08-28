"""
This is a file of random useful methods and algorithms collected in Python,
as I was exploring the sheer ease of use of this language

"""

#Searchs for an element in an ascending sorted list. Returns the position found otherwise -11
def binSearchAscending(A,val):
    l=0
    u=len(A)-1
    while(l<=u):
        mid=(l+u)//2
        if(val<A[mid]):
            u=mid-1
        elif(val>A[mid]):
            l=mid+1
        else:
            return mid
    return -1

#Returns the longest common subsequence between two arrays
#Input - Two lists of characters
#Output - The longest common subsequence as a string
def lcs(s1,s2):
    A=list(s1)
    B=list(s2)
    m=len(A)
    n=len(B)
    c=[[0]*(n+1)]*(m+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(A[i-1]==B[j-1]):
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    i=m
    j=n
    seq=''
    while(c[i][j]!=0):
        if(A[i-1]==B[j-1]):
            seq=A[i-1]+seq
            i=i-1
            j=j-1
        else:
            if(c[i-1][j]>c[i][j-1]):
                i=i-1
            else:
                j=j-1
    return seq

