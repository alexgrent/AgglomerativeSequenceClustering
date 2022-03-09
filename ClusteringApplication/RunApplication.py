"""
enviroment for usage and runing the evaluations implemented in ClusteringApp
"""


TEST_DATA1 = "..\DataReader\DATA\Testdata1.csv"
TEST_DATA2 = "..\DataReader\DATA\Testdata2.csv"
TEST_DATA3 = "..\DataReader\DATA\Testdata100.csv"

import ClusteringApplication.ClusteringApp as app


App = app.ClusteringApp(TEST_DATA1)

#App.performScikitClusteringSingleLinkage()
#App.performScikitClusteringCompleteLinkage()
#App.performScikitClusteringAverageLinkage()
#App.performScikitClusteringWardLinkage()
#App.saveData("Test100.txt", "Test100")

#App.performBiopythonClusteringUPGMA()

#Do not use needs some debugging
#App.performBiopythonClusteringTreecluster()