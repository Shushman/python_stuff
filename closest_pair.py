import pointlistops #Custom library for operations on lists of points
from math import sqrt

def distance(pt1,pt2):
    return sqrt((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)
    
def getP_L(Px):
    n=len(Px)
    return Px[:(n+1)//2]

def getP_R(Px):
    n=len(Px)
    return Px[(n+1)//2:]

#The recursive method for the DnC implementation
def ClosestPair(Px,Py):
    if(len(Px)==2):
        return distance(Px[0],Px[1])
    if(len(Px)==3):
        return min(distance(Px[0],Px[1]),distance(Px[1],Px[2]),distance(Px[2],Px[0]))
    P_L = getP_L(Px)
    P_R = getP_R(Px)
    d1 = ClosestPair(P_L,Py)
    d2 = ClosestPair(P_R,Py)

    delta = min(d1,d2)
    d=delta
    Qy=list()

    x_med = Px[len(Px)-1][0]
    for pt in Py:
        if(pt[0]>=x_med-delta and pt[0]<=x_med+delta):
            Qy.append(pt)
    n = len(Qy)
    for i in range(n):
        count=0
        j=i-1
        while(j>=0 and count<8):
            d=min(d,distance(Qy[j],Qy[i]))
            count=count+1
            j=j-1
        j=i+1
        count=0
        while(j<n and count<8):
            d=min(d,distance(Qy[j],Qy[i]))
            count=count+1
            j=j+1
        i=i+1
    return d

#Solves the closest pair of points problem by Divide and Conquer (O(nlogn))
#Input - A list of pairs of real numbers
#Eg - [(1.2,3.3),(2.0,3.4),(7.8,10.4)...etc]
#Output - The closest distance between any pair of points i
def getClosestPairDistance(P):
    Px=P[:]
    Py=P[:]
    pointlistops.sortByX(Px)
    pointlistops.sortByY(Py)
    return ClosestPair(Px,Py)

