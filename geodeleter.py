import pandas
import numpy

f = "DICCIONARIO_FINAL_V19.csv"
e = "UTF-8"
data = pandas.read_csv(f, delimiter = ";",dtype=numpy.string_, encoding=e)
data = data.drop('GPS', 1)
data = data.drop('GPS_LA', 1)
data = data.drop('GPS_LO', 1)
data.to_csv("output.csv", delimiter=",", index=False)
