from cluster import *
from point import *

def kmeans(pointdata, clusterdata) :

    point = makePointList(pointdata)
    clusters = createClusters(clusterdata)
    vallist = [1] * len(pointdata)
    while (sum(vallist)):
        vallist = []
        for eachpoint in point:
            dest = eachpoint.closest(clusters)
            val = int(eachpoint.moveToCluster(dest))
            vallist.append(val)
        #   Hint: keep track here whether any point changed clusters by
        #  seeing if any moveToCluster call returns "True"
        for cluster in clusters:
            cluster.updateCenter()
    return clusters



if __name__ == '__main__' :
    data = np.array([[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]], dtype=float)
    centers = np.array([[0, 0], [1, 1]], dtype=float)

    clusters = kmeans(data, centers)
    for c in clusters :
        c.printAllPoints()
