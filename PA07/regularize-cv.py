import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def main():
    #Importing dataset
    diamonds = pd.read_csv('diamonds.csv')

    #Feature and target matrices
    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]
    y = diamonds[['price']]

    #Normalizing X
    X = normalize(X)

    #Training and testing split, with 25% of the data reserved as the test set
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    #Define the range of lambda to test
    one = 0
    two = 1.5
    three = 11
    first = []
    second = []
    third = []

    while one <= 1:
        first.append(one)
        one = one + 0.1

    while two <= 10:
        second.append(two)
        two = two + 0.5

    while three <= 100:
        third.append(three)
        three = three + 1

    lmbda = first + second + third #fill in

    MODEL = []
    MSE = []
    for l in lmbda:
        #Train the regression model using a regularization parameter of l
        model = train_model(X_train,y_train,l)

        #Evaluate the MSE on the test set
        mse = error(X_test,y_test,model)

        #Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    #Plot the MSE as a function of lmbda
    plt.plot(lmbda,MSE) #fill in
    plt.title('MSE as a function of lmbda')
    plt.xlabel('lmbda values')
    plt.ylabel('Mean-squared-error')
    plt.show()

    #Find best value of lmbda in terms of MSE
    ind = MSE.index(min(MSE))#fill in
    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]
    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))

    X_test = [0.25,60,55,4,3,2,5,3,3]
    X_test = normalize(X_test)
    coeffs = model_best.coef_[0]
    intercept =model_best.intercept_[0]

    predictedvalue = 0
    for i in range (len(X_test)):
        predictedvalue = predictedvalue + X_test[len(X_test)-i-1]*coeffs[i]
    predictedvalue = predictedvalue + intercept
    print("The predicted y value is: " + str(predictedvalue))
    return model_best


#Function that normalizes features to zero mean and unit variance.
#Input: Feature matrix X.
#Output: X, the normalized version of the feature matrix.
def normalize(X):

    #fill in
    mean = []
    std = []
    mean = np.mean(X,axis = 0)
    std = np.std(X,axis = 0)
    X = (X - mean) / std
    return X

#Function that trains a ridge regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model.
def train_model(X,y,l):

    #fill in
    model = linear_model.Ridge(alpha = l, fit_intercept = True)
    model.fit(X,y)
    return model


#Function that calculates the mean squared error of the model on the input dataset.
#Input: Feature matrix X, target variable vector y, numpy model object
#Output: mse, the mean squared error
def error(X,y,model):

    #Fill in
    ypredict = model.predict(X)
    mse = mean_squared_error(y,ypredict)
    return mse

#including for testing purposes, basically to run it.
if __name__ == '__main__':
    main()
