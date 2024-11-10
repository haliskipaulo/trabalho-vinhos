import numpy as np
import pandas as pd

FixedAcidity = pd.read_csv('winequality-red.csv', usecols=[0], skiprows=1)
FixedAcidity = np.array(FixedAcidity)
FixedAcidity = np.transpose(FixedAcidity)

VolatileAcidity = pd.read_csv('winequality-red.csv', usecols=[1], skiprows=1)
VolatileAcidity = np.array(VolatileAcidity)
VolatileAcidity = np.transpose(VolatileAcidity)

CitricAcid = pd.read_csv('winequality-red.csv', usecols=[2], skiprows=1)
CitricAcid = np.array(CitricAcid)
CitricAcid = np.transpose(CitricAcid)

ResidualSugar = pd.read_csv('winequality-red.csv', usecols=[3], skiprows=1)
ResidualSugar = np.array(ResidualSugar)
ResidualSugar = np.transpose(ResidualSugar)

Chlorides = pd.read_csv('winequality-red.csv', usecols=[4], skiprows=1)
Chlorides = np.array(Chlorides)
Chlorides = np.transpose(Chlorides)

FreeSulfurDioxide = pd.read_csv('winequality-red.csv', usecols=[5], skiprows=1)
FreeSulfurDioxide = np.array(FreeSulfurDioxide)
FreeSulfurDioxide = np.transpose(FreeSulfurDioxide)

TotalSulfurDioxide = pd.read_csv('winequality-red.csv', usecols=[6], skiprows=1)
TotalSulfurDioxide = np.array(TotalSulfurDioxide)
TotalSulfurDioxide = np.transpose(TotalSulfurDioxide)

Density = pd.read_csv('winequality-red.csv', usecols=[7], skiprows=1)
Density = np.array(Density)
Density = np.transpose(Density)

pH = pd.read_csv('winequality-red.csv', usecols=[8], skiprows=1)
pH = np.array(pH)
pH = np.transpose(pH)

Sulphates = pd.read_csv('winequality-red.csv', usecols=[9], skiprows=1)
Sulphates = np.array(Sulphates)
Sulphates = np.transpose(Sulphates)

Alcohol = pd.read_csv('winequality-red.csv', usecols=[10], skiprows=1)
Alcohol = np.array(Alcohol)
Alcohol = np.transpose(Alcohol)

Quality = pd.read_csv('winequality-red.csv', usecols=[11], skiprows=1)
Quality = np.array(Quality)
Quality = np.transpose(Quality)

# Entrada do perceptron
X = np.vstack((FixedAcidity, VolatileAcidity, CitricAcid, ResidualSugar, 
               Chlorides, FreeSulfurDioxide, TotalSulfurDioxide, Density, 
               pH, Sulphates, Alcohol, Quality))
