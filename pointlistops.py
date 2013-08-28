
def partition(A,p,q,val):
    x=A[p][val]
    i=p
    for j in range(i+1,q+1):
        if(A[j][val]<=x):
            i=i+1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
    temp=A[p]
    A[p]=A[i]
    A[i]=temp
    return i

def qsort(A,p,r,val):
    if(p<r):
        q=partition(A,p,r,val)
        qsort(A,p,q-1,val)
        qsort(A,q+1,r,val)

def quickSort(A,val):
    qsort(A,0,len(A)-1,val)

def sortByX(L):
    return quickSort(L,0)

def sortByY(L):
    return quickSort(L,1)

