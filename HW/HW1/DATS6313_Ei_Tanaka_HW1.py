"""
Author: Ei Tanaka
Date: Sepetember 20, 2023
Purpose: Homework 1
"""

# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# =====================================================================================================
# Question 1
# Write a python function called “correlation_coefficent_cal(x,y)” that implements the correlation
# coefficient between random variable x and y. The formula for correlation coefficient is given
# below. The function should be written in a general form that can work for any dataset x and
# dataset y. The return value for this function is r. Test the developed code with the following makeup dataset for x, y, z, h & g.
# a. The correlation coefficient between x and y. Display the answer on the console.
# b. The correlation coefficient between x and z. Display the answer on the console.
# c. The correlation coefficient between g and h. Display the answer on the console.
# Verify a, b and c using a python program.
# =====================================================================================================
def correlation_coefficent_cal(x, y):
    """
    Calculate the correlation coefficient between x and y
    :param x: list
    :param y: list
    :return: correlation coefficient
    """
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    return np.sum((x - x_mean) * (y - y_mean)) / np.sqrt(np.sum((x - x_mean) ** 2) * np.sum((y - y_mean) ** 2))

x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = [-1,-2,-3,-4,-5]
g = [1,1,0,-1,-1,0,1]
h = [0,1,1,1,-1,-1,-1]

print("Correlation coefficient between x and y: ", round(correlation_coefficent_cal(x, y), 2))
print("Correlation coefficient between x and z: ", round(correlation_coefficent_cal(x, z), 2))
print("Correlation coefficient between g and h: ", round(correlation_coefficent_cal(g, h), 2))

# =====================================================================================================
# Question 2
# Hand Writing Stuff
# =====================================================================================================

# =====================================================================================================
# Question 3
# Load the time series data called tute1.csv from the course GitHub.
# Graph the scatter plot between Sales & GDP
# Calculate the correlation coefficient between Sales and GDP [using the developed code in question 1] and update the graph title between calculated correlation coefficients.
# Update the x and y axis with an appropriate label.
# Does the calculated correlation coefficient make sense with respect to the scatter plot? Justify your answer.
# =====================================================================================================
url = "https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv"
df = pd.read_csv(url)

# Graph the scatter plot between Sales & GDP
plt.figure(figsize=(12, 6))
plt.scatter(df['GDP'], df['Sales'], color='blue', alpha=0.5)
plt.xlabel('GDP')
plt.ylabel('Sales')
plt.title('Scatter Plot between Sales & GDP: correlation coefficient = ' + str(round(correlation_coefficent_cal(df['GDP'], df['Sales']), 2)))
plt.show()

# =====================================================================================================
# Question 4
# Graph the scatter plot between Sales and AdBudget.
# Calculate the correlation coefficient between Sales and AdBudget [using the developed code in question 1] and update the graph title between
# calculated correlation coefficients.
# Update the x and y axis with an appropriate label.
# Does the calculated correlation coefficient make sense with respect to the scatter plot?
# Justify your answer.
# =====================================================================================================
plt.figure(figsize=(12, 6))
plt.scatter(df['AdBudget'], df['Sales'], color='blue', alpha=0.5)
plt.xlabel('AdBudget')
plt.ylabel('Sales')
plt.title('Scatter Plot between Sales & AdBudget: correlation coefficient = ' + str(round(correlation_coefficent_cal(df['AdBudget'], df['Sales']), 2)))
plt.show()

# =====================================================================================================
# Question 5
# Graph the scatter plot between GDP & AdBudget. Calculate the correlation coefficient between
# GDP & AdBudget [using the developed code in question 1] and update the graph title between
# calculated correlation coefficients. Update the x and y axis with an appropriate label. Does the
# calculated correlation coefficient make sense with respect to the scatter plot? Justify your answer.
# =====================================================================================================
plt.figure(figsize=(12, 6))
plt.scatter(df['GDP'], df['AdBudget'], color='blue', alpha=0.5)
plt.xlabel('GDP')
plt.ylabel('AdBudget')
plt.title('Scatter Plot between GDP & AdBudget: correlation coefficient = ' + str(round(correlation_coefficent_cal(df['GDP'], df['AdBudget']), 2)))
plt.show()

# =====================================================================================================
# Question 6
# Using the Seaborn package and pairplot() function, graph the correlation matrix for the tute1.csv
# dataset.
# Plot the Dataframe using the following options. Explain the graphs and justify the cross
# correlations.
# a. kind="kde"
# b. kind="hist"
# c. diag_kind="hist"
# =====================================================================================================
# a. kind="kde"
plt.figure(figsize=(12, 6))
sns.pairplot(df, kind="kde")
plt.show()

# b. kind="hist"
plt.figure(figsize=(12, 6))
sns.pairplot(df, kind="hist")
plt.show()

# c. diag_kind="hist"
plt.figure(figsize=(12, 6))
sns.pairplot(df, diag_kind="hist")
plt.show()

# =====================================================================================================
# Question 7
# Using the Seaborn package and heatmap() function, graph the correlation matrix for the tute1.csv
# dataset. Explain the depicted correlation matrix.
# =====================================================================================================
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True)
plt.show()

# =====================================================================================================
# Question 8
# Develop a python program that asks a user to input numerical numbers: mean, variance & number
# of observations [default values : mean = 0, variance = 1, observations = 1000].
# Then generates a random variable x that is normally distributed with above statistics. Create the following random
# variables:
# a. 𝑦 = 𝑥**2
# b. 𝑧 = 𝑥**3

# Using the developed code in question 1 calculate the following correlation coefficients:
# • The correlation coefficient between x & y. Display the answer on the console.
# • The correlation coefficient between x & z. Display the answer on the console.
# • Justify your answer to the above questions using the plot of x versus y and z.
# • Are x and y independent? Are x & y correlated? Justify your answer.
# • Are x and z independent? Are x & z correlated? Justify your answer.
# =====================================================================================================

mean = float(input("Enter mean: "))
variance = float(input("Enter variance: "))
observations = int(input("Enter number of observations: "))
x = np.random.normal(mean, variance, observations)
y = x ** 2
z = x ** 3

print("Correlation coefficient between x and y: ", round(correlation_coefficent_cal(x, y), 2))
print("Correlation coefficient between x and z: ", round(correlation_coefficent_cal(x, z), 2))

# plot of x versus y
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot between x & y: correlation coefficient = ' + str(round(correlation_coefficent_cal(x, y), 2)))
plt.show()

# plot of x versus z
plt.figure(figsize=(12, 6))
plt.scatter(x, z, color='blue', alpha=0.5)
plt.xlabel('x')
plt.ylabel('z')
plt.title('Scatter Plot between x & z: correlation coefficient = ' + str(round(correlation_coefficent_cal(x, z), 2)))
plt.show()

