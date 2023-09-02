from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ADF_Cal(x):
    """
    Calculate the Augmented Dickey-Fuller test and print out the result
    :param x:
    :return:
    """
    result = adfuller(x)
    print("ADF Statistic: %f" % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

def kpss_test(timeseries):
    """
    Calculate the KPSS test and print out the result
    :param timeseries: time series data
    :return: None
    """
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c', nlags="auto")
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print (kpss_output)

def Cal_rolling_mean_var(x):
    """
    Calculate the rolling mean and rolling variance
    :param x: time series data
    :return: rolling mean and rolling variance
    """
    rolling_mean = x.rolling(window=1).mean()
    rolling_var = x.rolling(window=1).var()
    return rolling_mean, rolling_var

def plot_rolling_statistics(x):
    """
    Plot the rolling mean and rolling variance separately 2x1
    :param x: time series data
    :return: None
    """
    sample_size = np.arange(0, len(x), 1)
    rolling_mean, rolling_var = Cal_rolling_mean_var(x)
    fig, ax = plt.subplots(2, 1, figsize=(12, 6))
    ax[0].plot(sample_size, x, label='Original')
    ax[0].plot(sample_size, rolling_mean, label='Rolling Mean')
    ax[0].set_xlabel('Sample Size')
    ax[0].set_ylabel('Magnitude')
    ax[0].set_title('Rolling Mean')
    ax[0].grid()
    ax[0].legend()
    ax[1].plot(sample_size, rolling_var, label='Rolling Variance')
    ax[1].set_xlabel('Sample Size')
    ax[1].set_ylabel('Magnitude')
    ax[1].set_title('Rolling Variance')
    ax[1].grid()
    ax[1].legend()
    plt.tight_layout()
    plt.show()

