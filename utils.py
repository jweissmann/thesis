import numpy as np
import torch


def normalize(i):
	m = i.min()
	if m <= 0: return (i + abs(m))/(i + abs(m)).max() 
	return (i - abs(m))/(i + abs(m)).max() 


def loadData():
	outputfile1 = '../data/all_data/KBCT010028_noncontrast.npy'
	outputfile2 = '../data/all_data/KBCT010028_contrast.npy'
	nc010028 = np.load(outputfile1)
	nc010028 = [normalize(i) for i in nc010028]
	c010028 = np.load(outputfile2)
	c010028 = [normalize(i) for i in c010028]
	return nc010028, c010028


################################################
#### BACKGROUND REMOVAL FUNCTIONS ##############
def extractPixels(ind, dataPixels):
    rows, cols = ind
    return dataPixels[rows[0]:rows[1],cols[0]:cols[1]]

def removeBackgroundIndices(pixelArray, N = 10):
	# returns a start and stop for both cols and rows to remove the background
    # N is a smoothing parameter
    colSum = np.sum(pixelArray,axis=0)
    # https://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    colSum = np.convolve(colSum, np.ones((N,))/N, mode='valid')
    idx = np.argmax(colSum) # remember to add the max back to the second index
    cols = [np.argmin(colSum[:idx]), np.argmin(colSum[idx:])+idx]  
    rowSum = np.sum(pixelArray,axis=1)
    rowSum = np.convolve(rowSum, np.ones((N,))/N, mode='valid')
    idx = np.argmax(rowSum)
    rows = [np.argmin(rowSum[:idx]), np.argmin(rowSum[idx:])+idx]    
    return [rows, cols]


def removeBackground(image1, image2):
	inds = removeBackgroundIndices(image1)
	preC = extractPixels(inds,image1)
	postC = extractPixels(inds, image2)
	return preC, postC
##############################################

# Class for each image in he dataset

























