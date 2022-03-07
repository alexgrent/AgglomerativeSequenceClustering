import unittest
from DataReader import Datareader


class TestDataReader(unittest.TestCase):
    #Data = Datareader.Datareader("Testdata1.csv")
    Data = Datareader.Datareader()
    umi_list = []

    def test_usage(self):
        Data = Datareader.Datareader()
        self.Data.read_excel()
        print(len(self.Data.umi_list))  # list of all umis
        self.Data.remove_duplicate()
        print(len(self.Data.umi_list))  # generates umi_list_unique
        filtered_umis = Datareader.Filter.size(10, self.Data.umi_list_unique)
        print(filtered_umis)
        print(len(filtered_umis))
        self.umi_list = filtered_umis
        self.assertGreater(len(filtered_umis), 2, msg="UMIs in csv file found")
