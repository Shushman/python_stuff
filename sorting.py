#This module is a collection of simple useful sorting procedures. The sorting is done in place.

def mergeLists(L1,L2):
    len1=len(L1)
    len2=len(L2)
    res=list()
    i=0
    j=0
    while (i<len1 and j<len2):
	    if(L1[i]<L2[j]):
	    	res.append(L1[i])
	    	i=i+1
	    else:
    		res.append(L2[j])
    		j=j+1
    while(i<len1):
    	res.append(L1[i])
    	i=i+1
    while(j<len2):
    	res.append(L2[j])
    	j=j+1
    return res

def mergeSortAscending(A):
    n=len(A)
    if n==1:
        return A
    else:
        return mergeLists(mergeSort(A[:n//2]),mergeSort(A[n//2:]))

# --------------------------------------------------------------------------

def partitionAscending(A,p,q):
    x=A[p]
    i=p
    for j in range(i+1,q+1):
        if(A[j]<=x):
            i=i+1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
    temp=A[p]
    A[p]=A[i]
    A[i]=temp
    return i

def qsortAscending(A,p,r):
    if(p<r):
        q=partitionAscending(A,p,r)
        qsortAscending(A,p,q-1)
        qsortAscending(A,q+1,r)

def quickSortAscending(A):
    qsortAscending(A,0,len(A)-1)


    
