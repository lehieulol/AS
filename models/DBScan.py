from sklearn.cluster import DBSCAN

def DBScan(X, k = 16, num_iterations=10):
    clustering = DBSCAN(eps=0.2, min_samples=6).fit(X)
    return clustering.fit_predict(), tmp