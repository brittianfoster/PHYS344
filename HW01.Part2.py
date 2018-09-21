#Programmer: Brittian Foster

from __future__ import division
from numpy import *
from scipy import *
from math import *
from pylab import *
import matplotlib.pyplot as plt
import random

#Modeling the Output of a Stern Gerlach Generator
#constants
N = 1e6
i = 0
#lists
p_list = []
diff_list = []
p=random.randint(0,1)

# 1 represents +1/2 spin
# 0 represents -1/2 spin
while i < N:
    i = i + 100
    p = random.randint(0,1)
    p_list.append(p)
    p1 = p_list.count(1)
    p0 = p_list.count(0)
    diff = abs(p1 - p0)
    diff_list.append(diff)

#Graphing
x = linspace(0, 1e6, 10000)
figure()
plot(x, diff_list)
show()
