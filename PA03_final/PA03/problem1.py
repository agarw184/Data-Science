import numpy as np
import matplotlib.pyplot as plt
from helper import *
#from homework2 import histogram

data = np.loadtxt('inp.txt')

def histogram(data,n,l,h):
    hist = []  
    if (n > 0 and h >= l):       
        w = ((h-l)/n)
        hist = n*[0]
        for i in range(n):
            for counter in range(len(data)):
                    if (data[counter] < l or data[counter] > h):
                        continue  
                    else:
                        if(data[counter] >= (l+(i*w)) and data[counter] < (l+(i+1)*w)):
                            hist[i] = hist[i] + 1
                            
                        elif(data[counter] == h):
                            if (i == n-1):
                                hist[n-1] = hist[n-1] + 1
    else:
        print("Error")
        return hist
    return hist

#change a histogram of counts into a histogram of probabilities
#input: a histogram (like your histogram function creates)
#output: a normalized histogram with probabilities instead of counts
def norm_histogram(hist) :
    #fill in
    #hint: when doing your normalization, you should convert the integers
    #      in your histogram buckets to floats: float(x)
    sumhist = 0.0                           #Variable to hold the frequency 
    norm_hist = [0]*len(hist)
    for j in range(len(hist)):
        hist[j] = float(hist[j])           #Converts into float
        sumhist = sumhist + hist[j]        #Total ferquency
        
    for i in range(len(hist)):
        norm_hist[i] = (hist[i] / sumhist)
    return norm_hist
    
#compute cross validation for one bin width
#input: a (non-normalized) histogram and a bin width
#output: the cross validation score (J) for the specified width
def crossValid (histo, width) :
    #1. build the list of probabilities
    probabilities = norm_histogram(histo)
    #2. compute the sum of the squares of the probabilities
    probsquare = 0.0        #Keeping the floats
    for j in range(len(probabilities)):
        probsquare = probsquare + (probabilities[j]*probabilities[j])
    #3. determine the total number of points in the histogram
    #   hint: look up the Python "sum" function 
    #4. Compute J(h) and return it
    n = sum(histo)
    J = (2 / ((n-1)* width)) - (((n+1)/((n-1) * width)) * probsquare)
    return J
    
#sweep through the range [min_bins, max_bins], compute the cross validation
#score for each number of bins, and return a list of all the Js
#Note that the range is inclusive on both sides!
#input: the dataset to build a histogram from
#       the minimum value in the data set
#       the maximum value in the data set
#       the smallest number of bins to test
#       the largest number of bins to test
#output: a list (of length max_bins - min_bins + 1) of all the appropriate js
def sweepCross (data, minimum, maximum, min_bins, max_bins) :
    #fill in. Don't forget to convert from a number of bins to a width!
    js = [0]*(max_bins-min_bins+1)
    i = 1
    for i in range(min_bins,max_bins+1):
        w = ((maximum - minimum) / i)   #Width 
        histo = histogram(data,i,minimum,maximum)
        js[i-1] = crossValid(histo,w)        #Calling crossvalid
    return js
        
#return the minimum value in a list *and* the index of that value
#input: a list of numbers
#output: a tuple with the first element being the minimum value, and the second 
#        element being the index of that minumum value (if the minimum value is 
#        in the list more than once, the index should be the *first* occurence 
#         of that minimum value)
def findMin (l) :
    minVal = min(l)
    minIndex = l.index(min(l)) 
    return (minVal, minIndex)
        
if __name__ == '__main__' :
        #Sample test code
        data = getData() #reads data from inp.txt
        lo = min(data)
        hi = max(data)
        js = sweepCross(data, lo, hi, 1, 100)
        print(findMin(js))