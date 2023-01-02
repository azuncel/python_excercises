import numpy as np
import pandas as pd

#PANDAS https://pandas.pydata.org/docs/user_guide/10min.html


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

#Put index in series
weight = np.array([43,35,29])
series2 = pd.Series(weight,index=['Emily', 'Azucena', 'Arely'])
print(series2)

#DataFrame
data_frame = pd.DataFrame([
    ['Emily','Crisantemos 1',33],
    ['Azu', 'Crisantemos 2',13],
    ['Arely', 'Crisantemos 3',40]
    ],
    columns=['name','address','age'])

data_frame.set_index('name')
print(data_frame)


# Creating a Pandas DataFrame
# Passing in a dictionary:
data = {'name':['Azucena', 'Emily'],
'age':[30, 28]}
df1 = pd.DataFrame(data)
# Passing in a list of lists:
data = [['Azu', 20], ['Emily', 30],
['Arely', 25]]
df2 = pd.DataFrame(data, columns = ['Name',
'Age'])
# Reading data from a csv file:
df3 = pd.read_csv('insurance.csv')
print(df3)

# Specifying each value in the new column:
df1['nums'] = [1, 2]
# Setting each row in the new column to the same value:
df1['same_value'] = 1
# Creating a new column by doing a calculation on an existing column:
df1['calc_another_column'] = df1['nums'] * 5

print(df1)




# This function doubles the input value
def triple(x):
 return 3*x
# Apply this function
df3.bmi = df3.bmi.apply(triple)
# Lambda functions
df3.charges = df3.charges.apply(lambda x : round(x, 2))
print(df3)
# Applying to a row requires it to be called on the entire DataFrame
df3['bmixcharges'] = df3.apply(lambda row: round(row['bmi'] * row['charges'], 2), axis=1)
print(df3)


#Inspect DataFrame
print(df3.head())
print(df3.tail())
print(df3.info())