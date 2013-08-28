#Doubly linked list implementation

import sys
class Node:
    def __init__(self,cargo,nxt):
        self.cargo = cargo
        self.next=nxt
    def __str__(self):
        return str(self.cargo)

class DNode:
    def __init__(self,cargo,nxt,prv):
        self.cargo = cargo
        self.next=nxt
        self.prv=prv
    def __str__(self):
        print(self.cargo)
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def isEmpty(self):
        return self.length==0
    
    def addFront(self,cargo):
        self.length=self.length+1
        new=Node(cargo,self.head)
        self.head=new
        if(self.length==1):
            self.tail=new

    def addTail(self,cargo):
        self.length=self.length+1
        new=Node(cargo,None)
        if(self.length==1):
            self.head=new
        else:
            self.tail.next=new
        self.tail=new

    def display(self):
        if self.length==0:
            print("Empty list!")
        else:
            ptr = self.head
            while(ptr!=None):
                sys.stdout.write(str(ptr.cargo))
                sys.stdout.write(' ')
                ptr=ptr.next
        print('')

    def join(self,other):
        self.tail.next(other.head)

    def popHead(self):
        if self.length==0:
            return None
        res = self.head
        self.head=self.head.next
        return res.cargo

    def popTail(self):
        if self.length==0:
            return None
        res=self.tail
        self.tail=None
        return res.cargo

    def delete(self,cargo):
        if self.length==0:
            print("Empty list!")
        else:
            ptr=self.head
            temp=None
            while(ptr.cargo!=cargo and ptr!=None):
                temp=ptr
                ptr=ptr.next
            if(ptr!=None):
                if(ptr==self.head):
                    self.head=self.head.next
                elif(ptr==self.tail):
                    self.tail=None
                else:
                    temp.next=ptr.next
                    
            else:
                print("Value not in list!")

    
    
