import os
from scipy import special 
import numpy as np
import sys
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
# recibir 2 variables
c=int(sys.argv[3])
a=int(sys.argv[2])
if c < 5: # es c<5
	y=special.lpmv(a,c,x)

	fig, ax = plt.subplots()
	ax.plot(x, y, label='$P_%i^%i (x)$'%(a,c)) ## el valor de a

	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
		         box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
		  fancybox=True, shadow=True, ncol=1);

	plt.title('Associated Legendre polynomials.',fontsize = 15, color = '0.20', 	verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.axhline(0, color="black")
	plt.xlim(-1, 1)
	if a==0:
		if c==0:
			plt.ylim(-1.2, 1.2)
		else:
			plt.ylim(-1, 1)
        elif a==1:
		if c==1:
			plt.ylim(-1.2, 1.2)
		elif c==2:
			plt.ylim(-1.6, 1.6)
		elif c==3:
			plt.ylim(-2.2, 2.2)
		else:
			plt.ylim(-3, 3)
	else: 
		if c==2:
			plt.ylim(-1, 4)
		elif c==3:
			plt.ylim(-6, 6)
		else:
			plt.ylim(-10, 10)
	plt.grid(True)
	plt.show()

else:
	x = np.linspace(-1, 1, 100)

	y6=special.lpmv(a,1,x)
	y7=special.lpmv(a,2,x)
	y8=special.lpmv(a,3,x)
	y9=special.lpmv(a,4,x)

	fig, ax = plt.subplots()

	line, =ax.plot(x, y6, '--', linewidth=2, label='$P_%i ^1 (x)$'%a)
	line, =ax.plot(x, y7, '--', linewidth=2,label='$P_%i ^2 (x)$'%a) 
	ax.plot(x, y8, label='$P_%i^3 (x)$'%a)  
	ax.plot(x, y9, label='$P_%i^4 (x)$'%a)  
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
		         box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
		  fancybox=True, shadow=True, ncol=4);

	plt.axhline(0, color="black")
	plt.axvline(0, color="black")
	plt.xlim(-1, 1)
	if a==1:
		plt.title('Associated Legendre polynomials.',fontsize = 15, color = '0.20', 	verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.ylim(-3, 3)
	elif a==0:
		plt.title("Legendre's polynomials.",fontsize = 15, color = '0.20', 	verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.ylim(-1, 1)
	else:
		plt.title('Associated Legendre polynomials.',fontsize = 15, color = '0.20', 	verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.ylim(-10, 10)
	plt.grid(True)
	plt.show()
