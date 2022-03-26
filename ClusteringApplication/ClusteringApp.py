import Datacollector.DataCollector as dc
import Distances.Distances as d
import Clustering.ScikitClustering as scc
import Clustering.BiopythonClustering as bc
from timeit import default_timer as timer
from datetime import timedelta
from matplotlib import pyplot as plt
"""
ClusteringApp uses Datacollector parameters in folder for saving the evaluated data
the calculation of specific task is implemented in the class the evaluation not!!
"""


class ClusteringApp:
    distanceCalculater = None
    dataCollector = None
    scikitClustering = None
    biopythonClustering = None


    def __init__(self, Testdatafile):
        print("starting evaluation")
        self.distanceCalculation = d.Distance(Testdatafile)
        self.dataCollector = dc.DataCollector()
        self.scikitClustering = scc.ScikitClustering(Testdatafile)
        self.biopythonClustering = bc.BiopythonClustering(Testdatafile)

    def saveData(self, log_file, id):
        self.dataCollector.saveData(log_file, id)

    def createDistances(self):
        #createing hamming distance + timing -> saved in datacollector for later evaluation
        startHammingTimer = timer()
        hamming = self.distanceCalculation.matrix_hamming_distance()
        self.dataCollector.hammingMatrix = hamming
        endHammingTimer= timer()
        self.dataCollector.runtimeHamming = timedelta(seconds=endHammingTimer-startHammingTimer)

        #creating Levensthein distance + Timing
        startLevenshteinTimer = timer()
        levensthein = self.distanceCalculation.matrix_levenstein_distance()
        self.dataCollector.levenshteinMatrix = levensthein
        endLevenshteinTimer = timer()
        self.dataCollector.runtimeLevensthein = timedelta(seconds=endLevenshteinTimer-startLevenshteinTimer)

        # creating jaro distance + Timing
        startJaroTimer = timer()
        jaro = self.distanceCalculation.matrix_jaro_similarity()
        self.dataCollector.jaroMatrix = jaro
        endJaroTimer = timer()
        self.dataCollector.runtimeJaro = timedelta(seconds=endJaroTimer-startJaroTimer)

        #creating jaro winkler + Timing
        startJaroWinklerTimer = timer()
        jaro_winkler = self.distanceCalculation.matrix_jaro_winkler_similarity()
        self.dataCollector.jaroWinklerMatrix = jaro_winkler
        endJaroWinklerTimer = timer()
        self.dataCollector.runtimeJaroWinkler = timedelta(seconds=endJaroWinklerTimer-startJaroWinklerTimer)

        #creating damerau distance + Timing
        startDamerauTimer = timer()
        damerau_levenshtein = self.distanceCalculation.matrix_damerau_levenshtein_distance()
        self.dataCollector.damerauMatrix = damerau_levenshtein
        endDamerauTimer = timer()
        self.dataCollector.runtimeDamerau = timedelta(seconds=endDamerauTimer-startDamerauTimer)

    def performScikitClusteringSingleLinkage(self):
        print("Scikit Clustering: Single linkage")
        start_ = timer()
        self.dataCollector.runtimeHammingClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='single',show=True)
        self.scikitClustering.save_dendrogram(self.dataCollector.runtimeHammingClusteringModelSingleLinkage, "Single linkage: Hamming Distance", "single_linkage_hamming.png")
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelSingleLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='single', show=False)
        self.scikitClustering.save_dendrogram(self.dataCollector.runtimeLevenstheinClusteringModelSingleLinkage, "Single linkage: Levensthein Distance", "single_linkage_levensthein.png")
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelSingleLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.runtimeJaroClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='single')
        self.scikitClustering.save_dendrogram(self.dataCollector.runtimeJaroClusteringModelSingleLinkage, "Single linkage: Jaro Distance", "single_linkage_jaro.png")
        end_ = timer()
        self.dataCollector.runtimeJaroClusteringModelSingleLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='single')
        self.scikitClustering.save_dendrogram(self.dataCollector.runtimeJaroWinklerclusteringModelSingleLinkage, "Single linkage: Jaro-Winkler Distance", "single_linkage_jaro_winkler.png")
        end_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelSingleLinkage = timedelta(seconds= end_-start_)

        start_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='single')
        self.scikitClustering.save_dendrogram(self.dataCollector.runtimeDamerauClusteringModelSingleLinkage, "Single linkage: Damerau Distance", "single_linkage_damerau.png")
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelSingleLinkage = timedelta(seconds=end_ - start_)

    def performScikitClusteringCompleteLinkage(self):
        print("Scikit clustering Complete linkage")
        start_ = timer()
        self.dataCollector.hammingClusteringModelCompleteLinkage= self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='complete')
        self.scikitClustering.save_dendrogram(self.dataCollector.hammingClusteringModelCompleteLinkage, "Complete linkage: Hamming Distance", "complete_linkage_hamming.png")
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.levenstheinClusteringModelCompleteLinkage  = self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='complete')
        self.scikitClustering.save_dendrogram(self.dataCollector.levenstheinClusteringModelCompleteLinkage, "Complete linkage: Levensthein Distance", "complete_linkage_levensthein.png")
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroClusteringModelCompleteLinkage    = self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='complete')
        self.scikitClustering.save_dendrogram(self.dataCollector.jaroClusteringModelCompleteLinkage, "Complete linkage: Jaro Distance", "complete_linkage_jaro.png")
        end_ = timer()
        self.dataCollector.runtimeJaroClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroWinklerclusteringModelCompleteLinkage    = self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='complete')
        self.scikitClustering.save_dendrogram(self.dataCollector.jaroWinklerclusteringModelCompleteLinkage, "Complete linkage: Jaro-Winkler Distance", "complete_linkage_jarowinkler.png")
        end_ = timer()
        self.dataCollector.runtimejaroWinklerClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.damerauClusteringModelCompleteLinkage  = self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='complete')
        self.scikitClustering.save_dendrogram(self.dataCollector.damerauClusteringModelCompleteLinkage, "Complete linkage: Damerau Distance", "complete_linkage_damerau.png")
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

    def performScikitClusteringAverageLinkage(self):
        print("scikit clustering average linkage")
        start_ = timer()
        self.dataCollector.hammingClusteringModelAverageLinkage =  self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='average')
        self.scikitClustering.save_dendrogram(self.dataCollector.hammingClusteringModelAverageLinkage, "Average linkage: Hamming Distance", "average_linkage_hamming.png")
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.levenstheinClusteringModelAverageLinkage=self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='average')
        self.scikitClustering.save_dendrogram(self.dataCollector.levenstheinClusteringModelCompleteLinkage, "Average linkage: Levensthein Distance", "average_linkage_levensthein.png")
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelAverageLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.jaroClusteringModelAverageLinkage= self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='average')
        self.scikitClustering.save_dendrogram(self.dataCollector.jaroClusteringModelAverageLinkage, "Average linkage: Jaro Distance", "average_linkage_jaro.png")
        end_ = timer()
        self.dataCollector.runtimeJaroclusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroWinklerclusteringModelAverageLinkage=self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='average')
        self.scikitClustering.save_dendrogram(self.dataCollector.jaroWinklerclusteringModelAverageLinkage, "Average linkage: Jaro-Winkler Distance","average_linkage_jarowinkler.png")
        end_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelAverageLinkage = timedelta(seconds=end_ -start_)

        start_ = timer()
        self.dataCollector.damerauClusteringModelAverageLinkage= self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='average')
        self.scikitClustering.save_dendrogram(self.dataCollector.damerauClusteringModelAverageLinkage, "Average linkage: Damerau Distance", "average_linkage_damerau.png")
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

    def performScikitClusteringWardLinkage(self):
        print("Scikit clustering Ward linkage")
        start_ = timer()
        self.dataCollector.hammingClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='ward')
        self.scikitClustering.save_dendrogram(self.dataCollector.hammingClusteringModelWardLinkage, "Ward linkage: Hamming Distance", "ward_linkage_hamming.png")
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.levenstheinClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='ward')
        self.scikitClustering.save_dendrogram(self.dataCollector.levenstheinClusteringModelWardLinkage, "Ward linkage: Levensthein Distance", "ward_linkage_levensthein.png")
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='ward')
        self.scikitClustering.save_dendrogram(self.dataCollector.jaroClusteringModelWardLinkage, "Ward linkage: Jaro Distance", "ward_linkage_jaro.png")
        end_ = timer()
        self.dataCollector.runtimeJaroclusteringModelWardLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroWinklerclusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='ward')
        self.scikitClustering.save_dendrogram(self.dataCollector.jaroWinklerclusteringModelWardLinkage, "Ward linkage: Jaro-Winkler Distance", "ward_linkage_jaroWinkler.png")
        end_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelWardLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.damerauClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='ward')
        self.scikitClustering.save_dendrogram(self.dataCollector.damerauClusteringModelWardLinkage, "Ward linkage: Damerau Distance", "ward_linkage_damerau.png")
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelWardLinkage = timedelta(seconds=end_ - start_)

    def performBiopythonClusteringUPGMA(self):
        tree = self.biopythonClustering.Agglomerative_clustering_UPGMA()
        self.biopythonClustering.plot_dendrogram(tree,True, "upgmatree")
        #self.biopythonClustering.plot_ascii_dendrogram(tree)

    def performBiopythonClusteringTreecluster(self):
        self.biopythonClustering.Agglomerative_clustering_tree("hamming", linkage='s')
        self.biopythonClustering.Agglomerative_clustering_tree( "hamming", linkage='a')
        self.biopythonClustering.Agglomerative_clustering_tree( "hamming", linkage='m')

    def runtimeResultsClustering(self):  #runtime calculation with exisiting distance matrix and without visulaiziation
        hamming = self.distanceCalculation.matrix_hamming_distance()
        self.distanceCalculation.save_matrix("Test_matrix",hamming)
        print("###Starting clustering runtime tests###")

        start_ = timer()
        self.scikitClustering.Agglomerative_clustering("hamming", "single", "Test_matrix", False)
        end_ = timer()
        print("Runtime: Scikit Clustering Single linkage: ", timedelta(seconds=end_-start_))

        start_ = timer()
        self.scikitClustering.Agglomerative_clustering("hamming", "complete", "Test_matrix", False)
        end_ = timer()
        print("Runtime: Scikit Clustering Complete linkage: ", timedelta(seconds=end_-start_))

        start_ = timer()
        self.scikitClustering.Agglomerative_clustering("hamming", "average", "Test_matrix", False)
        end_ = timer()
        print("Runtime: Scikit Clustering Average linkage: ", timedelta(seconds=end_-start_))

        start_ = timer()
        self.scikitClustering.Agglomerative_clustering("hamming", "ward", "Test_matrix", False)
        end_ = timer()
        print("Runtime: Scikit Clustering Ward linkage: ", timedelta(seconds=end_-start_))

        start_ = timer()
        #self.biopythonClustering.Agglomerative_clustering_UPGMA(hamming, "Test_matrix")
        end_ = timer()
        print("Runtime: Biopython UPGMA: ",timedelta(seconds=end_-start_))

        start_ = timer()
        #self.biopythonClustering.Agglomerative_clustering_tree(hamming, linkage='s')
        end_ = timer()
        print("Runtime: Biopython Treecluster Single linkage: ",timedelta(seconds=end_-start_))

        start_ = timer()
        #self.biopythonClustering.Agglomerative_clustering_tree(hamming, linkage='a')
        end_ = timer()
        print("Runtime: Biopython Treecluster Average linkage: ",timedelta(seconds=end_-start_))

        start_ = timer()
        #self.biopythonClustering.Agglomerative_clustering_tree(hamming, linkage='m')
        end_ = timer()
        print("Runtime: Biopython Treecluster Complete linkage: ",timedelta(seconds=end_-start_))

