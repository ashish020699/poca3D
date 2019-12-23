import math
from Point3Dimport import *
from Point3D import *

class scatter3D:
    x=0.0
    y=0.0
    z=0.0
    counter = 0
    def __init__(self,x=0,y=0,z=0,):
	self.x = x 
        self.y = y 
	self.z = z
        
    def show(self):
         print (self.x,self.y,self.z)
    
    def Dimension(self,poca):
         #poca.show()
         if (((poca.x < self.x) and (poca.x > -self.x)) and ((poca.y < self.y) and (poca.y > -self.y)) and ((poca.z < self.z) and (poca.z > -self.z))) :
            self.counter = self.counter +1
            #print(True)
            return  True
         else : 
           #print(False)
            return False
       

if __name__ == "__main__":
    x1 = scatter3D(100,100,100)
    x1.show()  
    
    p = Point3D(-117.21449274449008726,45.916641758033790666,2460)
    q = Point3D(-173.7718497565388702,-168.5293770107115563,460)
    u = Point3D(-199.22932412975865191,-265.04195381916900942,-440.00000000000011369) 
    v = Point3D(-255.81901232680456815,-479.56320266897358806,-2440)
    #p = Point3D(1,2,3)
    #u = Point3D(4,6,5)
    #q = Point3D(2,3,4)
    #v = Point3D(5,8,6)
       
    pocaPt = POCA()
    po_sc = pocaPt.Point3DPoca(p,u,q,v)
    
    
    x1.Dimension(po_sc[0])


    Poca_new = pocaPt.Point3DPocaIterative(p,u,q,v)
    x1.Dimension(Poca_new)


