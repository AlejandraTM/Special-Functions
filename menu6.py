import os
import sys
from scipy import special
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-1, 1, 0.01)
fig, ax = plt.subplots() 

a=int(sys.argv[2])

if a > 5:
	if a == 6:
		y=special.eval_chebyt(0,x)
		y1=special.eval_chebyt(1,x)
		line, =ax.plot(x, y,'--',linewidth=2, label='$T_0 (x)$') 
		ax.plot(x, y1, label='$T_1 (x)$') 
	elif a == 7:
		y=special.eval_chebyt(0,x)
		y1=special.eval_chebyt(1,x)
		y2=special.eval_chebyt(2,x)
		line, =ax.plot(x, y,'--',linewidth=2, label='$T_0 (x)$') 
		ax.plot(x, y1, label='$T_1 (x)$') 
		line, =ax.plot(x, y2,'--',linewidth=2, label='$T_2 (x)$') 
	elif a == 8:
		y=special.eval_chebyt(0,x)
		y1=special.eval_chebyt(1,x)
		y2=special.eval_chebyt(2,x)
		y3=special.eval_chebyt(3,x)
		line, =ax.plot(x, y,'--',linewidth=2, label='$T_0 (x)$') 
		ax.plot(x, y1, label='$T_1 (x)$') 
		line, =ax.plot(x, y2,'--',linewidth=2, label='$T_2 (x)$') 
		ax.plot(x, y3, label='$T_3 (x)$') 
	elif a == 9:
		y=special.eval_chebyt(0,x)
		y1=special.eval_chebyt(1,x)
		y2=special.eval_chebyt(2,x)
		y3=special.eval_chebyt(3,x)
		y4=special.eval_chebyt(4,x)
		line, =ax.plot(x, y,'--',linewidth=2, label='$T_0 (x)$') 
		ax.plot(x, y1, label='$T_1 (x)$') 
		line, =ax.plot(x, y2,'--',linewidth=2, label='$T_2 (x)$') 
		ax.plot(x, y3, label='$T_3 (x)$') 
		line, =ax.plot(x, y4,'--',linewidth=2, label='$T_4 (x)$') 
	elif a == 10:
		y=special.eval_chebyt(0,x)
		y1=special.eval_chebyt(1,x)
		y2=special.eval_chebyt(2,x)
		y3=special.eval_chebyt(3,x)
		y4=special.eval_chebyt(4,x)
		y5=special.eval_chebyt(5,x)
		line, =ax.plot(x, y,'--',linewidth=2, label='$T_0 (x)$') 
		ax.plot(x, y1, label='$T_1 (x)$') 
		line, =ax.plot(x, y2,'--',linewidth=2, label='$T_2 (x)$') 
		ax.plot(x, y3, label='$T_3 (x)$') 
		line, =ax.plot(x, y4,'--',linewidth=2, label='$T_4 (x)$') 
		ax.plot(x, y5, label='$T_5 (x)$')
else:
	y=special.eval_chebyt(a,x)
	ax.plot(x, y, label='$T_%i (x)$'%a) 

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
		             box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
		      fancybox=True, shadow=True, ncol=3);
plt.title("Chebyshev's first kind polynomials",fontsize = 15, color = '0.20', verticalalignment = 'baseline', horizontalalignment = 'center')

plt.xlim(-1, 1)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.show()

