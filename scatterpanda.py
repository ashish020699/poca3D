'''
This Code uses TrackExact.txt consisting of 99k rows and 14 columns 
First 12 columns are x,y,z coordinates of vectors p,pu,q and vu respectively
We need to find u and v  to find Poca 
so,
u1 = pu-p and v1 = vu-q
now, Unit vectors of u1 and v1 will give us 'u' and 'v' so that we can plot 'IterativePoca' accurately.
Point3DPocaIterative method of class POCA is used to calculate IterativePoca
'''
import pandas as pd 
from Point3D import *
from Point3Dimport import *
from scatter3D import *
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


headers = ["px","py","pz","pux","puy","puz","qx","qy","qz","vux","vuy","vuz","c1","c2"]
df = pd.read_csv("TrackExact.txt",delimiter=" ",names = headers)
print(df.shape)

xList=[]
yList=[]
zList=[]

x1 = Point3D(100,100,100)
for index in range(df.shape[0]):
    if((index%9000)==0):
        print("Num of Events processed : "+str(index)) 
    row=df.iloc[index]
    #print row

    p = Point3D(row[0],row[1],row[2])
    #p.show()
    pu = Point3D(row[3],row[4],row[5])
    #pu.show()
    q = Point3D(row[6],row[7],row[8])
    #q.show()
    vu = Point3D(row[9],row[10],row[11])
    #vu.show()
    p21 = pu-p
    #p21.show()
    #t = p21.Magnitude()
    #print t
   
    p43 =(vu-q)
    #p43.show()
    u = p21.Unit()
    #u.show()
    #print ("v is :")
    v = p43.Unit()
    #v.show()
        
    pocaPt = POCA()
    po_sc = pocaPt.Point3DPocaIterative(p,u,q,v)
    
    #print(type(po_sc))
    #print(po_sc)
    
    poca=po_sc[0]
    #truePositive=x1.Dimension(poca)


    #if(poca.x < x1.x and poca.x > -x1.x) and (poca.y < x1.y and poca.y > -x1.y) and (poca.z < x1.z and poca.z > -x1.z): //used for box of given dimensions
    #if(truePositive)
    if (poca.z<450 and poca.z>-450):
     xList.append(poca.x)
     yList.append(poca.y)
     zList.append(poca.z)
  

#print("Counter : "+str(x1.counter))
print ("Counter :" +str(len(xList)))




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#cm = plt.get_cmap("RdYlGn")   #to get red yellow green
cm = plt.get_cmap("Spectral")
xArray = np.array(xList)
yArray = np.array(yList)
zArray = np.array(zList)

N =len(xList)

col=np.arange(N)

#print len(xArray)
#print len(yArray)
#print len(zArray)
#plt.scatter (xArray,yArray,s=1,c=col,cmap=cm
ax.scatter(xArray,yArray,zArray,s=1,c=col,cmap=cm)  #for 3D scatter plot
#ax.scatter(xArray,yArray,zArray,s=1)  #for 3D scatter plot with default colors
plt.show()






























