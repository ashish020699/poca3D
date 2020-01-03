'''
This Code consists of various methods under class Point3D to calculate Poca Points which we are going to read using pandas.
Operator Overloading is used as well.

'''
import math
class Point3D:
    x=0.0
    y=0.0
    z=0.0
    color=0.0
    def __init__(self,x1=0.0,y1=0.0,z1=0.0): # constructor 
        self.x = (x1)
        self.y = (y1)
        self.z = (z1)

    def show(self):
        print(self.x,self.y,self.z)

    def dot(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z

    def Magnitude2(self):
        #print("Magnitude called.........")
	return ((self.x**2)+(self.y**2)+(self.z**2))
          
    def Magnitude(self):
        #print("Magnitude called.........")
	return (math.sqrt(self.Magnitude2()))
    
    def __add__(self,other):
        #print("+ called...........")
        return Point3D(self.x + other.x , self.y + other.y , self.z + other.z)

    def __sub__(self,other):
        return Point3D(self.x - other.x , self.y - other.y , self.z - other.z)

    def angle(self,other):
        cosTheta = self.dot(other)/(self.Magnitude()*other.Magnitude())
        theta = cosTheta
        iTheta = math.acos(cosTheta)
        return iTheta
    
    def Unit(self):
	return Point3D(self.x/self.Magnitude(),self.y/self.Magnitude(),self.z/self.Magnitude())

    def __mul__(self,val):
        return Point3D(self.x*val,self.y*val,self.z*val)
    
    def __div__(self, val):
      return Point3D(self.x/val,self.y/val,self.z/val) 

    def trisect1(self,other):
      return Point3D((other.x+2*self.x)/3,(other.y+2*self.y)/3,(other.z+2*self.z)/3)

    def trisect2(self,other):     
      return Point3D((2*other.x+self.x)/3,(2*other.y+self.y)/3,(2*other.z+self.z)/3)
def midpoint(p1, p2):                                                                    
   g= Point3D((p1.x+p2.x)/2.0,(p1.y+p2.y)/2.0,(p1.z+p2.z)/2.0)                               
   return g

if __name__== "__main__":
    p1 = Point3D(4,2,-6)
    #p1.show()

    p2 = Point3D(10,-16,6)
    #p2.show()
    
    #midpoint(p1,p2).show()
    
    a = Point3D(4,6,8)
    #a.show()
    b = Point3D(2,2,2)
    #b.show()
    x = 2
    div = a/x
    #div.show()
      
    c = a+b
    #c.show() 
    sub = a-b
    #sub.show()
    #print( " magnitude" , c.Magnitude())
    
    #print( "dot",a.dot(b))

    #print("angle ",a.angle(b))
    
    t = a.Unit()
    #t.show()
    #p1.trisect1(p2).show()
    #p1.trisect2(p2).show()












 

