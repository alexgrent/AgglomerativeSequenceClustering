from Bio import SeqIO
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

class Datareader:
    filename =""
    sequences_list = []
    umi_list = []
    umi_list_unique = []        #umis without duplicates

    #def __init__(self):
    #    self.filename = "DATA\Testdata1.csv"

    def __init__(self, filename):
        self.filename = filename

    def print_data(self):
        print("\nFilename: ", self.filename)
        print("\nSequences: ", self.sequences_list)
        print("\nUMIs: ", self.umi_list)

    def remove_duplicate(self):
        l = list(dict.fromkeys(self.umi_list))
        self.umi_list_unique = l
        return l

    def open_file(self):
        return open(self.filename)

    def read_seq(self, format):
        if format == "fastq":
            for record in SeqIO.parse(self.filename, format):
                self.sequences_list.append(str(record.seq))
        elif format == "csv":
            self.read_excel()  #use pandas !!!!
        else:
            print("Format not supported")

    def read_excel(self):
        data = open(self.filename, "r")
        for line in data:
            line_list = line.split("\t")
            self.sequences_list.append(line_list[4])
            self.umi_list.append(line_list[1])

    def convert_to_df(self):
        return pd.DataFrame(list(zip(self.sequences_list, self.umi_list)), columns=['Sequence', 'UMI'])

    def get_dataframe(self):
        return self.convert_to_df()

    def get_dataframe_umi(self):
        return pd.DataFrame(list(zip(self.umi_list)), columns=['UMI'])

    def get_umis_by_size(self, size=10):
        return Filter.size(size, self.umi_list)  #should be 10 just for verification




class Data_Formating(Datareader):
    def print_umis_file(self):
        f_out = open("umis.txt", "w")
        for umi in self.umi_list:
            f_out.write("> \n")
            f_out.write(str(umi)+"\n")

class Filter:
    @staticmethod
    def size(size_, list_type):
        new_list = []
        for i in list_type:
            if len(i) == size_:
                new_list.append(i)
            else:
                print(i)
        return new_list





#Usage:
"""
#d = Datareader("DATA\Testdata2.csv")
d = Datareader()
d.read_excel()
print(len(d.umi_list))  #list of all umis
d.remove_duplicate()
print(len(d.umi_list))  #generates umi_list_unique
filtered_umis = Filter.size(10,d.umi_list_unique)
print(filtered_umis)
print(len(filtered_umis))
"""
