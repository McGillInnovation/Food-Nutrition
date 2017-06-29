#!/usr/bin/python

from pandas import read_excel,merge
from numpy import arange
import numpy as np
from numpy import *
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',1000)
from sklearn.datasets import load_iris
def test_this(a):

    if isnan(a) == True:
        print a
        print '\n\nThis is not an accepted type of input for A\n\n'
        raise ValueError
    # else:
        # print "Yep,that's a number"



def clustering():

    df = pd.read_excel('C:\Users\Admin\/afoodproject\datasetbest.xlsx')
    # print list(df)

    names = df['food_Name']
    # print list(df)
    mylist = [ u'Weight = 100g', u'Energy(kcal)_for_100g', u'Energy (kJ) for 100g', u'Protein(g)_for_100g', u'Carbohydrate (g) for 100 g', u'Total Sugar (g) for 100g',  u'Total Dietary Fibre (g) for 100g', u'Total Fat (g) for 100g', u'Saturated Fat (g) for 100g', u'Cholesterol (mg) for 100g', u'Calcium (mg) for 100g', u'Iron (mg) for 100g', u'Sodium (mg) for 100g ', u'Potassium (mg) for 100g ', u'Magnesium (mg)  for 100g ', u'Phosphorus (mg) for 100g ', u'Thiamin (mg) for 100g ', u'Riboflavin (mg)  for 100g ', u'Niacin (NE) for 100g ', u'Folate (DFE)  for 100g ']
    features = df[mylist]

    # features = df.drop(labels='food_Name', axis=1)

    # print features

    arr = np.array(features)
    arr = np.clip(arr,0,np.finfo(np.float64).max)
    arr = np.nan_to_num(arr)
#do loop change value of 1 in x and  and change the 0:2 to a list with the indeces of the columns
    # print arr[:,:].dtype
    # print(arr.min())
    columnx=1 #is our base in kcal
    columny=15# 3proteins 4 carbs 5 sugar 6fiber
    # 7 fat 8satfat 9choleserol 10 calcium
    # 11iron #12sodium 13 potassium 14magnesium
    # 15 phosphorus


    x = arr[:,columnx]
    # print x
    y = arr[:,columny]
    # print y

    kmeans = KMeans(n_clusters=3, max_iter=2000)
    labels = kmeans.fit_predict(arr) # same size array of which cluster index is in
    ##text=List of strings to be written to file
    print type(labels)

    print labels
    this= list(labels)
    print this
    with open('csvfile.csv', 'wb') as file:
        for i in range(0,1071):
            file.write(str(this[i]))
            file.write('\n')
    thecolumns=[columnx,columny]
    centers = kmeans.cluster_centers_[:,thecolumns]


    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    scatter = ax.scatter(x, y, c=labels, s=50)
    for i, j in centers:
        ax.scatter(i, j, s=50, c='red', marker='+')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.colorbar(scatter)

    # plt.xlim(0,10)
    fig.savefig('plot.png',dpi = 400)

    # fig.show()
