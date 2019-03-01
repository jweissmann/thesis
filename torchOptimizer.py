# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:39:50 2019

@author: Josh Weissmann
"""

import numpy as np
# import cvxpy as cvx
# import matplotlib.pyplot as plt
import introduction
import utils
import torch

absMeanDev = lambda a,b: (1/len(a))*np.sum(abs(a-b))

def optimize(loss, d1, d2, blob):
	# loss should be a function
	# blob is the blob we are looking for in the data
	# coords are coordinates of the object in question

	# vectorize the process
	cutNSubtract = lambda data,i,j,blob: absMeanDev(data[(i):(i+blob.shape[0]),(j):(j+blob.shape[1])],blob)
	h = d1.shape[0] - blob.shape[0]
	w = d1.shape[1] - blob.shape[1]
	results = [[cutNSubtract(d2,i,j,blob) for j in range(w)] for i in range(h)]

	return results
	

def singleTensor(index, pixelArray, n):
	# index is a [x,y] coordinate, should be a Torch vector
	# n is a vecetor [nx, ny] containing the dimensions of the meshgrid, should be a torch vector

    d = len(index) # the dimensionality 
    B0 = lambda t: (1/6)*(1-t)**3
    B1 = lambda t: (1/6)*(3*t**3-6*t**2+4)
    B2 = lambda t: (1/6)*(-3*t**3 + 3*t**2 + 3*t + 1)
    B3 = lambda t: (1/6)*(t)**3
    B = [B0,B1,B2,B3]
	
	# newIndices are transformed indices from x,y,z to i,j,k
    newIndices = [int(torch.floor(torch.Tensor([index[i]/n[i]-1]))) for i in range(d)]
    
	# inputs to the B-spline equations
    splines = [index[i]/n[i] - torch.floor(torch.Tensor([index[i]/n[i]])) for i in range(d)]

    i,j = newIndices
    u,v = splines

    tensor = torch.randn(1, re)
    e = len(B) # how many equations there are
    for a in range(e):
    	for b in range(e):
    		tensor += B[a](u)*B[b](v)*pixelArray[:,:,i+a,j+b]
    
    return tensor

def transform(image1, image2, n):
    # inputs image1 and image2 can be arrays or lists, do not need to be torch Tensors
	# n refers to nx or ny (in a square mesh) -- the length/width of the meshgrid
    preC, postC = utils.removeBackground(image1, image2)
    shape = preC.shape
    preC, postC = preC.reshape([1,1,shape[0],shape[1]]), postC.reshape([1,1,shape[0],shape[1]])
    preC, postC = torch.Tensor(preC), torch.Tensor(postC)
    
	#trans = np.zeros_like(preC)
    trans = [[singleTensor(torch.Tensor([i,j]),preC,n) for i in range(shape[0])] for j in range(shape[1])]
    return (trans)
   



def main():

	return

# main()