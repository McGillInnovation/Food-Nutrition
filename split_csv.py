#!/usr/bin/python
from __future__ import division
import pandas as pd

# # Read the file
# data = pd.read_csv("../database_revised.csv", low_memory=False)

# numrows = 33400 #number of rows threshold to be 5 GB
# count = 0 #keep track of chunks
# chunkrows = 10000 #read 100k rows at a time
# df = pd.read_csv("../database_revised.csv", iterator=True, chunksize=chunkrows, low_memory=False)
# for chunk in df: #for each 100k rows
#     if count <= numrows/chunkrows: #if 5GB threshold has not been reached
#         outname = "database_revised_1.csv"
#     else:
#         outname = "database_revised_2.csv"
#     #append each output to same csv, using no header
#     chunk.to_csv(outname, mode='a', header=None, index=None)
#     count+=1

data = pd.read_csv("database_revised_1.csv", low_memory=False)
# assign a column with unique values as the index of the dataframe
df2 = data.set_index("product_name")

# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See which headers are available
print(list(data))
