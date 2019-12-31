import cv2 
from matplotlib import pyplot as plt 

img = cv2.imread ("imashish.jpg")

canny = [img]

for i in range (1):
  plt.subplot(1,1,i+1),plt.imshow(images[i],'gray')
  plt.xticks([]),plt.yticks([])
plt.show()
