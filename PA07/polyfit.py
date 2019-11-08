import numpy as np
import math as m
import matplotlib.pyplot as plt

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of n = degrees[i].
def main(datapath, degrees):
    paramFits = []
    #fill in
    x = []
    y = []
    y_pred = []
    #read the input file, assuming it has two columns, where each row is of the form [x y] as
    #in problem1.txt.
    data = np.loadtxt(datapath)
    for i in range(len(data)):
        x.append(float(data[i][0]))
        y.append(float(data[i][1]))
    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.
    for i in range (len(degrees)):
        newB = (least_squares(feature_matrix(x,degrees[i]),y))
        paramFits.append(newB)
        #For plotting
        X = np.array(feature_matrix(x,degrees[i]))
        y_pred_value_list = np.dot(X,np.array(newB))
        y_pred_value_list.sort()
        y_pred.append(y_pred_value_list)
    x.sort()
    y.sort()
    plt.scatter(x,y,label='Data Set',color="black")
    plt.plot(x,y_pred[0],label ='Degree 1')
    plt.plot(x,y_pred[1],label ='Degree 2')
    plt.plot(x,y_pred[2],label ='Degree 3')
    plt.plot(x,y_pred[3],label ='Degree 4')
    plt.plot(x,y_pred[4],label ='Degree 5')

    plt.xlabel('degree values')
    plt.ylabel('paramFits (coefficients) unit')
    plt.title('Estimated paramFits values')
    plt.legend()
    plt.show()


    #Question 4
    netval = 0
    currenthighestdegree = 5
    for i in paramFits[4]:
        netval = netval + i* 2**currenthighestdegree
        currenthighestdegree = currenthighestdegree - 1
    print("The estimated y_pred value at x = 2 is " + str(netval) + "\n" )
    return paramFits


#Return the feature matrix for fitting a polynomial of degree n based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and n as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by n+1.
def feature_matrix(x, n):

    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^n, x^(n-1), ..., x^0.
    X = []
    for i in range (len(x)):
        temp = []
        for k in range (n , -1 , -1):
            temp.append(x[i] ** k)
        X.append(temp)
    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    #fill in
    B = []
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    Btemp = np.dot(np.linalg.inv(np.dot(np.transpose(X),X)),np.transpose(X))
    for i in range (len(Btemp)):
       B.append(np.dot(Btemp[i],y))
    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [1,2,3,4,5]

    paramFits = main(datapath, degrees)
    print(paramFits)
