import os
import sys
from scipy import special
import numpy as np
import matplotlib.pyplot as plt

a=int(sys.argv[2])

if a>7:
	x = np.linspace(0, 30, 1000)
	fig, ax = plt.subplots()

	y= special.yv(a, x)
	b=a-8
	ax.plot(x, y, label='$Y_ %i (x)$'%b) 

	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
		         box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
		  fancybox=True, shadow=True, ncol=1);

	plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')

	plt.hlines(0, 0, 30) 
	plt.xlim(0, 30)
	plt.ylim(-1, .4)
	plt.grid(True)
	plt.show()

else: 
	if a==7:
		x= np.linspace(0,20, 100)
		fig, ax = plt.subplots()
		y= special.yv(0, x)
		y2= special.yv(1, x)
		y3= special.yv(2, x)
		y4= special.yv(3, x)
		y5= special.yv(4, x)
		y6= special.yv(5, x)
		y7= special.yv(6, x)

		ax.plot(x, y, label='$Y_0 (x)$') 
		line, =ax.plot(x, y2,'--', label='$Y_1 (x)$') 
		line, =ax.plot(x, y3,'--',label='$Y_2 (x)$') 
		line, =ax.plot(x, y4,'--', label='$Y_3 (x)$') 
		line, =ax.plot(x, y5,'--',label='$Y_4 (x)$')
		line, =ax.plot(x, y6,'--',label='$Y_5 (x)$')
		line, =ax.plot(x, y7,'--',label='$Y_6 (x)$')

		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
				 box.width, box.height * 0.9])
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
			  fancybox=True, shadow=True, ncol=4);
		plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.hlines(0, 0, 10) 
		plt.xlim(0, 20)
		plt.ylim(-1, 1)
		plt.grid(True)
		plt.show()
	elif a==6:
		x= np.linspace(0,20, 100)
		fig, ax = plt.subplots()
		y= special.yv(0, x)
		y2= special.yv(1, x)
		y3= special.yv(2, x)
		y4= special.yv(3, x)
		y5= special.yv(4, x)
		y6= special.yv(5, x)

		ax.plot(x, y, label='$Y_0 (x)$') 
		line, =ax.plot(x, y2,'--', label='$Y_1 (x)$') 
		line, =ax.plot(x, y3,'--',label='$Y_2 (x)$') 
		line, =ax.plot(x, y4,'--', label='$Y_3 (x)$') 
		line, =ax.plot(x, y5,'--',label='$Y_4 (x)$')
		line, =ax.plot(x, y6,'--',label='$Y_5 (x)$')

		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
				 box.width, box.height * 0.9])
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
			  fancybox=True, shadow=True, ncol=3);
		plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.hlines(0, 0, 10) 
		plt.xlim(0, 20)
		plt.ylim(-1, 1)
		plt.grid(True)
		plt.show()
	elif a==5:
		x= np.linspace(0,20, 100)
		fig, ax = plt.subplots()
		y= special.yv(0, x)
		y2= special.yv(1, x)
		y3= special.yv(2, x)
		y4= special.yv(3, x)
		y5= special.yv(4, x)

		ax.plot(x, y, label='$Y_0 (x)$') 
		line, =ax.plot(x, y2, label='$Y_1 (x)$') 
		line, =ax.plot(x, y3,'--',label='$Y_2 (x)$') 
		line, =ax.plot(x, y4,'--', label='$Y_3 (x)$') 
		line, =ax.plot(x, y5,'--',label='$Y_4 (x)$')

		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
				 box.width, box.height * 0.9])
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
			  fancybox=True, shadow=True, ncol=3);
		plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.hlines(0, 0, 10) 
		plt.xlim(0, 20)
		plt.ylim(-1, 1)
		plt.grid(True)
		plt.show()
	elif a==4:
		x= np.linspace(0,20, 100)
		fig, ax = plt.subplots()
		y= special.yv(0, x)
		y2= special.yv(1, x)
		y3= special.yv(2, x)
		y4= special.yv(3, x)

		ax.plot(x, y, label='$Y_0 (x)$') 
		line, =ax.plot(x, y2,'--', label='$Y_1 (x)$') 
		line, =ax.plot(x, y3,'--',label='$Y_2 (x)$') 
		line, =ax.plot(x, y4,'--',label='$Y_3 (x)$') 

		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
				 box.width, box.height * 0.9])
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
			  fancybox=True, shadow=True, ncol=4);
		plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.hlines(0, 0, 10) 
		plt.xlim(0, 20)
		plt.ylim(-1, 1)
		plt.grid(True)
		plt.show()
	elif a==3:
		x= np.linspace(0,20, 100)
		fig, ax = plt.subplots()
		y= special.yv(0, x)
		y2= special.yv(1, x)
		y3= special.yv(2, x)

		ax.plot(x, y, label='$Y_0 (x)$') 
		line, =ax.plot(x, y2,'--', label='$Y_1 (x)$') 
		line, =ax.plot(x, y3,'--',label='$Y_2 (x)$')

		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
				 box.width, box.height * 0.9])
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
			  fancybox=True, shadow=True, ncol=3);
		plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.hlines(0, 0, 10) 
		plt.xlim(0, 20)
		plt.ylim(-1, 1)
		plt.grid(True)
		plt.show()
	elif a==2:
		x= np.linspace(0,20, 100)
		fig, ax = plt.subplots()
		y= special.yv(0, x)
		y2= special.yv(1, x)

		ax.plot(x, y, label='$Y_0 (x)$') 
		line, =ax.plot(x, y2,'--', label='$Y_1 (x)$') 

		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
				 box.width, box.height * 0.9])
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
			  fancybox=True, shadow=True, ncol=2);
		plt.title("Second class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.hlines(0, 0, 10) 
		plt.xlim(0, 20)
		plt.ylim(-1, 1)
		plt.grid(True)
		plt.show()
