def controlPoints(*args):
	# needs to take into account the third dimension by creating actual 3D object
	global data
	return extractBackground(removeBackground(data[0][250]),data[0][250])[args]


def transformBSpline(data, )
	# data should be a set of 2D slices stacked together
	B0 = lambda t: (1/6)*(1-t)**3
	B1 = lambda t: (1/6)*(3*t**3-6*t**2+4)
	B2 = lambda t: (1/6)*(-3*t**3 + 3*t**2 + 3*t + 1)
	B3 = lambda t: (1/6)*(t)**3
	B = [B0,B1,B2,B3]


def T(x,y,z, meshDims):
    nx,ny,nz = meshDims[0],meshDims[1],meshDims[2]
    i = int(np.floor(x/nx)-1)
    j = int(np.floor(y/ny)-1)
    k = int(np.floor(z/nz)-1)
    intensity = lambda i,j,k: controlPoints(i,j)
    
    u = x/nx - np.floor(x/nx)
    v = y/ny - np.floor(y/ny)
    w = z/nz - np.floor(z/nz)
    
    s = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                s += B[a](u)*B[b](v)*B[c](w)*intensity(i+a,j+b,k+c)
    
    return s



class Blob3D:
	def __init__(self, i, N, pixelArraySlices):
		# pass the entire set of slices as pixelArraySlices
		# i is the central slice for which the Blob3D object is created
		# N is the number of slices on each side of the center
		self.data = pixelArraySlices[(i-N):(i+N)]
		self.i = i
		self.N = N

	def controlPoints(self):
		CPs = [controlPoints(i) for i in self.data]
		return CPs