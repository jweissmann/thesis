import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw 

def extractPixels(ind, dataPixels):
    rows, cols = ind
    return dataPixels[rows[0]:rows[1],cols[0]:cols[1]]

def removeBackground(pixelArray, N = 10):
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

def removeBackgroundTest(contrast = 1):
	row = 0
	col = 0
	for m in range(349):
	    idx = removeBackground(data[contrast][m])
	    row += idx[0][1] - idx[0][0]
	    col += idx[1][1] - idx[1][0]
	return row/350, col/350

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


def showInverse(a):
	plt.imshow(1/a, cmap = plt.cm.bone)
	plt.show()
	return()

def enhanceContrast(a, alpha):
	# # enhance the contrast of the image
	# # alpha=1.0 is the original, max is 2.0, min is 0.0
	im = Image.fromarray(a * 255).convert('L') # convert to black and white mode
	contrast = ImageEnhance.Contrast(im)
	contrast.enhance(alpha).show()
	return


def main():
	data = loadData()
	s = np.sum(data[1][250],axis=0)-np.sum(data[0][240],axis=0)
	s = np.sum(data[1][250],axis=0)-np.sum(data[1][240],axis=0)
	plt.plot(s)
	plt.title('RowSum difference 250 contrast with 240 contrast')
	plt.show()


# main()

