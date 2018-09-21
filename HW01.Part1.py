Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#Programmer: Brittian Foster

from __future__ import division
from numpy import *
from scipy import *
from math import *
from pylab import *
import matplotlib.pyplot as plt
import random

#Making a Plot of 10 Random Points 
#list and constants
t = 0
x_list = []
y_list = []

while t < 10:
    t = t + 1
    x = random.random()
    y = random.random()
    x_list.append(x)
    y_list.append(y)
print(x_list)

#plotting
figure()
plt.scatter(x_list, y_list)
show()
