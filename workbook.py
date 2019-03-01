# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:31:13 2019

@author: Josh Weissmann
"""
import numpy as np
import matplotlib.pyplot as plt
#data = loadData()
N = len(data[0])
#rowSums = [np.sum(data[1][i] - data[0][i], 0) for i in range(N)]
#colSums = [np.sum(data[1][i] - data[0][i], 1) for i in range(N)]

#rowMaxIndxs = [rowSums[i].argmax() for i in range(N)]
#colMaxIndxs = [colSums[i].argmax() for i in range(N)]

#plt.imshow(data[1][150])
#plt.scatter(rowMaxIndxs[150],colMaxIndxs[150])


##### ROTATION DEFORMATION #####
t = np.pi / 4
R = np.array([[np.cos(t), -np.sin(t), 0],[np.sin(t), np.cos(t), 0],[0, 0, 1]])
x = np.random.rand(1000,3)
x[:,2] = 1
rotate = lambda x: np.matmul(R, x)
y = (rotate(x.T)).T
plt.scatter(x.T[0], x.T[1], color = 'red')
plt.scatter(y.T[0], y.T[1], color = 'blue')


xM, yM = sum(x) / len(x), sum(y) / len(y)

M = sum([np.matmul((x-xM)[i].reshape(3,1) , (y-yM)[i].reshape(1,3)) for i in range(len(x))])
USV = np.linalg.svd(M)
np.matmul(USV[2].T, USV[0].T)

(y - np.matmul(x, R))