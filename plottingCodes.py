# image generation

def 21():
	m = 151
	plt.plot(np.sum(data[1][m],0)[600:700], label='post-contrast')
	plt.plot(np.sum(data[0][m],0)[600:700],label='pre-contrast')
	plt.legend()
	plt.title('Row Sums Difference, Slice 150\nRows 600:700')
	plt.savefig('../Plots/21.png')

