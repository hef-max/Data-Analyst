import numpy as np
import pandas as pd
import os



tabel_1 = pd.read_excel('sclube.xlsx', sheet_name='Table 1')
tabel_2 = pd.read_excel('sclube.xlsx', sheet_name='Table 2')
tabel_3 = pd.read_excel('sclube.xlsx', sheet_name='Table 3')
tabel_4 = pd.read_excel('sclube.xlsx', sheet_name='Table 4')
tabel_5 = pd.read_excel('sclube.xlsx', sheet_name='Table 5')
tabel_6 = pd.read_excel('sclube.xlsx', sheet_name='Table 6')
tabel_7 = pd.read_excel('sclube.xlsx', sheet_name='Table 7')
tabel_8 = pd.read_excel('sclube.xlsx', sheet_name='Table 8')
tabel_9 = pd.read_excel('sclube.xlsx', sheet_name='Table 9')
tabel_10 = pd.read_excel('sclube.xlsx', sheet_name='Table 10')
tabel_11 = pd.read_excel('sclube.xlsx', sheet_name='Table 11')
tabel_12 = pd.read_excel('sclube.xlsx', sheet_name='Table 12')
tabel_13 = pd.read_excel('sclube.xlsx', sheet_name='Table 13')
tabel_14 = pd.read_excel('sclube.xlsx', sheet_name='Table 14')
tabel_15 = pd.read_excel('sclube.xlsx', sheet_name='Table 15')
tabel_16 = pd.read_excel('sclube.xlsx', sheet_name='Table 16')
tabel_17 = pd.read_excel('sclube.xlsx', sheet_name='Table 17')
tabel_18 = pd.read_excel('sclube.xlsx', sheet_name='Table 18')
tabel_19 = pd.read_excel('sclube.xlsx', sheet_name='Table 19')
tabel_20 = pd.read_excel('sclube.xlsx', sheet_name='Table 20')
tabel_21 = pd.read_excel('sclube.xlsx', sheet_name='Table 21')
tabel_22 = pd.read_excel('sclube.xlsx', sheet_name='Table 22')
tabel_23 = pd.read_excel('sclube.xlsx', sheet_name='Table 23')
tabel_24 = pd.read_excel('sclube.xlsx', sheet_name='Table 24')
tabel_25 = pd.read_excel('sclube.xlsx', sheet_name='Table 25')
tabel_26 = pd.read_excel('sclube.xlsx', sheet_name='Table 26')
tabel_27 = pd.read_excel('sclube.xlsx', sheet_name='Table 27')
tabel_28 = pd.read_excel('sclube.xlsx', sheet_name='Table 28')
tabel_29 = pd.read_excel('sclube.xlsx', sheet_name='Table 29')
tabel_30 = pd.read_excel('sclube.xlsx', sheet_name='Table 30')

data = [tabel_2, tabel_3, tabel_4, tabel_5,
 tabel_6, tabel_7, tabel_8, tabel_9, tabel_10,
 tabel_11, tabel_12, tabel_13, tabel_14, tabel_15, 
 tabel_16, tabel_17, tabel_18, tabel_19, tabel_20,
 tabel_21, tabel_22, tabel_23, tabel_24, tabel_25,
 tabel_26, tabel_27, tabel_28, tabel_29, tabel_30]

df = pd.DataFrame(data=data, columns=['data'], dtype=object)
print(df)