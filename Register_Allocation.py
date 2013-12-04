""

    This program solves the register allocation problem, given as part of the AI course for Autumn 2013-14
    It takes input in the manner specified - the first line being the number of registers, the second being
    the number of temporaries (identified by characters a to z), the third being the number of edges of the
    graph and then the remaining lines after that specifying the end-points for each edge.

    The program implements DFS, DFS with forward checking, DFS with forward checking and MRV heuristic,
    DFS with forward checking and degree heuristic, and arc consistency.

"""

import math
from queue import Queue

def sortdegrees(): #To sort the adjacency list in order of degrees of neighbours
    count = dict()
    for i in temps:
        count[i]=len(edgeList[i])
    for i in temps:
        l = count[i]
        for j in range(0,l-1):
            for k in range(j+1,l):
                if(count[edgeList[i][j]]<count[edgeList[i][k]]):
                    temp=edgeList[i][j]
                    edgeList[i][j]=edgeList[i][k]
                    edgeList[i][k]=temp

def getConnections(): #To obtain the connected components of the graph
    global edgeList
    global connected
    global temps
    global graphs
    count = -1
    q=Queue()
    for i in temps:
        if(connected[i]!=-1):
            continue
        q.put(i)
        count = count+1
        while(q.empty()==False):
            top = q.get()
            connected[top]=count
            for j in edgeList[top]:
                if(connected[j]==-1):
                    q.put(j)
    j = 0
    numcount=[0]*(count+1)
    for i in temps:
        numcount[connected[i]]=numcount[connected[i]]+1
    for i in temps:
        if(connected[i]==j):
            graphs[i]=numcount[j]
            j=j+1
    
def isFinalSolution(allotments):#To check if a solution is valid
    global visited
    for i in allotments.keys():
        d = allotments[i]
        if(visited[i]==1):
            if(d==-1):
                return False
            for j in edgeList[i]:
                if(allotments[j]==d):
                    return False
        else:
            return False
    return True

def isLegal(allotments,node,d):#To check if an assignment is legal
    for i in edgeList[node]:
        if(allotments[i]==d):
            return False
    return True

def dfSearch(allotments,node,count,totcount):#Recursive function for depth-first search
    global visited
    global assignment
    global flag
    visited[node]=1
    if(count==totcount):
        assignment = dict(allotments)
        flag = True
        return 0
    for nbr in edgeList[node]:
        for val in regs:
            copy=dict(allotments)
            if(copy[nbr]==-1 and isLegal(copy,nbr,val)):
                copy[nbr]=val
                if(dfSearch(copy,nbr,count+1,totcount)==0):
                    return 0
    return 1

def depthFirstSearch():
    global assignment
    global graphs
    global flag
    for i in graphs.keys():
        dummy=dict(assignment)
        dummy[i]=regs[0]
        flag=False
        dfSearch(dummy,i,1,graphs[i])
        if(flag==False):
            break


def dfsFwdCheck(allotments,node,domains,iden):
    global assignment
    global flag
    if(areDomainsSat(domains,iden)==True):
        for i in domains:
            if(connected[i]==iden):
                assignment[i]=domains[i][0]
        flag = True
        return 0
    for nbr in edgeList[node]:
        if(allotments[nbr]==-1):
            for val in domains[nbr]:
                domcopy=dict(domains)
                copy=dict(allotments)
                copy[nbr]=val
                domcopy[nbr]=[val]
                for nnbr in edgeList[nbr]:
                    if(val in domains[nnbr]):
                       domcopy[nnbr].remove(val)
                if(dfsFwdCheck(copy,nbr,domcopy,iden)==0):
                    return 0
    return 1


def forwardChecking():

    global assignment
    global domain
    global flag
    for i in graphs.keys():
        domcopy=dict(domain)
        dummy=dict(assignment)
        dummy[i]=regs[0]
        domcopy[i]=[regs[0]]
        flag=False
        for nbr in edgeList[i]:
            domcopy[nbr].remove(dummy[i])
        dfsFwdCheck(dummy,i,domcopy,connected[i])
        if(flag==False):
            break

def forwardWDegree():
    sortdegrees()
    forwardChecking()

def dfsFwdCheckMRV(allotments,node,domains,iden):
    global assignment
    global flag
    if(areDomainsSat(domains,iden)==True):
        for i in domains:
            if(connected[i]==iden):
                assignment[i]=domains[i][0]
        flag = True
        return 0
    domlist = list(edgeList[node])
    l = len(domlist)
    for i in range(0,l-1):
        for j in range(i+1,l):
            if(len(domains[i])>len(domains[j])):
                temp=domlist[i]
                domlist[i]=domlist[j]
                domlist[j]=temp
    for nbr in domlist:
        if(allotments[nbr]==-1):
            for val in domains[nbr]:
                domcopy=dict(domains)
                copy=dict(allotments)
                copy[nbr]=val
                domcopy[nbr]=[val]
                for nnbr in edgeList[nbr]:
                    if(val in domains[nnbr]):
                       domcopy[nnbr].remove(val)
                if(dfsFwdCheckMRV(copy,nbr,domcopy,iden)==0):
                    return 0
    return 1


def forwardCheckingMRV():
    global flag
    global assignment
    global domain
    for i in graphs.keys():
        domcopy=dict(domain)
        dummy=dict(assignment)
        dummy[i]=regs[0]
        domcopy[i]=[regs[0]]
        flag=False
        for nbr in edgeList[i]:
            domcopy[nbr].remove(dummy[i])
        dfsFwdCheck(dummy,i,domcopy,connected[i])
        if(flag==False):
            break

def makeArcConsistent(domains,allotments,node,nbr):
    if(allotments[node]==-1):
        for i in domains[node]:
            locflag = False
            for j in domains[nbr]:
                if(i!=j):
                    locflag=True
                    break
            if(locflag==False):
                domains[node].remove(i)
    
def areDomainsSat(domains,iden):
    for i in domains.keys():
        if(connected[i]==iden):
            if(len(domains[i])!=1):
                return False
    return True

def makeAllArcsConsistent(domains,allotments):
    for arc in arclist:
        makeArcConsistent(domains,allotments,arc[0],arc[1])

def dfsFwdCheckArcConsistency(allotments,node,domains,iden):
    global assignment
    global flag
    if(areDomainsSat(domains,iden)==True):
        for i in domains:
            if(connected[i]==iden):
                assignment[i]=domains[i][0]
        flag = True
        return 0
    makeAllArcsConsistent(domains,allotments)
    for nbr in edgeList[node]:
        if(allotments[nbr]==-1):
            for val in domains[nbr]:
                copy=dict(allotments)
                domcopy=dict(domains)
                domcopy[nbr]=[val]
                copy[nbr]=val
                if(dfsFwdCheckArcConsistency(copy,nbr,domcopy,iden)==0):
                    return 0
    return 1

def forwardArcConsistent():
    global assignment
    global domain
    global flag
    for i in graphs.keys():
        domcopy=dict(domain)
        dummy=dict(assignment)
        dummy[i]=regs[0]
        flag=False
        domcopy[i]=[regs[0]]
        dfsFwdCheckArcConsistency(dummy,i,domcopy,connected[i])
        if(flag==False):
            break

#The common part of the program

flag = False;   
f = open('ai_inp.txt','r')
numReg=int(f.readline()) #Number of registers read
regs = list(range(numReg)) 
regs = [1+x for x in regs]
numTemps=int(f.readline()) #Number of temporaries
temps = [chr(97+i) for i in range(numTemps)] #Temporaries represented as characters
nEdges=int(f.readline())
edgeList = dict() #For the adjacency list representation
assignment = dict() #For the allotments
domain=dict() #For storing the domains
visited = dict()#To check if a node has been visited
connected = dict() #For computing the connected subgraphs
arclist = list() #For storing the arcs
graphs = dict() #A custom data structure for storing the first node, and size of each connected component

for i in temps:
    domain[i]=list(regs)
for i in temps:
    edgeList[i] = list()
    assignment[i]=-1
    visited[i]=-1
    connected[i]=-1
for i in range(nEdges):
    edge = f.readline()
    edge=edge.split()
    arclist.append((edge[0],edge[1]))
    arclist.append((edge[1],edge[0]))
    edgeList[edge[0]].append(edge[1])
    edgeList[edge[1]].append(edge[0])
getConnections() #Computes the connected components

#The various methods are outlined here. Uncomment any one and compile and run to try it out. Do not uncomment more or less than one.

#depthFirstSearch()
#forwardChecking()
#forwardCheckingMRV()
#forwardWDegree()
#forwardArcConsistent()
f.close()
fout = open('AI_output.txt','w')
if(flag==True):
    for i in assignment.keys():
        fout.write('{0}\t{1}\n'.format(i,assignment[i]))
else:
    fout.write('No Solution Exists!')
fout.close()
