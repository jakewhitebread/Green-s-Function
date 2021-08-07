#Jake Whitebread
#CST-305
#Dr. Citro
#Green's Function

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import time

#Plotting Handwritten Solution for Equation 1
x1 = []     #making arrays to store x values
y1 = []     #making arrays to store y values
for x in range(1,50):
    for y in range(1,1000):
        #General Solution to the first DE
        eq1 = -(((3 * math.exp(-2*x)) + (2 * (x^2)) - (6*x) + 3) / 4)
        x1.append(x)
        y1.append(eq1)
plt.title("DE 1 Hand Solution")
plt.xlabel("time(t)")
plt.ylabel("y")
plt.plot(x1,y1)
plt.show()

#Plotting Handwritten Solution for Equation 2
x2 = []     #array to store x values
y2 = []     #array to store y values
for x in range(1,50):
    for y in range(1,1000):
        eq2 = 4 - (4*math.cos(x))       #General Solution for DE 2
        x2.append(x)
        y2.append(eq2)
plt.title("DE 2 Hand Solution")
plt.xlabel("time(t)")
plt.ylabel("y")
plt.plot(x2,y2)
plt.show()
