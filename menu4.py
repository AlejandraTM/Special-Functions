import os
import sys
from scipy import special
import numpy as np
import matplotlib.pyplot as plt


x= np.arange(-1.0, 1.0, 0.0001)

c=int(sys.argv[3])
a=int(sys.argv[2])
fig, ax = plt.subplots()
if a < 11:
	y= special.eval_gegenbauer(a,c,x)
	ax.plot(x, y, label='$C_%i^%i(x)$'%(a,c)) 
	print "menor 11"
elif a == 11:
	y1= special.eval_gegenbauer(0,c,x)
	y2= special.eval_gegenbauer(1,c,x)
	y3= special.eval_gegenbauer(2,c,x)
	y4= special.eval_gegenbauer(3,c,x)
	y5= special.eval_gegenbauer(4,c,x)
	y6= special.eval_gegenbauer(5,c,x)
	ax.plot(x, y1, label='$C_0 ^{%i} (x)$'%c) 
	ax.plot(x, y2, label='$C_1 ^{%i} (x)$'%c) 
	ax.plot(x, y3, label='$C_2 ^{%i} (x)$'%c) 
	ax.plot(x, y4, label='$C_3 ^{%i} (x)$'%c) 
	ax.plot(x, y5, label='$C_4 ^{%i} (x)$'%c) 
	ax.plot(x, y6, label='$C_5 ^{%i} (x)$'%c)

	print "11"

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3);
plt.title('Gegenbauer Polynomials.',fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
plt.xlim(-1, 1)
plt.ylim(-10, 10)
plt.grid(True)
plt.show()
