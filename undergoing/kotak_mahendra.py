import csv

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

csv_file = open("C:\\Users\\saimanoj\\Downloads\\data.csv")
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)

x_data = []
y_data = []

for x in csv_data:
    x_data.append(x[0])
    y_data.append(x[1])

plt.scatter(x_data, y_data)

regr = linear_model.LinearRegression()

x_data = np.array(x_data, ndmin=2)

regr.fit(x_data, y_data)

print("trained")

print(x_data, y_data)

y_data = regr.predict(x_data)

print("values re-generated")

plt.plot(x_data, y_data)

plt.show()
