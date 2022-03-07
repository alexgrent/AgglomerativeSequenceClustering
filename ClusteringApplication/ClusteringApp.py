import Datacollector.DataCollector as dc
import Distances.Distances as d
import Clustering.ScikitClustering as scc
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

    def __init__(self, Testdatafile):
        print("starting evaluation")
        self.distanceCalculation = d.Distance("..\DataReader\DATA\Testdata1.csv")
        self.dataCollector = dc.DataCollector()
        self.scikitClustering = scc.ScikitClustering("..\DataReader\DATA\Testdata1.csv")

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
        self.dataCollector.runtimeHammingClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='single')
        self.scikitClustering.save_dendrogram(self.dataCollector.runtimeHammingClusteringModelSingleLinkage, "Single linkage: Hamming Distance", "test.png") #TODO vizulize
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelSingleLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='single')
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelSingleLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.runtimeJaroClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='single')
        end_ = timer()
        self.dataCollector.runtimeJaroClusteringModelSingleLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='single')
        end_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelSingleLinkage = timedelta(seconds= end_-start_)

        start_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelSingleLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='single')
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelSingleLinkage = timedelta(seconds=end_ - start_)

    def performScikitClusteringCompleteLinkage(self):
        print("Scikit clustering Complete linkage")
        start_ = timer()
        self.dataCollector.hammingClusteringModelCompleteLinkage= self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='complete')
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.levenstheinClusteringModelCompleteLinkage    = self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='complete')
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroClusteringModelCompleteLinkage    = self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='complete')
        end_ = timer()
        self.dataCollector.runtimeJaroClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroWinklerclusteringModelCompleteLinkage    = self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='complete')
        end_ = timer()
        self.dataCollector.runtimejaroWinklerClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.damerauClusteringModelCompleteLinkage  = self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='complete')
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelCompleteLinkage = timedelta(seconds=end_ - start_)

    def performScikitClusteringAverageLinkage(self):
        print("scikit clustering average linkage")
        start_ = timer()
        self.dataCollector.hammingClusteringModelAverageLinkage =  self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='complete')
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.levenstheinClusteringModelAverageLinkage=self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='average')
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelAverageLinkage = timedelta(seconds=end_-start_)

        start_ = timer()
        self.dataCollector.jaroClusteringModelAverageLinkage= self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='average')
        end_ = timer()
        self.dataCollector.runtimeJaroclusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroWinklerclusteringModelAverageLinkage=self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='average')
        end_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelAverageLinkage = timedelta(seconds=end_ -start_)

        start_ = timer()
        self.dataCollector.damerauClusteringModelAverageLinkage= self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='average')
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

    def performScikitClusteringWardLinkage(self):
        print("Scikit clustering Ward linkage")
        start_ = timer()
        self.dataCollector.hammingClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="hamming", linkage_='ward')
        end_ = timer()
        self.dataCollector.runtimeHammingClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.levenstheinClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="levensthein", linkage_='ward')
        end_ = timer()
        self.dataCollector.runtimeLevenstheinClusteringModelAverageLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaro", linkage_='ward')
        end_ = timer()
        self.dataCollector.runtimeJaroclusteringModelWardLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.jaroWinklerclusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="jaroWinkler", linkage_='ward')
        end_ = timer()
        self.dataCollector.runtimeJaroWinklerclusteringModelWardLinkage = timedelta(seconds=end_ - start_)

        start_ = timer()
        self.dataCollector.damerauClusteringModelWardLinkage = self.scikitClustering.Agglomerative_clustering(distancemetric="damerau", linkage_='ward')
        end_ = timer()
        self.dataCollector.runtimeDamerauClusteringModelWardLinkage = timedelta(seconds=end_ - start_)