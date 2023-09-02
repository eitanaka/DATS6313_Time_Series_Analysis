"""
Name: Ei Tanaka
StudenID: G24454239
Class: DATS 6313-10 Time Series Analysis
Purpose: Lab 1 Stationary & Non-Stationary
"""

# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import sys

# !!!! Please change the path to your local path
sys.path.append(r'/Users/eitanaka/Documents/GW_Univ/FA2023/DATS6313_Time_Series_Analysis/DATS6313_Time_Series_Analysis/toolbox.py')
from toolbox import ADF_Cal, kpss_test, Cal_rolling_mean_var, plot_rolling_statistics

# =====================================================================================================
# Question 1 Load the data set & Plot Sales, AdBudget and GPD versus time step in one graph.
# =====================================================================================================
# Load the data set
url = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv'
df = pd.read_csv(url, index_col=0, parse_dates=True)

# Plot Sales, AdBudget and GPD versus time step in one graph.
def plot_data(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['Sales'], label='Sales')
    ax.plot(df.index, df['AdBudget'], label='AdBudget')
    ax.plot(df.index, df['GDP'], label='GDP')
    ax.set_xlabel('Date')
    ax.set_ylabel('USD($)')
    ax.set_title('Sales, AdBudget, GDP versus time step')
    ax.grid()
    ax.legend()
    plt.tight_layout()
    plt.show()

plot_data(df)

# =========================================================================================================================
# Question 2
# Find the time series statistics (average, variance, standard deviation, median) of Sales, AdBudget and GPD
# and display the Average, variance, and standard deviation.
# =========================================================================================================================
def display_statistics(df):
    print('The Sales mean is : {:.2f} and the variance is : {:.2f} with standard deviation : {:.2f} median: {:.2f}'.format(df['Sales'].mean(), df['Sales'].var(), df['Sales'].std(), df['Sales'].median()))
    print('The AdBudget mean is : {:.2f} and the variance is : {:.2f} with standard deviation : {:.2f} median: {:.2f}'.format(df['AdBudget'].mean(), df['AdBudget'].var(), df['AdBudget'].std(), df['AdBudget'].median()))
    print('The GDP mean is : {:.2f} and the variance is : {:.2f} with standard deviation : {:.2f} median: {:.2f}'.format(df['GDP'].mean(), df['GDP'].var(), df['GDP'].std(), df['GDP'].median()))

display_statistics(df)

# =========================================================================================================================
# Question 3
# Prove that the Sales, AdBudget and GDP in this time series dataset is stationary.
# You need to plot the rolling mean and rolling variance in one graph using subplot [2x1] by creating a loop over the number of samples in the dataset and calculate the means & variances versus time.
#
# =========================================================================================================================

# Plot the rolling mean and rolling variance
plot_rolling_statistics(df['Sales'])
plot_rolling_statistics(df['AdBudget'])
plot_rolling_statistics(df['GDP'])

# =========================================================================================================================
# Question 5
# Perform an ADF-test to check if the Sales, AdBudget and GDP are stationary.
# =========================================================================================================================
# ADF test
ADF_Cal(df['Sales'])
ADF_Cal(df['AdBudget'])
ADF_Cal(df['GDP'])

# =========================================================================================================================
# Question 6
# Perform a KPSS-test to check if the Sales, AdBudget and GDP are stationary.
# =========================================================================================================================
# KPSS test
kpss_test(df['Sales'])
kpss_test(df['AdBudget'])
kpss_test(df['GDP'])

# =========================================================================================================================
# Question 7
# Repeat step 1-6 with "AirPassengers.csv" dataset.
# =========================================================================================================================
url2 = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/AirPassengers.csv'
df2 = pd.read_csv(url2, index_col=0, parse_dates=True)

# Plot passengers versus time step in one graph.
plt.figure(figsize=(12, 6))
plt.plot(df2.index, df2['#Passengers'])
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.title('Passengers versus time step')
plt.grid()
plt.tight_layout()
plt.show()

# Find the time series statistics (average, variance, standard deviation, median) of passengers and display the Average, variance, and standard deviation.
print('The passengers mean is : {:.2f} and the variance is : {:.2f} with standard deviation : {:.2f} median: {:.2f}'.format(df2['#Passengers'].mean(), df2['#Passengers'].var(), df2['#Passengers'].std(), df2['#Passengers'].median()))

# Plot the rolling mean and rolling variance

# ADF test
ADF_Cal(df2['#Passengers'])

# KPSS test
kpss_test(df2['#Passengers'])

# =========================================================================================================================
# Question 8
# 8.a Performs a 1st order non-seasonal differencing on the #Passengers time series and plot the differenced time series.
# 8.b Performs a 2nd order non-seasonal differencing on the #Passengers time series and plot the differenced time series.
# 8.c Performs a 3rd order non-seasonal differencing on the #Passengers time series and plot the differenced time series.
# 8.d Performs a log transformation followed by a 1st order non-seasonal differencing on the #Passengers time series and plot the rolling mean and rolling variance.
# 8.e Performs ADF-test and KPSS-test on the transformed dataset and display the result on the console.
# =========================================================================================================================
# 8.a Performs a 1st order non-seasonal differencing on the #Passengers time series and plot the differenced time series.
