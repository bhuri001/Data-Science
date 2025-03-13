import numpy as np
import pandas as pd

# PART 1 - "Numpy"
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# 1. Two custom numpy arrays A and B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

# 2. Common elements between A and B
common_elements = np.intersect1d(A, B)

# 3. Numbers from A within a specific range
filtered_A = A[(A >= 2) & (A <= 5)]

# 4. Rows of iris where petal_length > 1.5 and sepal_length < 5.0
filtered_iris = iris[(iris[:, 2] > 1.5) & (iris[:, 0] < 5.0)]

# Part 2 - Pandas
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# 1. Filtering 'Manufacturer', 'Model', and 'Type' for every 20th row starting from 1st
filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]

# 2. Replacing missing values in Min.Price and Max.Price columns with their respective mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

# 3. Get rows of a dataframe where row sum > 100
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_sum_gt_100 = df_random[df_random.sum(axis=1) > 100]

# Displaying results
print("Vertical Stack:\n", vertical_stack)
print("Horizontal Stack:\n", horizontal_stack)
print("Common Elements:\n", common_elements)
print("Filtered A:\n", filtered_A)
print("Filtered Iris Data:\n", filtered_iris)
print("Filtered DF:\n", filtered_df)
print("Updated DF with Mean Replacement:\n", df[['Min.Price', 'Max.Price']].head())
print("Rows with sum > 100:\n", rows_sum_gt_100)