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
        self.logger.writelines(str(self.runtimeHamming))
        self.logger.writelines(str(self.runtimeLevensthein))
        self.logger.writelines(str(self.runtimeJaro))
        self.logger.writelines(str(self.runtimeJaroWinkler))
        self.logger.writelines(str(self.runtimeDamerau))
        self.logger.writelines(str(self.runtimeMatchRating))
        self.logger.writelines(str(self.runtimeHammingClusteringModelAverageLinkage))
        self.logger.writelines(str(self.runtimeLevenstheinClusteringModelAverageLinkage))
        self.logger.writelines(str(self.runtimeJaroClusteringModelAverageLinkage))
        self.logger.writelines(str(self.runtimeJaroWinklerclusteringModelAverageLinkage))
        self.logger.writelines(str(self.runtimeDamerauClusteringModelAverageLinkage))
        self.logger.writelines(str(self.runtimeHammingClusteringModelSingleLinkage))
        self.logger.writelines(str(self.runtimeLevenstheinClusteringModelSingleLinkage))
        self.logger.writelines(str(self.runtimeJaroClusteringModelSingleLinkage))
        self.logger.writelines(str(self.runtimeJaroWinklerclusteringModelSingleLinkage))
        self.logger.writelines(str(self.runtimeDamerauClusteringModelSingleLinkage))
        self.logger.writelines(str(self.runtimehammingClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.runtimelevenstheinClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.runtimejaroClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.runtimejaroWinklerclusteringModelCompleteLinkage))
        self.logger.writelines(str(self.runtimedamerauClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.runtimehammingClusteringModelWardLinkage))
        self.logger.writelines(str(self.runtimelevenstheinClusteringModelWardLinkage))
        self.logger.writelines(str(self.runtimejaroClusteringModelWardLinkage))
        self.logger.writelines(str(self.runtimejaroWinklerclusteringModelWardLinkage))
        self.logger.writelines(str(self.runtimedamerauClusteringModelWardLinkage))
        self.logger.writelines(str(self.hammingClusteringModelSingleLinkage))
        self.logger.writelines(str(self.levenstheinClusteringModelSingleLinkage))
        self.logger.writelines(str(self.jaroClusteringModelSingleLinkage))
        self.logger.writelines(str(self.jaroWinklerclusteringModelSingleLinkage))
        self.logger.writelines(str(self.damerauClusteringModelSingleLinkage))
        self.logger.writelines(str(self.hammingClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.levenstheinClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.jaroClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.jaroWinklerclusteringModelCompleteLinkage))
        self.logger.writelines(str(self.damerauClusteringModelCompleteLinkage))
        self.logger.writelines(str(self.hammingClusteringModelAverageLinkage))
        self.logger.writelines(str(self.levenstheinClusteringModelAverageLinkage))
        self.logger.writelines(str(self.jaroClusteringModelAverageLinkage))
        self.logger.writelines(str(self.jaroWinklerclusteringModelAverageLinkage))
        self.logger.writelines(str(self.damerauClusteringModelAverageLinkage))
        self.logger.writelines(str(self.hammingClusteringModelWardLinkage))
        self.logger.writelines(str(self.levenstheinClusteringModelWardLinkage))
        self.logger.writelines(str(self.jaroClusteringModelWardLinkage))
        self.logger.writelines(str(self.jaroWinklerclusteringModelWardLinkage))
        self.logger.writelines(str(self.damerauClusteringModelWardLinkage))
        self.logger.close()
        ######
        l = open(log_file, "w")
        l.writelines(str(self.runtimeHamming))
        l.writelines(str(self.runtimeLevensthein))
        l.writelines(str(self.runtimeJaro))
        l.writelines(str(self.runtimeJaroWinkler))
        l.writelines(str(self.runtimeDamerau))
        l.writelines(str(self.runtimeMatchRating))
        l.writelines(str(self.runtimeHammingClusteringModelAverageLinkage))
        l.writelines(str(self.runtimeLevenstheinClusteringModelAverageLinkage))
        l.writelines(str(self.runtimeJaroClusteringModelAverageLinkage))
        l.writelines(str(self.runtimeJaroWinklerclusteringModelAverageLinkage))
        l.writelines(str(self.runtimeDamerauClusteringModelAverageLinkage))
        l.writelines(str(self.runtimeHammingClusteringModelSingleLinkage))
        l.writelines(str(self.runtimeLevenstheinClusteringModelSingleLinkage))
        l.writelines(str(self.runtimeJaroClusteringModelSingleLinkage))
        l.writelines(str(self.runtimeJaroWinklerclusteringModelSingleLinkage))
        l.writelines(str(self.runtimeDamerauClusteringModelSingleLinkage))
        l.writelines(str(self.runtimehammingClusteringModelCompleteLinkage))
        l.writelines(str(self.runtimelevenstheinClusteringModelCompleteLinkage))
        l.writelines(str(self.runtimejaroClusteringModelCompleteLinkage))
        l.writelines(str(self.runtimejaroWinklerclusteringModelCompleteLinkage))
        l.writelines(str(self.runtimedamerauClusteringModelCompleteLinkage))
        l.writelines(str(self.runtimehammingClusteringModelWardLinkage))
        l.writelines(str(self.runtimelevenstheinClusteringModelWardLinkage))
        l.writelines(str(self.runtimejaroClusteringModelWardLinkage))
        l.writelines(str(self.runtimejaroWinklerclusteringModelWardLinkage))
        l.writelines(str(self.runtimedamerauClusteringModelWardLinkage))
        l.writelines(str(self.hammingClusteringModelSingleLinkage))
        l.writelines(str(self.levenstheinClusteringModelSingleLinkage))
        l.writelines(str(self.jaroClusteringModelSingleLinkage))
        l.writelines(str(self.jaroWinklerclusteringModelSingleLinkage))
        l.writelines(str(self.damerauClusteringModelSingleLinkage))
        l.writelines(str(self.hammingClusteringModelCompleteLinkage))
        l.writelines(str(self.levenstheinClusteringModelCompleteLinkage))
        l.writelines(str(self.jaroClusteringModelCompleteLinkage))
        l.writelines(str(self.jaroWinklerclusteringModelCompleteLinkage))
        l.writelines(str(self.damerauClusteringModelCompleteLinkage))
        l.writelines(str(self.hammingClusteringModelAverageLinkage))
        l.writelines(str(self.levenstheinClusteringModelAverageLinkage))
        l.writelines(str(self.jaroClusteringModelAverageLinkage))
        l.writelines(str(self.jaroWinklerclusteringModelAverageLinkage))
        l.writelines(str(self.damerauClusteringModelAverageLinkage))
        l.writelines(str(self.hammingClusteringModelWardLinkage))
        l.writelines(str(self.levenstheinClusteringModelWardLinkage))
        l.writelines(str(self.jaroClusteringModelWardLinkage))
        l.writelines(str(self.jaroWinklerclusteringModelWardLinkage))
        l.writelines(str(self.damerauClusteringModelWardLinkage))
        l.close()
