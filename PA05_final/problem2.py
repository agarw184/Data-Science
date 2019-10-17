import numpy as np
from scipy.stats import norm
from scipy.stats import t


data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

#Use the sample to construct a 95% confidence interval for the number of points by which the team wins on average.
#Report the sample mean, the standard error, the standard statistic, and the interval.
pointsize = len(data)
pointavg = np.mean(data)
pointsd =  np.std(data, ddof = 1)
confidence = 0.95
pointerror = pointsd / (pointsize ** 0.5)
pvalue = (1 - ((1-confidence) / 2))
t_c = t.ppf(pvalue,pointsize-1)
C_L = pointavg - ((t_c * pointsd) / (pointsize ** 0.5))
C_U = pointavg + ((t_c * pointsd) / (pointsize ** 0.5))
confidenceinterval = (C_L,C_U)

print(' ')
print('The sample mean is: {}'.format(pointavg))
print('The standard error is: {} '.format(pointerror))
print('The standard statistic is: {} '.format(t_c))
print('The interval is: {} '.format(confidenceinterval))

#Repeat part 1 for a 90% confidence interval. Compare your results.
pointavg = np.mean(data)
pointsd =  np.std(data, ddof = 1)
confidence = 0.90
pointerror = pointsd / (pointsize ** 0.5)
pvalue = (1 - ((1-confidence) / 2))
t_c = t.ppf(pvalue,pointsize-1)
C_L = pointavg - ((t_c * pointsd) / (pointsize ** 0.5))
C_U = pointavg + ((t_c * pointsd) / (pointsize ** 0.5))
confidenceinterval = (C_L,C_U)

print(' ')
print('The sample mean is: {} '.format(pointavg))
print('The point error is: {} '.format(pointerror))
print('The standard statistic is: {} '.format(t_c))
print('The interval is: {}'.format(confidenceinterval))
print('The t_c has a relatively lower value which makes the interval precise as our confidence level decreases.'
'As t value decreases, the lower bound of our confidence level increase and upper bound decreases')


#Repeat part 1 if you are told that the population standard deviation is 16.836. Compare your results.
pointavg = np.mean(data)
pointsd = 16.836
confidence = 0.95
pointerror = pointsd / (pointsize ** 0.5)
pvalue = (1 - ((1-confidence) / 2))
z_c =norm.ppf(pvalue)
C_L = pointavg - ((z_c * pointsd) / (pointsize ** 0.5))
C_U = pointavg + ((z_c * pointsd) / (pointsize ** 0.5))
confidenceinterval = (C_L,C_U)

print(' ')
print('The interval is: {}'.format(confidenceinterval))
print('The sample mean is: {} '.format(pointavg))
print('The point error is: {} '.format(pointerror))
print('The standard statistic is: {} '.format(z_c))
print('The p value is: {}'. format(pvalue))
print('The results are similar because the standard deviation in both the cases, that is, part 2.1 and 2.3 are the same.')

#With what level of confidence can we say that the team is expected to win on average?
#(Hint: The interval must be strictly positive.)
pointsize = len(data)
pointavg = np.mean(data)
pointsd =  np.std(data, ddof = 1)
pointerror = pointsd / (pointsize ** 0.5)
pointz_new = (pointavg) / pointerror
pvalue = norm.cdf(pointz_new)
C = 2 * pvalue - 1

C_L_new = pointavg - ((pointz_new * pointerror))
C_U_new= pointavg + ((pointz_new * pointerror))
confidenceinterval = (C_L_new,C_U_new)
print(' ')
print('The mean is {}'. format(pointavg))
print('The level of confidence is {}'.format(C*100))
print('The interval is {}'.format(confidenceinterval))
