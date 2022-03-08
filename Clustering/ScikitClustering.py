
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from Distances.Distances import Distance



class ScikitClustering():

    DistanceMatrix = None


    def __init__(self, data):
        self.DistanceMatrix = Distance(data)



    def Agglomerative_clustering(self, distancemetric = "hamming", linkage_='ward', matrixFile=None):  #agglomerative clusering using file gven at distance, also calculating a neww distnace matrix with Distacnces
            #either use distancemetric parameter or file   #for plotting with own parameter use plot_dendrogram method
            if matrixFile==None:
                matrix= self.get_matrix(distancemetric)
                model = AgglomerativeClustering(distance_threshold=0,n_clusters=None, linkage = linkage_)
                y = model.fit(matrix)
                #self.plot_dendrogram(model)
                return y
            else:
                matrix = self.DistanceMatrix.get_matrix_from_file(matrixFile)
                model = AgglomerativeClustering(distance_threshold=0, n_clusters=None, linkage=linkage_)
                y = model.fit(matrix)
                #self.plot_dendrogram(model)
                return y


    def save_dendrogram(self, model,title, save_name):
        plt.title(title)
        self.plot_dendrogram(model)
        plt.savefig(save_name)

    def Agglomerative_clustering_step(self, matrix, n_clusters_=2, affinity_='precomputed', memory_=None, connectivity_=None, compute_full_tree_='auto', linkage_='ward', distance_threshold_=None, compute_distances_=False):
        agg_model = AgglomerativeClustering(distance_threshold=0,n_clusters=None, linkage = linkage_)
        y = agg_model.fit(matrix)
        return y

    def plot_dendrogram(self, model, **kwargs):
        counts = np.zeros(model.children_.shape[0])
        n_samples = len(model.labels_)
        for i, merge in enumerate(model.children_):
            current_count = 0
            for child_idx in merge:
                if child_idx < n_samples:
                    current_count += 1  # leaf node
                else:
                    current_count += counts[child_idx - n_samples]
            counts[i] = current_count
        linkage_matrix = np.column_stack(
            [model.children_, model.distances_, counts]
        ).astype(float)
        dendrogram(linkage_matrix, **kwargs)
        #plt.pause(2)



    def get_matrix(self, distance):
        if distance == "levensthein":
            return self.DistanceMatrix.matrix_levenstein_distance()
        if distance == "hamming":
            return self.DistanceMatrix.matrix_hamming_distance()
        if distance == "damerau":
            return self.DistanceMatrix.matrix_damerau_levenshtein_distance()
        if distance == "jaro":
           return self.DistanceMatrix.matrix_jaro_similarity()
        if distance == "jaroWinkler":
           return self.DistanceMatrix.matrix_jaro_winkler_similarity()



"""Usage:
"""
"""
clustering = ScikitClustering("..\DataReader\DATA\Testdata1.csv")
clustering.Agglomerative_clustering()
"""