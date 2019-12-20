import math
class Point3D:
    x=0.0
    y=0.0
    z=0.0

    def __init__(self,x1=0.0,y1=0.0,z1=0.0): # constructor 
        self.x = (x1)
        self.y = (y1)
        self.z = (z1)

    def show(self):
        print(self.x,self.y,self.z)

    def Magnitude(self):
         self.x = float(math.sqrt((p.x**2)+(p.y**2)+(p.z**2)))
         self.y = float(math.sqrt((p1.x**2)+(p1.y**2)+(p1.z**2)))
	 print(self.x,self.y)
    
    def dot(self):
         self.x = float (((p).x * (p1).x + (p).y * (p1).y + (p).z * (p1).z))
         print('dot product is ',self.x)    
    
    def sub(self):
        self.x = float (p.x- p1.x) 
 	self.y = float (p.y - p1.y)
        self.z = float (p.z - p1.z)
        print('subtraction is ',self.x,self.y,self.z)  
	
    def add(self):
        self.x = float (p.x + p1.x) 
 	self.y = float (p.y + p1.y)
        self.z = float (p.z + p1.z)
        print('addition is ',self.x,self.y,self.z)
    
    def __add__(self,other):
       return self.x + other.x , self.y + other.y , self.z + other.z

   

def midpoint(p1, p2):                                                                    
   g= Point3D((p1.x+p2.x)/2.0,(p1.y+p2.y)/2.0,(p1.z+p2.z)/2.0)                               
   return g

if __name__== "__main__":
    p = Point3D(4,6,8)
    p.show()

    p1 = Point3D(2,2,2)
    p1.show()
    midpoint(p,p1).show()
    midpoint(p,p1).Magnitude()
    midpoint(p,p1).dot()
    midpoint(p,p1).sub()
    midpoint(p,p1).add()
    a = midpoint(p,p1).__add__(p,p1)
    print a 
    

  

                                          






