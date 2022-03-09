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
        self.logger.writelines("id"+id)
        self.logger.writelines("runtimeHamming;"+str(self.runtimeHamming)+"\n")
        self.logger.writelines("runtimeLevensthein;"+str(self.runtimeLevensthein)+"\n")
        self.logger.writelines("runtimeJaro;"+str(self.runtimeJaro)+"\n")
        self.logger.writelines("runtimeJaroWinkler;"+str(self.runtimeJaroWinkler)+"\n")
        self.logger.writelines("runtimeDamerau;"+str(self.runtimeDamerau)+"\n")
        self.logger.writelines("runtimeMatchRating;"+str(self.runtimeMatchRating)+"\n")
        self.logger.writelines("runtimeHammingClusteringModelAverageLinkage;"+str(self.runtimeHammingClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("runtimeLevenstheinClusteringModelAverageLinkage;"+str(self.runtimeLevenstheinClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("runtimeJaroClusteringModelAverageLinkage;"+str(self.runtimeJaroClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("runtimeJaroWinklerclusteringModelAverageLinkage;"+str(self.runtimeJaroWinklerclusteringModelAverageLinkage)+"\n")
        self.logger.writelines("runtimeDamerauClusteringModelAverageLinkage;"+str(self.runtimeDamerauClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("runtimeHammingClusteringModelSingleLinkage;"+str(self.runtimeHammingClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("runtimeLevenstheinClusteringModelSingleLinkage;"+str(self.runtimeLevenstheinClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("runtimeJaroClusteringModelSingleLinkage;"+str(self.runtimeJaroClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("runtimeJaroWinklerclusteringModelSingleLinkage;"+str(self.runtimeJaroWinklerclusteringModelSingleLinkage)+"\n")
        self.logger.writelines("runtimeDamerauClusteringModelSingleLinkage;"+str(self.runtimeDamerauClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("runtimehammingClusteringModelCompleteLinkage;"+str(self.runtimehammingClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("runtimelevenstheinClusteringModelCompleteLinkage;"+str(self.runtimelevenstheinClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("runtimejaroClusteringModelCompleteLinkage;"+str(self.runtimejaroClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("runtimejaroWinklerclusteringModelCompleteLinkage;"+str(self.runtimejaroWinklerclusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("runtimedamerauClusteringModelCompleteLinkage;"+str(self.runtimedamerauClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("runtimehammingClusteringModelWardLinkage;"+str(self.runtimehammingClusteringModelWardLinkage)+"\n")
        self.logger.writelines("runtimelevenstheinClusteringModelWardLinkage;"+str(self.runtimelevenstheinClusteringModelWardLinkage)+"\n")
        self.logger.writelines("runtimejaroClusteringModelWardLinkage;"+str(self.runtimejaroClusteringModelWardLinkage)+"\n")
        self.logger.writelines("runtimejaroWinklerclusteringModelWardLinkage;"+str(self.runtimejaroWinklerclusteringModelWardLinkage)+"\n")
        self.logger.writelines("runtimedamerauClusteringModelWardLinkage;"+str(self.runtimedamerauClusteringModelWardLinkage)+"\n")
        self.logger.writelines("hammingClusteringModelSingleLinkage;"+str(self.hammingClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("levenstheinClusteringModelSingleLinkage;"+str(self.levenstheinClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("jaroClusteringModelSingleLinkage;"+str(self.jaroClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("jaroWinklerclusteringModelSingleLinkage;"+str(self.jaroWinklerclusteringModelSingleLinkage)+"\n")
        self.logger.writelines("damerauClusteringModelSingleLinkage;"+str(self.damerauClusteringModelSingleLinkage)+"\n")
        self.logger.writelines("hammingClusteringModelCompleteLinkage;"+str(self.hammingClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("levenstheinClusteringModelCompleteLinkage;"+str(self.levenstheinClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("jaroClusteringModelCompleteLinkage;"+str(self.jaroClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("jaroWinklerclusteringModelCompleteLinkage;"+str(self.jaroWinklerclusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("damerauClusteringModelCompleteLinkage"+str(self.damerauClusteringModelCompleteLinkage)+"\n")
        self.logger.writelines("hammingClusteringModelAverageLinkage;"+str(self.hammingClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("levenstheinClusteringModelAverageLinkage;"+str(self.levenstheinClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("jaroClusteringModelAverageLinkage;"+str(self.jaroClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("jaroWinklerclusteringModelAverageLinkage;"+str(self.jaroWinklerclusteringModelAverageLinkage)+"\n")
        self.logger.writelines("damerauClusteringModelAverageLinkage;"+str(self.damerauClusteringModelAverageLinkage)+"\n")
        self.logger.writelines("hammingClusteringModelWardLinkage;"+str(self.hammingClusteringModelWardLinkage)+"\n")
        self.logger.writelines("levenstheinClusteringModelWardLinkage;"+str(self.levenstheinClusteringModelWardLinkage)+"\n")
        self.logger.writelines("jaroClusteringModelWardLinkage;"+str(self.jaroClusteringModelWardLinkage)+"\n")
        self.logger.writelines("jaroWinklerclusteringModelWardLinkage;"+str(self.jaroWinklerclusteringModelWardLinkage)+"\n")
        self.logger.writelines("damerauClusteringModelWardLinkage;"+str(self.damerauClusteringModelWardLinkage)+"\n")
        self.logger.close()
        ######
        l = open(log_file, "w")
        l.writelines("id;"+id)
        l.writelines("runtimeHamming;"+str(self.runtimeHamming)+"\n")
        l.writelines("runtimeLevensthein;"+str(self.runtimeLevensthein)+"\n")
        l.writelines("runtimeJaro;"+str(self.runtimeJaro)+"\n")
        l.writelines("runtimeJaroWinkler;"+str(self.runtimeJaroWinkler)+"\n")
        l.writelines("runtimeDamerau;"+str(self.runtimeDamerau)+"\n")
        l.writelines("runtimeMatchRating;"+str(self.runtimeMatchRating)+"\n")
        l.writelines("runtimeHammingClusteringModelAverageLinkage;"+str(self.runtimeHammingClusteringModelAverageLinkage)+"\n")
        l.writelines("runtimeLevenstheinClusteringModelAverageLinkage;"+str(self.runtimeLevenstheinClusteringModelAverageLinkage)+"\n")
        l.writelines("runtimeJaroClusteringModelAverageLinkage;"+str(self.runtimeJaroClusteringModelAverageLinkage)+"\n")
        l.writelines("runtimeJaroWinklerclusteringModelAverageLinkage;"+str(self.runtimeJaroWinklerclusteringModelAverageLinkage))
        l.writelines("runtimeDamerauClusteringModelAverageLinkage;"+str(self.runtimeDamerauClusteringModelAverageLinkage)+"\n")
        l.writelines("runtimeHammingClusteringModelSingleLinkage;"+str(self.runtimeHammingClusteringModelSingleLinkage)+"\n")
        l.writelines("runtimeLevenstheinClusteringModelSingleLinkage;"+str(self.runtimeLevenstheinClusteringModelSingleLinkage)+"\n")
        l.writelines("runtimeJaroClusteringModelSingleLinkage;"+str(self.runtimeJaroClusteringModelSingleLinkage)+"\n")
        l.writelines("runtimeJaroWinklerclusteringModelSingleLinkage;"+str(self.runtimeJaroWinklerclusteringModelSingleLinkage)+"\n")
        l.writelines("runtimeDamerauClusteringModelSingleLinkage;"+str(self.runtimeDamerauClusteringModelSingleLinkage)+"\n")
        l.writelines("runtimehammingClusteringModelCompleteLinkage;"+str(self.runtimehammingClusteringModelCompleteLinkage)+"\n")
        l.writelines("runtimelevenstheinClusteringModelCompleteLinkage;"+str(self.runtimelevenstheinClusteringModelCompleteLinkage)+"\n")
        l.writelines("runtimejaroClusteringModelCompleteLinkage;"+str(self.runtimejaroClusteringModelCompleteLinkage)+"\n")
        l.writelines("runtimejaroWinklerclusteringModelCompleteLinkage;"+str(self.runtimejaroWinklerclusteringModelCompleteLinkage)+"\n")
        l.writelines("runtimedamerauClusteringModelCompleteLinkage;"+str(self.runtimedamerauClusteringModelCompleteLinkage)+"\n")
        l.writelines("runtimehammingClusteringModelWardLinkage;"+str(self.runtimehammingClusteringModelWardLinkage)+"\n")
        l.writelines("runtimelevenstheinClusteringModelWardLinkage;"+str(self.runtimelevenstheinClusteringModelWardLinkage)+"\n")
        l.writelines("runtimejaroClusteringModelWardLinkage;"+str(self.runtimejaroClusteringModelWardLinkage)+"\n")
        l.writelines("runtimejaroWinklerclusteringModelWardLinkage;"+str(self.runtimejaroWinklerclusteringModelWardLinkage)+"\n")
        l.writelines("runtimedamerauClusteringModelWardLinkage;"+str(self.runtimedamerauClusteringModelWardLinkage)+"\n")
        l.writelines("hammingClusteringModelSingleLinkage;"+str(self.hammingClusteringModelSingleLinkage)+"\n")
        l.writelines("levenstheinClusteringModelSingleLinkage;"+str(self.levenstheinClusteringModelSingleLinkage)+"\n")
        l.writelines("jaroClusteringModelSingleLinkage;"+str(self.jaroClusteringModelSingleLinkage)+"\n")
        l.writelines("jaroWinklerclusteringModelSingleLinkage;"+str(self.jaroWinklerclusteringModelSingleLinkage)+"\n")
        l.writelines("damerauClusteringModelSingleLinkage;"+str(self.damerauClusteringModelSingleLinkage)+"\n")
        l.writelines("hammingClusteringModelCompleteLinkage;"+str(self.hammingClusteringModelCompleteLinkage)+"\n")
        l.writelines("levenstheinClusteringModelCompleteLinkage;"+str(self.levenstheinClusteringModelCompleteLinkage)+"\n")
        l.writelines("jaroClusteringModelCompleteLinkage;"+str(self.jaroClusteringModelCompleteLinkage)+"\n")
        l.writelines("jaroWinklerclusteringModelCompleteLinkage;"+str(self.jaroWinklerclusteringModelCompleteLinkage)+"\n")
        l.writelines("damerauClusteringModelCompleteLinkage;"+str(self.damerauClusteringModelCompleteLinkage)+"\n")
        l.writelines("hammingClusteringModelAverageLinkage;"+str(self.hammingClusteringModelAverageLinkage)+"\n")
        l.writelines("levenstheinClusteringModelAverageLinkage;"+str(self.levenstheinClusteringModelAverageLinkage)+"\n")
        l.writelines("jaroClusteringModelAverageLinkage;"+str(self.jaroClusteringModelAverageLinkage)+"\n")
        l.writelines("jaroWinklerclusteringModelAverageLinkage;"+str(self.jaroWinklerclusteringModelAverageLinkage)+"\n")
        l.writelines("damerauClusteringModelAverageLinkage;"+str(self.damerauClusteringModelAverageLinkage)+"\n")
        l.writelines("hammingClusteringModelWardLinkage;"+str(self.hammingClusteringModelWardLinkage)+"\n")
        l.writelines("levenstheinClusteringModelWardLinkage;"+str(self.levenstheinClusteringModelWardLinkage)+"\n")
        l.writelines("jaroClusteringModelWardLinkage;"+str(self.jaroClusteringModelWardLinkage)+"\n")
        l.writelines("jaroWinklerclusteringModelWardLinkage;"+str(self.jaroWinklerclusteringModelWardLinkage)+"\n")
        l.writelines("damerauClusteringModelWardLinkage;"+str(self.damerauClusteringModelWardLinkage)+"\n")
        l.close()
