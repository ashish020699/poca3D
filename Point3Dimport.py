'''
This Code consists of 2 methods under class POCA 
1) Point3DPoca : It's used to find Poca Points 
2) Point3DPocaIterative : It's used to calculate Iterative Poca until difference btweeen 2 points is below 0.01.

'''
from Point3D import *
import math

class POCA:
   x=0.0
   y=0.0
   z=0.0
   
   def __init__(self,x=0,y=0,z=0):
	self.x = x 
        self.y = y 
	self.z = z
   
   def show(self):
         print (self.x,self.y,self.z)
   
   def Point3DPoca(self,p,u,q,v):

    ang=u.angle(v)
    #print("Angle : "+str(ang))
    if(ang < 0.00000000001):
        return Point3D(0,0,0),Point3D(0,0,0),Point3D(0,0,0)
    pdotv=p.dot(v)
    pdotu=p.dot(u)
    qdotv=q.dot(v)
    qdotu=q.dot(u)
    udotv=u.dot(v)
    uMagnitude=u.Magnitude2()
    vMagnitude=v.Magnitude2()
   
    a = -(pdotv-qdotv)/udotv
    b1 = udotv*(pdotu-qdotu)
    b2 = uMagnitude*(pdotv-qdotv)
    b = b1-b2
    c = (-udotv*udotv+vMagnitude*uMagnitude)
    d = (-vMagnitude*b/udotv*c)
    s = a+d
   
    numerator = (udotv*(pdotu-qdotu)- uMagnitude*(pdotv-qdotv))
    #print("UDotV : "+str(udotv)+" : UMag : "+str(uMagnitude)+ " : vMag : "+str(vMagnitude))
    denominator = (udotv*udotv-uMagnitude*vMagnitude)
    #print("Deno : "+str(denominator))
   
    t = numerator/denominator
   
    p1 = p+u*s
    q1 = q+v*t
   
    poca = (p1+q1)/2
    poca.color=ang
    #poca.show()
    return poca,p1,q1

   def Point3DPocaIterative(self,p,u,q,v):
    ang=u.angle(v)
    #print("Angle : "+str(ang))
    if(ang < 0.00000000001):
        return Point3D(0,0,0),Point3D(0,0,0),Point3D(0,0,0)
    iterations=5
    nList=[]
    for iterNo in range(iterations):
     
      if(iterNo==0):
        poca,p1,q1=self.Point3DPoca(p,u,q,v)
        #poca.show()
        mag_poca = poca.Magnitude()
        nList.append(mag_poca)
      else:
        u=(p1.trisect1(q1)-p).Unit()
        tempQ=p1.trisect2(q1)
        v=(q-tempQ).Unit()
        q=tempQ
        poca,p1,q1=self.Point3DPoca(p,u,q,v)
       
        Pocaiter_Mag = poca.Magnitude()
        #print Pocaiter_Mag
        nList.append(Pocaiter_Mag)
        diff = (nList[iterNo]-nList[(iterNo-1)])
        while diff > 0.01:       
          #poca.show()            
          break 
    return poca,p1,q1    
    #print(nList)   
      
      
if __name__== "__main__":
    p1 = Point3D(4,6,8)
    
    p2 = Point3D(2,2,2)
   
    #midpoint(p1,p2).show()
   
    p = Point3D(1,2,3)
    pu = Point3D(4,6,5)
    q = Point3D(2,3,4)
    vu = Point3D(5,8,6)
        
    c = p1+p2
    #c.show()
    sub = p1-p2
    #sub.show()
    #print('mag p1:' ,p1.Magnitude())
    #print('p1dotp2 :' ,p1.dot(p2))
    #print('p1anglep2 :' ,p1.angle(p2))    
    j = p1.Unit()
    #j.show()  
    p21 =(pu-p)
    #p21.show()
    t = (p21.Magnitude())
    #print ('u is :')
    u = Point3D(p21.x/t,p21.y/t,p21.z/t)
    #u.show()
    p43 =(vu-q)
    #p43.show()
   
    k = (p43.Magnitude())
    #print ('v is :')
    v = Point3D(p43.x/k,p43.y/k,p43.z/k)
    #v.show()

    x = POCA()
    pocaPt = x.Point3DPoca(p,u,q,v)[0]
    pocaPt.show()
    
    #l =  u.angle(v)
    #print l
    #pocaPt.color=l
    #print("Color : "+str(pocaPt[0].color))

    print("====Poca after Iterations==========")
    x.Point3DPocaIterative(p,u,q,v)[0].show()







