class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        print('['+str(self.x)+','+str(self.y)+']')
    def norm(self):
        return self.x*self.x + self.y*self.y
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
        
