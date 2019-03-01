import numpy as np
# import cvxpy as cvx
# import matplotlib.pyplot as plt
import introduction
import utils

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

	# # brute force for loops
	# ax = np.zeros([data2.shape[0]-blob.shape[0], data2.shape[1] - blob.shape[1]])
	# for i in range(data2.shape[0] - blob.shape[0]):
	# 	for j in range(data2.shape[1] - blob.shape[1]):
	# 		diff = loss(data2[i:(i+blob.shape[0]),j:(j+blob.shape[1])], blob)
	# 		ax[i,j] = diff

	return results
	
def findRotation(x,y):
# 	# x, y should have the same shape
# 	# optimal rotation matrix can be found explicitly
# 	xM, yM = sum(x) / len(x), sum(y) / len(y)
# 	d = len(x[0])
# 	# singular value decomposition of M = sum((x-xM) * (y-yM).T)
# 	M = sum([np.matmul((x-xM)[i].reshape(d,1) , (y-yM)[i].reshape(1,d)) for i in range(len(x))])
# 	USV = np.linalg.svd(M) 
# 	optimal =  np.matmul(USV[2].T, USV[0].T) # optimal solution: V * U.T

# 	indexVec = np.zeros(d)
# 	indexVec[-1] = 1

# 	R = cvx.Variable(d,d)
# 	constraints = []
# 	# constraints = [R[-1,:] == indexVec.reshape(1,d),R[:,-1] == indexVec.reshape(d,1)]
# 	objective = cvx.Minimize(cvx.sum_squares(y - x * R))
# 	problem = cvx.Problem(objective, constraints)
# 	print(problem.solve())
# 	print(R.value)
# 	print(optimal)
# 	return np.matrix(R.value), optimal
	return	


def singleTensor(index, pixelArray, n):
	# index is a [x,y] coordinate
	# n is a vecetor [nx, ny] containing the dimensions of the meshgrid

	d = len(index) # the dimensionality 
	B0 = lambda t: (1/6)*(1-t)**3
	B1 = lambda t: (1/6)*(3*t**3-6*t**2+4)
	B2 = lambda t: (1/6)*(-3*t**3 + 3*t**2 + 3*t + 1)
	B3 = lambda t: (1/6)*(t)**3
	B = [B0,B1,B2,B3]
	
	# newIndices are transformed indices from x,y,z to i,j,k
	newIndices = [int(np.floor(index[i]/n[i])-1) for i in range(d)]
	# inputs to the B-spline equations
	splines = [index[i]/n[i] - np.floor(index[i]/n[i]) for i in range(d)]

	tensor = 0
	e = len(B) # how many equations there are
	for a in range(e):
		for b in range(e):
			i,j = newIndices
			u,v = splines
			tensor += B[a](u)*B[b](v)*pixelArray[i+a,j+b]

	return tensor

def transform(image1, image2, n):
	# n refers to nx or ny (in a square mesh) -- the length/width of the meshgrid
    preC, postC = utils.removeBackground(image1, image2)
	#trans = np.zeros_like(preC)
    trans = [[singleTensor([i,j],preC,n) for i in range(preC.shape[0])] for j in range(preC.shape[1])]
    return np.matrix(trans)
   


def main():
	x = np.random.rand(5,3)
	y = np.random.rand(5,3)
	# plt.scatter(x[:,0], x[:,1], color = 'red')
	# plt.scatter(y[:,0], y[:,1], color = 'blue')
	# plt.show()
	x[:,-1] = 1
	y[:,-1] = 1
	findRotation(x,y)
	return

# main()