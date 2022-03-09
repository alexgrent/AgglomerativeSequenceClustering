import numpy as np


class DataCollector:
    log_ = str()
    logger = None

    def __init__(self, logfile= "Log.txt"):
        self.log_ = logfile
        self.logger = open(self.log_, "a")


    runtimeHamming = 0
    runtimeLevensthein = 0
    runtimeJaro = 0
    runtimeJaroWinkler = 0
    runtimeDamerau = 0
    runtimeMatchRating = 0

    #runtime scikit clustering
    #runtime average linkage
    runtimeHammingClusteringModelAverageLinkage = 0
    runtimeLevenstheinClusteringModelAverageLinkage = 0
    runtimeJaroClusteringModelAverageLinkage = 0
    runtimeJaroWinklerclusteringModelAverageLinkage = 0
    runtimeDamerauClusteringModelAverageLinkage = 0

    #runtime single linkage
    runtimeHammingClusteringModelSingleLinkage = 0
    runtimeLevenstheinClusteringModelSingleLinkage = 0
    runtimeJaroClusteringModelSingleLinkage =  0
    runtimeJaroWinklerclusteringModelSingleLinkage = 0
    runtimeDamerauClusteringModelSingleLinkage = 0

    #runtime complete linkage
    runtimehammingClusteringModelCompleteLinkage = 0
    runtimelevenstheinClusteringModelCompleteLinkage =0
    runtimejaroClusteringModelCompleteLinkage =  0
    runtimejaroWinklerclusteringModelCompleteLinkage =0
    runtimedamerauClusteringModelCompleteLinkage =0

    #runtime ward linkage
    runtimehammingClusteringModelWardLinkage = 0
    runtimelevenstheinClusteringModelWardLinkage = 0
    runtimejaroClusteringModelWardLinkage = 0
    runtimejaroWinklerclusteringModelWardLinkage = 0
    runtimedamerauClusteringModelWardLinkage = 0


    #Models scikit clustering:
    #models single linkage
    hammingClusteringModelSingleLinkage = None
    levenstheinClusteringModelSingleLinkage = None
    jaroClusteringModelSingleLinkage = None
    jaroWinklerclusteringModelSingleLinkage = None
    damerauClusteringModelSingleLinkage = None

    #models complete linkage
    hammingClusteringModelCompleteLinkage = None
    levenstheinClusteringModelCompleteLinkage = None
    jaroClusteringModelCompleteLinkage = None
    jaroWinklerclusteringModelCompleteLinkage = None
    damerauClusteringModelCompleteLinkage = None

    #models average linkage
    hammingClusteringModelAverageLinkage = None
    levenstheinClusteringModelAverageLinkage = None
    jaroClusteringModelAverageLinkage = None
    jaroWinklerclusteringModelAverageLinkage = None
    damerauClusteringModelAverageLinkage = None

    #models ward linkage
    hammingClusteringModelWardLinkage = None
    levenstheinClusteringModelWardLinkage = None
    jaroClusteringModelWardLinkage = None
    jaroWinklerclusteringModelWardLinkage = None
    damerauClusteringModelWardLinkage = None


    #matrix calculations
    hammingMatrix = np.array([])
    levenshteinMatrix = np.array([])
    jaroMatrix = np.array([])
    jaroWinklerMatrix = np.array([])
    damerauMatrix = np.array([])
    matchRatingMatrix = np.array([])

    def saveData(self,log_file, id): #id to identify datacollector in log_file, log_file => filename of spcific  testcase
        self.logger.writelines(id)
        self.logger.writelines(str(self.runtimeHamming)+"\n")
        self.logger.writelines(str(self.runtimeLevensthein)+"\n")
        self.logger.writelines(str(self.runtimeJaro)+"\n")
        self.logger.writelines(str(self.runtimeJaroWinkler)+"\n")
        self.logger.writelines(str(self.runtimeDamerau)+"\n")
        self.logger.writelines(str(self.runtimeMatchRating)+"\n")
        self.logger.writelines(str(self.runtimeHammingClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.runtimeLevenstheinClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.runtimeJaroClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.runtimeJaroWinklerclusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.runtimeDamerauClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.runtimeHammingClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.runtimeLevenstheinClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.runtimeJaroClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.runtimeJaroWinklerclusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.runtimeDamerauClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.runtimehammingClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.runtimelevenstheinClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.runtimejaroClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.runtimejaroWinklerclusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.runtimedamerauClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.runtimehammingClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.runtimelevenstheinClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.runtimejaroClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.runtimejaroWinklerclusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.runtimedamerauClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.hammingClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.levenstheinClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.jaroClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.jaroWinklerclusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.damerauClusteringModelSingleLinkage)+"\n")
        self.logger.writelines(str(self.hammingClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.levenstheinClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.jaroClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.jaroWinklerclusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.damerauClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines(str(self.hammingClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.levenstheinClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.jaroClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.jaroWinklerclusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.damerauClusteringModelAverageLinkage)+"\n")
        self.logger.writelines(str(self.hammingClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.levenstheinClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.jaroClusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.jaroWinklerclusteringModelWardLinkage)+"\n")
        self.logger.writelines(str(self.damerauClusteringModelWardLinkage)+"\n")
        self.logger.close()
        ######
        l = open(log_file, "w")
        l.writelines(str(self.runtimeHamming)+"\n")
        l.writelines(str(self.runtimeLevensthein)+"\n")
        l.writelines(str(self.runtimeJaro)+"\n")
        l.writelines(str(self.runtimeJaroWinkler)+"\n")
        l.writelines(str(self.runtimeDamerau)+"\n")
        l.writelines(str(self.runtimeMatchRating)+"\n")
        l.writelines(str(self.runtimeHammingClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.runtimeLevenstheinClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.runtimeJaroClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.runtimeJaroWinklerclusteringModelAverageLinkage))
        l.writelines(str(self.runtimeDamerauClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.runtimeHammingClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.runtimeLevenstheinClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.runtimeJaroClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.runtimeJaroWinklerclusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.runtimeDamerauClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.runtimehammingClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.runtimelevenstheinClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.runtimejaroClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.runtimejaroWinklerclusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.runtimedamerauClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.runtimehammingClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.runtimelevenstheinClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.runtimejaroClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.runtimejaroWinklerclusteringModelWardLinkage)+"\n")
        l.writelines(str(self.runtimedamerauClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.hammingClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.levenstheinClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.jaroClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.jaroWinklerclusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.damerauClusteringModelSingleLinkage)+"\n")
        l.writelines(str(self.hammingClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.levenstheinClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.jaroClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.jaroWinklerclusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.damerauClusteringModelCompleteLinkage)+"\n")
        l.writelines(str(self.hammingClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.levenstheinClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.jaroClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.jaroWinklerclusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.damerauClusteringModelAverageLinkage)+"\n")
        l.writelines(str(self.hammingClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.levenstheinClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.jaroClusteringModelWardLinkage)+"\n")
        l.writelines(str(self.jaroWinklerclusteringModelWardLinkage)+"\n")
        l.writelines(str(self.damerauClusteringModelWardLinkage)+"\n")
        l.close()
