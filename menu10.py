import os
import sys
from scipy import special
import numpy as np
import matplotlib.pyplot as plt
import math

a=int(sys.argv[2])
x= np.arange(-10, 10, 0.01)

fig, ax = plt.subplots() 
if a < 7:
	y=special.eval_hermite(a,x)
	ax.plot(x, y,label='$H_%i (x)$'%a)
	if a < 4:	
		plt.ylim(-6, 6)
		plt.xlim(-2, 2)
	else:
		plt.xlim(-2, 2)
		plt.ylim(-180, 180)
elif a == 7:
	y1=special.eval_hermite(0,x)
	y2=special.eval_hermite(1,x)
	y3=special.eval_hermite(2,x)
	y4=special.eval_hermite(3,x)
	ax.plot(x, y1,label='$H_0 (x)$')
	ax.plot(x, y2,'--',linewidth=2,label='$H_1 (x)$')
	ax.plot(x, y3,label='$H_2 (x)$') 
	ax.plot(x, y4,'--',linewidth=2,label='$H_3 (x)$')
	plt.ylim(-6, 6)
	plt.xlim(-2, 2)
elif a == 8:
	y5=special.eval_hermite(4,x)
	y6=special.eval_hermite(5,x)
	y7=special.eval_hermite(6,x)
	ax.plot(x, y5,label='$H_4 (x)$') 
	ax.plot(x, y6,'--',linewidth=2,label='$H_5 (x)$') 
	ax.plot(x, y7,label='$H_6 (x)$')
	plt.xlim(-2, 2)
	plt.ylim(-200, 200) 

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=4);

plt.title( "Hermite Polynomials.",fontsize = 15, color = '0.20', verticalalignment = 'baseline', horizontalalignment = 'center')

plt.grid(True)
plt.show()
