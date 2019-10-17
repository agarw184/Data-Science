
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from helper import *

#For data set A
data = getData('distA.csv')
plt.hist(data,rwidth = 0.85)
plt.title('Histogram')

stats.probplot(data, dist ='norm', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Gaussian.png')

stats.probplot(data, dist ='cauchy', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Cauchy.png')

stats.probplot(data, dist ='cosine', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Cosine.png')

stats.probplot(data, dist ='expon', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Exponential.png')

stats.probplot(data, dist ='uniform', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Uniform.png')

stats.probplot(data, dist ='laplace', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Laplace.png')

stats.probplot(data, dist ='wald', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Wald.png')

stats.probplot(data, dist ='rayleigh', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distA-Rayleigh.png')

##For datasetB
data = getData('distB.csv')
plt.hist(data,rwidth = 0.85 )
plt.title('Histogram')

stats.probplot(data, dist ='norm', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Gaussian.png')

stats.probplot(data, dist ='cauchy', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Cauchy.png')

stats.probplot(data, dist ='cosine', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Cosine.png')

stats.probplot(data, dist ='expon', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Exponential.png')

stats.probplot(data, dist ='uniform', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Uniform.png')

stats.probplot(data, dist ='laplace', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Laplace.png')

stats.probplot(data, dist ='wald', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Wald.png')

stats.probplot(data, dist ='rayleigh', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distB-Rayleigh.png')

##For datasetC
data = getData('distC.csv')
plt.hist(data,rwidth = 0.85 )
plt.title('Histogram')

stats.probplot(data, dist ='norm', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Gaussian.png')

stats.probplot(data, dist ='cauchy', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Cauchy.png')

stats.probplot(data, dist ='cosine', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Cosine.png')

stats.probplot(data, dist ='expon', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Exponential.png')

stats.probplot(data, dist ='uniform', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Uniform.png')

stats.probplot(data, dist ='laplace', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Laplace.png')

stats.probplot(data, dist ='wald', plot=plt)
plt.title('Wald')
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Wald.png')

stats.probplot(data, dist ='rayleigh', plot=plt)
plt.show() # modify this to write the plot to a file instead
plt.savefig('distC-Rayleigh.png')
