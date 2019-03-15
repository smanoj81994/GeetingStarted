# -*- coding: utf-8 -*-
"""
Owner: Manoj

Basics of python & pandas
"""


import os
import numpy as np
import pandas as pd


# Getting current working directory
os.getcwd()

# Changing the working directory
os.chdir("G:/Datasets/Titanic/")

# Listing whats in the directory
files=os.listdir()

# A numpy array
array=[1,2,3,4,5,6]
ZeroArray = np.zeros(10)



############################################# Pandas ###############################


# Defining a dataframe
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)


# Shape of the dataframe
df.shape

# Column names
df.columns

# Select a particular column
df[['one','two']]


# Summary of the dataset
df.describe()

# Some basic opertions on the columns
df['one'].max()









