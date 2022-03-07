import pandas as pd
import numpy as np
import DataReader.Datareader as Data
import DataReader
from Bio.Cluster import distancematrix, clustercentroids, treecluster, kcluster, somcluster, pca
from jellyfish import hamming_distance, levenshtein_distance, jaro_similarity, jaro_winkler_similarity, damerau_levenshtein_distance, match_rating_comparison
from numba  import jit


class Distance:
    sequences = []
    matrix = np.array([])
    Data_ = Data.Datareader


    #def __init__ (self, sequences):
    #    self.sequences = sequences

    def __init__(self, filename):   #using Datareader within the class using the file in default constructor
        #self.Data_ = Data.Datareader("..\DataReader\DATA\Testdata2.csv")
        self.Data_ = Data.Datareader(filename)
        self.Data_.read_excel()
        print(len(self.Data_.umi_list))  # list of all umis
        self.Data_.remove_duplicate()
        print(len(self.Data_.umi_list))  # generates umi_list_unique
        filtered_umis = self.Data_.get_umis_by_size(10)
        print(filtered_umis)
        print(len(filtered_umis))
        self.sequences = filtered_umis


    def init_matrix(self):
        matrix = np.array([])
        self.sequences.pop(0)
        for i in self.sequences:
            matrix = np.append(matrix, 0)
        return matrix

    def save_matrix(self, filename, distance_marix): #saves matrix in file as csv
        out_writer = open(filename, "w")
        out_writer.write('\n'.join([','.join(['{:4}'.format(item) for item in row])
                         for row in distance_marix]))
        out_writer.close()

    def get_matrix_from_file(self, filename):
        m = np.loadtxt(filename, delimiter=", ")
        return m

    def get_hamming_distance(self, s1, s2):
        return hamming_distance(s1, s2)

    def get_levenstein_distance(self, s1, s2):
        return levenshtein_distance(s1, s2)

    def get_jaro_similarity(self, s1, s2):
        return jaro_similarity(s1, s2)

    def get_jaro_winkler_similarity(self, s1, s2):
        return jaro_winkler_similarity(s1, s2)

    def get_damerau_levenshtein_distance(self, s1, s2):
        return damerau_levenshtein_distance(s1, s2)

    def get_match_rating_comparison(self, s1, s2):
        return match_rating_comparison(s1, s2)

    def matrix_hamming_distance(self):
        matrix = self.init_matrix()
        for i in self.sequences:
            line_list = np.array([])
            for j in self.sequences:
                line_list = np.append(line_list, self.get_hamming_distance(i, j))
            matrix = np.vstack([matrix, line_list])
            np.delete(line_list, 0, 0)
        return matrix

    def matrix_levenstein_distance(self):
        print("Levenstein-Distance Calculating...")
        s_counter = 0
        matrix = self.init_matrix()
        for i in self.sequences:
            s_counter = s_counter+1
            line_list = np.array([])
            for j in self.sequences:
                line_list = np.append(line_list, self.get_levenstein_distance(i, j))
            matrix = np.vstack([matrix, line_list])
            np.delete(line_list, 0, 0)
        return matrix

    def matrix_jaro_similarity(self):
        print("jaro-similarity Calculating...")
        matrix = self.init_matrix()
        for i in self.sequences:
            print("Seq...")
            line_list = np.array([])
            for j in self.sequences:
                line_list = np.append(line_list, self.get_jaro_similarity(i, j))
            matrix = np.vstack([matrix, line_list])
            np.delete(line_list, 0, 0)
        return matrix

    def matrix_jaro_winkler_similarity(self):
        print("jaro-winkler Calculating...")
        matrix = self.init_matrix()
        for i in self.sequences:
            line_list = np.array([])
            print(".")
            for j in self.sequences:
                line_list = np.append(line_list, self.get_jaro_winkler_similarity(i, j))
            matrix = np.vstack([matrix, line_list])
            np.delete(line_list, 0, 0)
        return matrix

    def matrix_damerau_levenshtein_distance(self):
        print("damerau-Levenstein Calculating...")
        matrix = self.init_matrix()
        for i in self.sequences:
            line_list = np.array([])
            print(".")
            for j in self.sequences:
                line_list = np.append(line_list, self.get_damerau_levenshtein_distance(i, j))
            matrix = np.vstack([matrix, line_list])
            np.delete(line_list, 0, 0)
        return matrix

    def matrix_match_rating_comparison(self):
        print("match rating calc...")
        matrix = self.init_matrix()
        for i in self.sequences:
            line_list = np.array([])
            for j in self.sequences:
                line_list = np.append(line_list, self.get_match_rating_comparison(i, j))
            matrix = np.vstack([matrix, line_list])
            np.delete(line_list, 0, 0)
        return matrix



#Usage
"""
distance_matrix = Distance("..\DataReader\DATA\Testdata1.csv")
hamming_matrix = distance_matrix.matrix_hamming_distance()
print(hamming_matrix)
#distance_matrix.save_matrix("test.csv", hamming_matrix)
"""