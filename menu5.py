import os
from scipy import special 
import numpy as np
import sys
import matplotlib.pyplot as plt

x= np.arange(-1.0, 1.0, 0.0001)
fig, ax = plt.subplots()

y7= special.eval_gegenbauer(6,0.5,x)
y9= special.eval_gegenbauer(6,0,x)
y10= special.eval_gegenbauer(6,1,x)

line, =ax.plot(x, y7,'--',linewidth=2, label='P. of Legendre') 
line, =ax.plot(x, y9,'--',linewidth=2, label='P. of Chebyshev I') 
line, =ax.plot(x, y10,'--',linewidth=2, label='P. of Chebyshev II') 
	
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3);
plt.title('Gegenbauer Polynomials.',fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
plt.xlim(-1, 1)
plt.ylim(-2, 2)
plt.grid(True)
plt.show()
