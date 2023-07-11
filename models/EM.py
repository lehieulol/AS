import numpy as np
from scipy.stats import multivariate_normal

def EM(X, k=2, num_iterations=5):
    m, n = X.shape

    # Initialize parameters
    phi = np.full((k, 1), fill_value=1/k)
    mu = X[np.random.permutation(m)[:k]]
    sigma = [np.cov(X.T) for j in range(k)]

    for iteration in range(num_iterations):
        # E-step
        likelihood = np.zeros((k, m))
        for j in range(k):
            distribution = multivariate_normal(mean=mu[j], cov=sigma[j])
            likelihood[j] = distribution.pdf(X)
        
        numerator = likelihood*phi
        denominator = np.sum(numerator, axis=0)
        w = numerator/denominator
        idx = np.argmax(w, axis=0)

        # M-step
        phi = np.mean(w, axis=0)
        for j in range(k):
            mu[j] = np.sum(w[[j]].T*X, axis=0) / np.sum(w[[j]])
            sigma[j] = np.matmul((w[[j]].T*(X-mu[j])).T, (X-mu[j])) / np.sum(w[[j]])

    return idx, mu
