import os
import sys
from scipy import special
import numpy as np
import matplotlib.pyplot as plt
import math

a=int(sys.argv[2])
b=int(sys.argv[3])
c=int(sys.argv[4])

x= np.arange(-100.0, 100.0, 0.01) 

fig, ax = plt.subplots()

y=special.hyp2f1(a, b, c, x) #c<b
y1=special.hyp1f1(a,b, x)#b no 0 # a=100 :0
ax.plot(x, y, label='Hypergeometric') 
ax.plot(x, y1, label='Confluent') 
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=2);
plt.title("Gauss' Hipergeometric Function.",fontsize = 15, color = '0.20', verticalalignment = 'baseline', horizontalalignment = 'center')

plt.xlim(-20,20)
plt.ylim(-2,2)
plt.grid(True)
plt.show()
