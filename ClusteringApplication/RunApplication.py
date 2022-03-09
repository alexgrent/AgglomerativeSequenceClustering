"""
enviroment for usage and runing the evaluations implemented in ClusteringApp
"""


TEST_DATA1 = "..\DataReader\DATA\Testdata1.csv"
TEST_DATA2 = "..\DataReader\DATA\Testdata2.csv"

import ClusteringApplication.ClusteringApp as app


App = app.ClusteringApp(TEST_DATA1)
"""
App.performScikitClusteringSingleLinkage()
App.performScikitClusteringCompleteLinkage()
App.performScikitClusteringAverageLinkage()
App.performScikitClusteringWardLinkage()
App.saveData("Test500.txt", "Test500")
"""
App.performBiopythonClusteringUPGMA()
App.performBiopythonClusteringTreecluster()