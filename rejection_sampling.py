# Rejection Sampling Script
# Lucas Cusimano
# 11/5/2017

import numpy as np
import matplotlib.pyplot as plt

#This is our sampling from the uniform distribution
s = np.random.uniform(0,1,100000)

#We will reject some of the draws from "s" to create the "new_dist" -- the new distribution
new_dist =  []

#We loop through our initial draws
for i in s:
    #We draw a probability to know whether to reject this draw or not
    test = np.random.uniform(0,1)
    #With probability 1 - i we keep this sample, otherwise we reject it (don't add it)
    #Change "if" statement to get more complicated rejection criteria
    if (test > i):
        # Add the draw to our new distribution
        new_dist.append(i)

#Create a cool representation of the PDF
plt.hist(new_dist, 30, normed=True)
plt.show()
