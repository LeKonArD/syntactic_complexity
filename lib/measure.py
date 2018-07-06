import pandas as pd
import numpy as np
from collections import Counter
import os
import re


tagset =[ "ADJA","ADJD","ADV","APPR","APPRART","APPO","APZR","ART","CARD","FM","ITJ","KOUI","KOUS","KON","KOKOM","NN",
          "NE","PDS","PDAT","PIS","PIAT","PIDAT","PPER","PPOSS"
,"PPOSAT" ,"PRELS","PRELAT","PRF","PWS","PWAT","PWAV","PAV","PTKZU","PTKNEG","PTKVZ","PTKANT","PTKA","TRUNC","VVFIN",
          "VVIMP"
,"VVINF","VVPP","VAFIN","VAIMP","VAINF","VAPP","VMFIN","VMINF","VMPP","XY","$,","$.","$("]


def helper_get_filepaths(path, file_ending=".csv"):

    files = list()
    for path, sub_dirs, file_names in os.walk(path):
        for filename in file_names:
            if filename.endswith(file_ending):
                files.append(os.path.join(path, filename))
    files.sort()

    return files

def read_input(filename, sep="\t"):

    data = pd.read_csv(filename, sep=sep, header=0)

    return data

def chunks(input_array, window_size):
    for i in range(0, len(input_array), window_size):
        yield input_array[i:i+window_size]

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

def create_pos_trigrams(data, window, tagset):

    pos = list(chunks(np.array(data["pos_tt"]), window))
    trigrams = [Counter(list(find_ngrams(wind, 3))) for wind in pos]
    permut_pos = Counter(list(find_ngrams(tagset, 3)))

    framed_trigrams = pd.DataFrame(columns=permut_pos)
    print(framed_trigrams)
    for tri in trigrams:
        framed_trigrams = framed_trigrams.append(pd.DataFrame.from_dict(tri, orient="index").transpose())
    framed_trigrams = framed_trigrams.fillna(0)




files = helper_get_filepaths("/media/konle/3d665f71-096f-4974-8ef9-b365f5f16389/token_exp/out_spacy", ".tsv")

for filename in files[1:2]:
    data = read_input(filename, "\t")
    create_pos_trigrams(data, 300, tagset)
