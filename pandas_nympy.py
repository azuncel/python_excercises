import numpy as np
import pandas as pd

#list with numpy
list = [1,2,3,4]
array = np.array(list)
print(array)

#Matriz
double_list = [[1,2,3],[4,5,6]]
array_2 = np.array(double_list)
print(array_2)

#Modify
numbers = np.array([10,22,33,44])
print(numbers - 2)

#Series in pandas
weight = np.array([43,35,29])
series1 = pd.Series(weight)
print(series1)