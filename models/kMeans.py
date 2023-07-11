import numpy as np

def kMeans(X, k=2, num_iterations=5):
    m, n = X.shape

    # Initialize parameters
    centroids = X[np.random.permutation(m)[:k]]
    idx = np.zeros(m)

    for iteration in range(num_iterations):
        # Color the points
        distance = np.zeros((k, m))
        for j in range(k):
            distance[j] = np.linalg.norm(X-centroids[j], axis=1)
        idx = np.argmin(distance, axis=0)

        # Moves the cluster centroid
        for j in range(k):
            points = X[idx==j]
            centroids[j] = np.mean(points, axis=0)

    return idx, centroids
