from Distances.Distances import Distance
from Bio.Align.Applications import MafftCommandline, MuscleCommandline, ClustalwCommandline, ClustalOmegaCommandline
from Bio.Cluster import distancematrix, clustercentroids, treecluster, kcluster, somcluster, pca
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
import matplotlib.pyplot
import pylab
from scipy.spatial import distance_matrix
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor, DistanceMatrix
import pandas as pd
import numpy as np


class BiopythonClustering():
    DistanceMatrix = None

    def __init__(self, filename):
        self.DistanceMatrix = Distance(filename)


    def distance(self):
        matrix = self.DistanceMatrix.matrix_hamming_distance()

    def use_treecluster(self):
        matrix = self.DistanceMatrix.matrix_hamming_distance()
        print(matrix)
        tree = treecluster(matrix)
        return tree

    def Agglomerative_clustering_UPGMA(self):
        m = self.DistanceMatrix.matrix_hamming_distance().tolist()
        df = pd.DataFrame(m)
        dm = distance_matrix(df.values, df.values)
        distMatrix = DistanceMatrix([str(x) for x in range(len(dm))], [list(x[:i+1]) for i, x in enumerate(dm)])
        constructor = DistanceTreeConstructor()
        Tree = constructor.upgma(distMatrix)
        for i, c in enumerate(Tree.find_clades()):
            print("calculating..")
            if c.name.lower().find("inner") >=0:
                c.name =""
        Phylo.draw(tree=Tree)
        matplotlib.pyplot.pause(10)
        Phylo.draw_ascii(tree=Tree)
        matplotlib.pyplot.pause(10)
        print("end")


    def Agglomerative_clustering_tree(self, distance_matrix, linkage='m'): #s -> single linkage #m-> maximum linkage #a -> average linkage
        distance_matrix = np.delete(distance_matrix, 1, 0)
        tree = treecluster(data=None, mask=None, weight=None, transpose=False, method=linkage, dist='e', distancematrix=distancematrix())
        print(type(tree))
        print(tree)


    def plot_dendrogram(self, tree_object):
        for i, c in enumerate(tree_object.find_clades()):
            print("calculating..")
            if c.name.lower().find("inner") >=0:
                c.name =""
        Phylo.draw(tree=tree_object)

    def ascii_dendrogram(self, tree_object):
        for i, c in enumerate(tree_object.find_clades()):
            print("calculating..")
            if c.name.lower().find("inner") >=0:
                c.name =""
        Phylo.draw_ascii(tree=tree_object)

    def get_matrix(self, distance):
        if distance =="levensthein":
            return self.DistanceMatrix.matrix_levenstein_distance()
        if distance =="hamming":
            return self.DistanceMatrix.matrix_hamming_distance()
        if distance == "damerau":
            return self.DistanceMatrix.matrix_damerau_levenshtein_distance()
        if distance =="jaro":
           return self.DistanceMatrix.matrix_jaro_similarity()
        if distance =="jaroWinkler":
           return self.DistanceMatrix.matrix_jaro_winkler_similarity()


    def test_clustering(self):
        data = [[5, 7], [7, 3], [8, 1], [8, 1]]
        ctys = ['Boston', 'Phoenix', 'New York', "NY"]
        print(data)
        df = pd.DataFrame(data, columns=['xcord', 'ycord'], index=ctys)
        print(df)
        dm = distance_matrix(df.values, df.values)
        distMatrix = DistanceMatrix([str(x) for x in range(len(dm))], [list(x[:i+1]) for i, x in enumerate(dm)])
        constructor = DistanceTreeConstructor()
    #    Construct the phlyogenetic tree using UPGMA algorith
        UPGMATree = constructor.upgma(distMatrix)
        print(type(UPGMATree))
        for i, c in enumerate(UPGMATree.find_clades()):
            if c.name.lower().find("inner") >= 0:
                c.name = ""
        Phylo.draw(UPGMATree)
        matplotlib.pyplot.pause(10)
        print("fsdf", type(UPGMATree))






clustering = BiopythonClustering("..\DataReader\DATA\Testdata1.csv")
#clustering.AlginmentClustering("sequence.fasta")
t = clustering.use_treecluster()
print(type(t))
#clustering.test_clustering()
#clustering.Agglomerative_clustering_UPGMA()
clustering.Agglomerative_clustering()
#print(str(t[0])[:5])
#clustering.plot_tree(t)
