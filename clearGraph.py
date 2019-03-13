#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
import random

#create a figure instance that will later be written to a PDF
f = plt.figure()

x = []
y = []

#open file
fopen  = open("percapitaPop.txt")

num = 0
for each in fopen:
    fields = each.split("|")
    if float(fields[1].strip('\n')) < 40000:
        x.append(float(fields[1].strip('\n')))
        y.append(float(fields[0]))
        num +=1
    
# Make a list of of random colors
colors = [random.random() for i in range(num)]    
# Make a list of same sized circles
areas = [1 for i in range(num)]

# Do the scatter plot, with specified colors and sizes
plt.scatter(x, y, c = colors, s = areas, alpha = 0.5)

# Specify the x and y axis labels
plt.xlabel("Population of a zipcode (age 65+)")
plt.ylabel("The percapita of antidepressants of a zipCode")

plt.show()
#Save the plot into a PDF file
f.savefig("clearGraph.pdf")
