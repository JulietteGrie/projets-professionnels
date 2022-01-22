# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:32:42 2021

@author: Juliette
"""

import pandas as pd
import ezodf
from scipy.spatial.distance import dplist

coordonnees = ezodf.opendoc('coordonnées génération matrice distance.ods')

sheet = coordonnees.sheets[0]
df_dict = {}
for i, row in enumerate(sheet.rows()):
    if i == 0:
        df_dict = {cell.value:[] for cell in row}
        col_index = {j:cell.value for j, cell in enumerate(row)}
        continue
    for j, cell in enumerate(row):
        df_dict[col_index[j]].append(cell.value)

df = pd.DataFrame(df_dict)

matrice_distance = dp.DataFrame(dplist(df_dict))