import os
import sys
from scipy import special
import numpy as np
import matplotlib.pyplot as plt
import math

e=int(sys.argv[2])#constante medio
r=int(sys.argv[3])#constante rigidez
m=int(sys.argv[4])#masa
d=int(sys.argv[5])#Tipo de grafica

b=e/(2*m)
a=(r/m)**(1/2)
m1=-b+(b**2-a**2)**(1/2)
m2=-b-(b**2-a**2)**(1/2)

x= np.arange(0, 4*np.pi, 0.01)

fig, ax = plt.subplots() 

y1=(math.e)**(m1*x) + (math.e)**(m2*x)
y2=(math.e)**(-a*x) + (math.e)**(-a*x)
y3=(math.e)**(-b*x)*(np.cos((b**2-a**2)**(1/2))+np.sin((b**2-a**2)**(1/2)))
y4=np.cos(a*x)+np.sin(a*x)

if d == 0:
	ax.plot(x, y4,'--',linewidth=2,label='Simple harmonic oscllator.')
	
elif d == 1:
	ax.plot(x, y2, '--',linewidth=2, label='Overdamping harmonic oscillators.') 
	
elif d == 2:
	ax.plot(x, y1,'--',linewidth=2, label='Damped harmonic oscillator.') 
	
elif d == 3:
	ax.plot(x, y3, '--',linewidth=2,label='Underdamping harmonic oscillators.') 
	
else:
	ax.plot(x, y4,'--',linewidth=2,label='Simple harmonic oscllator.')
	ax.plot(x, y1, '--',linewidth=2, label='Overdamping harmonic oscillators.') 
	ax.plot(x, y2,'--',linewidth=2, label='Damped harmonic oscillator.') 
	ax.plot(x, y3, '--',linewidth=2,label='Underdamping harmonic oscillators.') 
	 
plt.legend(loc='upper right')

plt.title("Harmonic Oscillator.",fontsize = 15, color = '0.20', verticalalignment = 'baseline', horizontalalignment = 'center')
plt.hlines(0, -2, 10)
plt.xlim(0, 10)
plt.ylim(-2, 4)
plt.grid(True)
plt.show()
