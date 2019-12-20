import pandas as pd 
from Point3D import *
from Point3Dimport import *
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

headers = ["px","py","pz","pux","puy","puz","qx","qy","qz","vux","vuy","vuz","c1","c2"]
df = pd.read_csv("TrackExact.txt",delimiter=" ",names = headers)
#print(df.shape)


xList=[]
yList=[]
zList=[]

for index in range(df.shape[0]):
    if((index%10000)==0):
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
    #print('POCA')
    x = POCA()
    #x.Point3DPoca(p,u,q,v).show()
    pocaPt = x.Point3DPoca(p,u,q,v)
    #pocaPt.show()
    if(pocaPt[0].z < 450 and pocaPt[0].z > -450):
        xList.append(pocaPt[0].x)
        yList.append(pocaPt[0].y)
        zList.append(pocaPt[0].z)
#plt.scatter([row[13],row[14]],color=['red'],)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#cm = plt.get_cmap("RdYlGn")   to get red yellow green
cm = plt.get_cmap("Spectral")
xArray = np.array(xList)
yArray = np.array(yList)
zArray = np.array(zList)

N = len(xList)
col=np.arange(N)

#print len(xArray)
#print len(yArray)
#print len(zArray)
#plt.scatter (xArray,yArray,s=1,c=col,cmap=cm) for 3D scatter plot
ax.scatter(xArray,yArray,zArray,s=1,c=col,cmap=cm)  #for 3D scatter plot
plt.show()



   
   

 
    
  
  



  

  




    
     

    
    











  





