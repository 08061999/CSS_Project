# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:06:28 2024

@author: user
"""

import pandas as pd

df = pd.read_csv("C:/Users/user/Desktop/css2024_project/css2024_project/movie_dataset.csv")

print(df)


x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True) 


x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True) 

print(df.describe())

print(df["Rating"] > 8.0)

import matplotlib.pyplot as plt

x_bar = df["Year"]
y_bar = df["Revenue (Millions)"]

plt.bar(x_bar, y_bar)

plt.show()

x_bar = df["Year"]
y_bar = df["Rating"]

plt.bar(x_bar, y_bar)

plt.show()

x_line = df["Rank"]
y_line = df["Rating"]

plt.plot(x_line, y_line)

plt.show()


print(['Rating'].str('2016').mean())






