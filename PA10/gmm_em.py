import numpy as np
from scipy.stats import norm

#function which carries out the expectation step of expectation-maximization
def expectation(data, weights, means, varis):
    k = len(means)
    N = len(data)
    gammas = np.zeros((k,N))
    valnum = 0
    valden = 0
    #fill in here
    #code to calculate each gamma = gammas[i][j], the likelihood of datapoint j in gaussian i, from the
    #current weights, means, and varis of the gaussians

    for i in range (N):
        valden = 0
        for j in range (k):
            valden += (weights[j] * (norm(means[j],np.sqrt(varis[j])).pdf(data[i])))

        for j in range (k):
            valnum = (weights[j] * (norm(means[j],np.sqrt(varis[j])).pdf(data[i])))
            gammas[j][i] = valnum / valden
    return gammas


#function which carries out the maximization step of expectation-maximization
def maximization(data, gammas):
    k = len(gammas)
    N = len(data)
    weights = np.zeros(k)
    means = np.zeros(k)
    varis = np.zeros(k)
    Nofgaussian = 0
    #fill in here
    #code to calculate each (i) weight = weights[i], the weight of gaussian i, (ii) mean = means[i], the
    #mean of gaussian i, and (iii) var = varis[i], the variance of gaussian i, from the current gammas of the
    #datapoints and gaussians
    for i in range (k):
        for j in range (N):
            Nofgaussian = sum(gammas[i])
            weights[i] = Nofgaussian / N
            means[i] = sum(gammas[i] * data) / Nofgaussian
            varis[i] = sum(gammas[i] * ((data-means[i])**2)) / Nofgaussian
    return weights, means, varis


#function which trains a GMM with k clusters until expectation-maximization returns a change in log-likelihood of less
#than a tolerance tol
def train(data, k, tol):
    # fill in
    # initializations of gaussian weights, means, and variances according to the specifications
    means =np.zeros(k)
    weights = np.zeros(k)
    varis =np.zeros(k)

    x_0 = np.min(data)
    x_n = np.max(data)

    for i in range (k):
        means[i] = (x_0 + i * (x_n - x_0) / k)
        weights[i] = 1 / k
        varis[i] = 1

    diff = float("inf")
    ll_prev = -float("inf")

    # iterate through expectation and maximization procedures until model convergence
    while(diff >= tol):
        gammas = expectation(data, weights, means, varis)
        weights, means, varis = maximization(data, gammas)
        ll = log_likelihood(data,weights,means,varis)
        diff = abs(ll - ll_prev)
        ll_prev = ll
    return weights, means, varis, ll


#calculate the log likelihood of the current dataset with respect to the current model
def log_likelihood(data, weights, means, varis):
    #fill in
    k = len(means)
    N = len(data)
    total = 0
    for i in range(N):
        valdenominator = 0
        for j in range(k):
            valdenominator += weights[j] * (norm(means[j],np.sqrt(varis[j])).pdf(data[i]))
        total += np.log(valdenominator)
    ll = total
    return ll


def main(datapath, k, tol):
    #read in dataset
    with open(datapath) as f:
        data = f.readlines()
    data = [float(x) for x in data]

    #train mixture model
    weights, means, varis, ll = train(data, k, tol)

    return weights,means,varis,ll


for i in range (2, 7):
     weights, means, varis, ll = main("data.txt", i , 1)
     for k in range(i):
         print(weights[k], "*N(x| ", means[k],",",varis[k],")")
#     print("Log-likelihood:", ll)
