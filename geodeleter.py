import pandas
import numpy
import csv

data = pandas.read_csv("DICCIONARIO_FINAL_V19.csv", delimiter = ";",dtype=numpy.string_, encoding="UTF-8")
data = data.drop('GPS', 1)
data = data.drop('GPS_LA', 1)
data = data.drop('GPS_LO', 1)
data.to_csv("output.csv",delimiter=",", index=False)
