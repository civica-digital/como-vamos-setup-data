import pandas
import numpy
import csv

f = "DICCIONARIO_FINAL_V19.csv"
e = "UTF-8"
data = pandas.read_csv(f, delimiter = ";",dtype=numpy.string_, encoding=e)
data = data.drop('GPS', 1)
data = data.drop('GPS_LA', 1)
data = data.drop('GPS_LO', 1)
data.to_csv("output_1.csv", delimiter=",",dtype=numpy.string_, quoting=csv.QUOTE_NONNUMERIC, index=False)
