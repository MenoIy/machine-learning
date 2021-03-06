# -*- coding: utf-8 -*-
"""Digitreco.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UBmiffjfIEjwApufHK6QATBQtU3YXld0
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model, preprocessing, tree , model_selection
import warnings
from sklearn.ensemble.forest import RandomForestClassifier

path = './drive/My Drive/'
list = os.listdir(path)
df = pd.read_csv(path + list[-1])
df.head()

path = './drive/My Drive/Digit recognizer/'
list = os.listdir(path)
print(list)
train = pd.read_csv(path + list[1])
test = pd.read_csv(path + list[2])
sub = pd.read_csv(path + list[0])

print(train.shape)
print(train.size)
print(train.head())

from sklearn.utils import shuffle
train = shuffle(train)
from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(train, test_size=0.02380952380)
train_data.to_csv('train.csv',index=False)
#test_data.to_csv('test.csv',index=False)
from google.colab import files
files.download('train.csv')
#files.download('test.csv')
print(train_data.head())
print(train_data.shape)

print(test_data.head())
print(test_data.shape)

data = train.values
cls = tree.DecisionTreeClassifier()
np.random.shuffle(data)
xtrain = data[0:21000, 1:]
train_label = data[0:21000, 0]

xtest = data[21000: ,1:]
test_label = data[21000:,0]

index = 16
cls.fit(xtrain, train_label)
d=xtest[index]
d.shape= (28, 28)
plt.imshow(d, cmap='gray')
plt.show()
print(cls.predict([xtest[index]]))

pre = cls.predict(xtest)
count = 0
for i in range (0, 21000):
    count += 1 if pre[i] == test_label[i] else 0
print("Accuracy", (count / 21000) * 100)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(xtrain, train_label)

pre = rf.predict(xtest)
count = 0
for i in range (len(pre)):
    count += 1 if pre[i] == test_label[i] else 0
print("Accuracy", (count / len(pre)) * 100)

pre = rf.predict(test)
print(pre)
sub.head()
sub.Label = pre

sub.head()
sub.info()
sub.to_csv('submition.csv', index=False)
from google.colab import files
files.download('submition.csv')