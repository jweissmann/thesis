import numpy as np
import introduction as intro

def absMeanDev(a,b):
	return (1/len(a))*np.sum(abs(a-b))

def meanSquared(a,b):
	return (1/len(a))*np.sum((a-b)**2)

def entropyHistogram(a):
	prbs = np.histogram(a,100)[0]/a.size
	return sum(prbs * np.log(a.size / prbs))

class EntropyLoss(torch.nn.Module):
    def __init__(self):
        super(EntropyLoss, self).__init__()
    
    def forward(self, x, y, bins = 500):
        x = image1
        y = image2
        pX, pY = x.histc(bins), y.histc(bins)
        pX, pY = pX[pX!=float(0)], pY[pY!=float(0)]
        hX = sum(-1.0*pX * torch.log(pX))
        hY = sum(-1.0*pY * torch.log(pY))
        return hX, hY