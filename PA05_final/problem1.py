
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import math as m

#Importing file to read
eng0File = open('eng0.txt')
eng0data = eng0File.readlines()
eng0File.close()

eng1File = open('eng1.txt')
eng1data = eng1File.readlines()
eng1File.close()

eng1data = [float(x) for x in eng1data]                   #convert the string to a float
eng0data = [float(x) for x in eng0data]                   #convert the string to a float

#Suppose the instructor of the course is convinced that the mean engagement of students who become knowledgeable
#in the material (i.e., the eng1 population) is 0.75. Formulate null and alternative hypotheses for a statistical
#test that seeks to challenge this belief. What type of test can be used?

print('Null hypothesis : H0: mean of the student who became knowledgeable is equal to 0.75')
print('Alternative hypothesis : H1: mean of the students who become knowledgeable is not equal to 0.75')
print(' ')

#Carry out this statistical test using the eng1 sample. Report the sample size, the sample mean, the standard error,
#the standard score, and the p-value. Are the results significant at a level of 0.1? How about 0.05? How about 0.01?
#What (if anything) can we conclude?
eng1size = np.size(eng1data)                                  #Size
eng1avg = np.mean(eng1data)                          #Average
eng1sd = np.std(eng1data, ddof=1)                        #Standard Deviation
eng1se = (eng1sd / (np.sqrt(eng1size)))                    #Standard Error
z_c = (eng1avg - 0.75) / eng1se
p_value = 2 * norm.cdf(-abs(z_c))

print('The sample size is : {}'.format(eng1size))
print('The sample mean is: {}'.format(eng1avg))
print('The sample standard of deviation  is : {} '.format(eng1sd))
print('The standard error is: {} '.format(eng1se))
print('The standard score is: {} '.format(z_c))
print('The standard p-value is: {} '.format(p_value))

if (p_value <= 0.1):
    print('The sample is significant as 10% level of significance, we fail to reject H0')
elif(p_value <= 0.05):
    print('The sample is significant as 5% level of significance, we fail to reject H0.')
elif(p_value <= 0.01):
    print('The sample is significant as 1% level of significance, we fail to reject H0.')
else:
    print('We reject the null hypothesis.')
print(' ')
#Determine the largest standard of error for which the test will be significant at a level of 0.05.
#What is the corresponding minimum sample size?
p_value_new = 0.05
z_c_new = norm.ppf(p_value_new / 2)
SE_new = (eng1avg - 0.75) / z_c_new                      #Largest standard error
samplesize = (eng1sd / SE_new)                           #Sample size
size = m.ceil(samplesize **2)

print('The largest standard of error is: {} '.format(SE_new))
print('The corresponding minimum sample size is: {} '.format(size))
print(' ')


#Suppose the instructor is also convinced that the mean engagement is different between students who become knowledgeable
#(the eng1 population) and those who do not (the eng0 population). Formulate null and alternative hypotheses that seek
#to validate this belief. What type of test can be used ?

print('H0: the mean engagement is different between students who become knowledgeable and those who do not is equal')
print('H1: the mean engagement is different between students who become knowledgeable and those who do not is not equal')
print(' ')

#Carry out this statistical test using the eng0 and eng1 samples.
#Report the sample sizes, the sample means, the standard error, the z-score, and the p-value.
#Are the results significant? What (if anything) can we conclude?
eng1avg = np.mean(eng1data)
eng0avg = np.mean(eng0data)
netavg = (eng1avg - eng0avg)

eng1sd = np.std(eng1data, ddof=1)
eng0sd = np.std(eng0data, ddof=1)

eng1var = (eng1sd ** 2)
eng1size = (np.size(eng1data))
eng1div = ((eng1var) / eng1size)

eng0var = (eng0sd ** 2)
eng0size = (np.size(eng0data))
eng0div = ((eng0var) / eng0size)

sum = eng0div + eng1div
final = (np.sqrt(sum))

z_c = (netavg / final)
p = 2 * norm.cdf(-abs(z_c))

print('We reject the null hypothesis due to such a small value which approximates so close to zero.')
print('The sample mean for eng1data is : {}'.format(eng1avg))
print('The sample mean for eng0data is : {}'.format(eng0avg))
print('The sample mean is: {} '.format(netavg))
print('The standard error is: {} '.format(final))
print('The z-score value is: {} '.format(-abs(z_c)))
print('The p-value is: {} '.format(p))
