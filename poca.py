class poca:
    x=0
    y=0
    z=0

    def __init__(self,x1=0,y1=0,z1=0): # constructor 
        self.x = x1
        self.y = y1
        self.z = z1

    def show(self):
        print(self.x,self.y,self.z)

def midpoint(p1, p2):  #p2 is argument whose value will be given during function call
   g= poca((p1.x+p2.x)/2.0,(p1.y+p2.y)/2.0,(p1.z+p2.z)/2.0) # this will calculate the required midpoints
   return g

if __name__== "__main__":
    p = poca(4,6,8)
    p.show()

    p1 = poca(2,2,2)
    p1.show()
    midpoint(p,p1).show()

  

                                          






