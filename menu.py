import os
from scipy import special 
import numpy as np
import sys
import matplotlib.pyplot as plt

opcionMenu=sys.argv[2]

if opcionMenu=="1":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(0, x)
	ax.plot(x, y, label='$J_0 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=1);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20', verticalalignment 			='baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()

elif opcionMenu=="2":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y, y2= special.jv(0, x), special.jv(1, x)
	ax.plot(x, y, label='$J_0 (x)$') 
	line, =ax.plot(x, y2,'--', linewidth=2 ,label='$J_1 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=2);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize =15, color = '0.20', verticalalignment = 			'baseline',horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()

elif opcionMenu=="3":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y, y2, y3= special.jv(0, x), special.jv(1, x), special.jv(2, 			x)
	ax.plot(x, y, label='$J_0 (x)$') 
	line, =ax.plot(x, y2,'--', linewidth=2 ,label='$J_1 (x)$') 
	line, =ax.plot(x, y3,'--',linewidth=2, label='$J_2 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=3);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize =15, color = '0.20', verticalalignment = 			'baseline',horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()

elif opcionMenu=="4":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y, y2, y3, y4= special.jv(0, x), special.jv(1, x), special.jv(2,x), special.jv(3,x)
	ax.plot(x, y, label='$J_0 (x)$') 
	line, =ax.plot(x, y2,'--', linewidth=2 ,label='$J_1 (x)$') 
	line, =ax.plot(x, y3,'--',linewidth=2, label='$J_2 (x)$') 
	line, =ax.plot(x, y4, '--', linewidth=2 ,label='$J_3 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=4);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize =15, color = '0.20', verticalalignment = 			'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
	
elif opcionMenu=="5":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y, y2, y3, y4 , y5= special.jv(0, x), special.jv(1, x), special.jv(2,x), special.jv(3,x), special.jv(4,x)
	ax.plot(x, y, label='$J_0 (x)$') 
	line, =ax.plot(x, y2,'--', linewidth=2 ,label='$J_1 (x)$') 
	line, =ax.plot(x, y3,'--',linewidth=2, label='$J_2 (x)$') 
	line, =ax.plot(x, y4, '--', linewidth=2 ,label='$J_3 (x)$') 
	line, =ax.plot(x, y5,'--', linewidth=2 , label='$J_4 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=3);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize =15, color = '0.20', verticalalignment = 			'baseline',horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()

elif opcionMenu=="6":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y, y2, y3, y4 , y5, y6= special.jv(0, x), special.jv(1, x), special.jv(2,x), special.jv(3,x),special.jv(4,x),special.jv(5,x)
	ax.plot(x, y, label='$J_0 (x)$') 
	line, =ax.plot(x, y2,'--', linewidth=2 ,label='$J_1 (x)$') 
	line, =ax.plot(x, y3,'--',linewidth=2, label='$J_2 (x)$') 
	line, =ax.plot(x, y4, '--', linewidth=2 ,label='$J_3 (x)$') 
	line, =ax.plot(x, y5,'--', linewidth=2 , label='$J_4 (x)$') 
	line, =ax.plot(x, y6, '--', linewidth=2 ,label='$J_5 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=3);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize =15, color = '0.20', verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()

elif opcionMenu=="7":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y, y2, y3, y4 , y5, y6, y7= special.jv(0, x), special.jv(1, x), special.jv(2,x), special.jv(3,x), special.jv(4,x),special.jv(5,x), special.jv(6,x)
	ax.plot(x, y, label='$J_0 (x)$') 
	line, =ax.plot(x, y2,'--', linewidth=2 ,label='$J_1 (x)$') 
	line, =ax.plot(x, y3,'--',linewidth=2, label='$J_2 (x)$') 
	line, =ax.plot(x, y4, '--', linewidth=2 ,label='$J_3 (x)$') 
	line, =ax.plot(x, y5,'--', linewidth=2 , label='$J_4 (x)$') 
	line, =ax.plot(x, y6, '--', linewidth=2 ,label='$J_5 (x)$') 
	line, =ax.plot(x, y7, '--', linewidth=2 ,label='$J_6 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=4);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20', verticalalignment = 'baseline',horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()

elif opcionMenu=="8":

	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(0, x)
	ax.plot(x, y, label='$J_0 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
       	box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	fancybox=True, shadow=True, ncol=1);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="9":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(1, x)
	ax.plot(x, y, label='$J_1 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=1);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="10":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(2, x)
	ax.plot(x, y, label='$J_2 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=1);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="11":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(3, x)
	ax.plot(x, y, label='$J_3 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=1);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="12":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(4, x)
	ax.plot(x, y, label='$J_4 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=4);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="13":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(5, x)
	ax.plot(x, y, label='$J_5 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=4);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="14":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(6, x)
	ax.plot(x, y, label='$J_6 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=4);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
elif opcionMenu=="15":
	x= np.arange(0, 16, 0.01) 
	fig, ax = plt.subplots()
	y= special.jv(7, x)
	ax.plot(x, y, label='$J_7 (x)$') 
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
        box.width, box.height * 0.9])
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  	fancybox=True, shadow=True, ncol=4);
	plt.grid
	plt.title("First class Bessel's functions.",fontsize = 15, color = '0.20',verticalalignment = 'baseline', horizontalalignment = 'center')
	plt.hlines(0, 0, 16) 
	plt.grid(True)
	plt.show()
else:
	os.system("python InterFun.py ")

