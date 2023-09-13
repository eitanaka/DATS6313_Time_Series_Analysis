from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def Cal_rolling_mean_var(df, feature, window=1):
    """
    Calculate the rolling mean and rolling variance
    :param df: the time series data
    :param feature: variable name
    :param window: window size
    :return: list of rolling mean and rolling variance
    """
    x = df[feature]
    mean_list = []
    var_list = []
    for i in range(1, len(df) + 1):
        mean = x[:i].mean()
        if i == 1:
            var = 0
        else:
            var = x[:i].var()
        mean_list.append(mean)
        var_list.append(var)
    return mean_list, var_list

def plot_rolling_mean_var(df, feature, window=1):
    """
    Plot the rolling mean and rolling variance
    :param df: time series data
    :param feature: feature name
    :param window: windon size
    :return: None
    """
    mean_list, var_list = Cal_rolling_mean_var(df, feature, window)
    samples_mean = np.linspace(1, len(mean_list), len(mean_list))
    samples_var = np.linspace(1, len(var_list), len(var_list))
    fig, ax = plt.subplots(figsize=(12, 6), nrows=2, ncols=1)
    ax[0].plot(samples_mean, mean_list, label='Rolling Mean')
    ax[0].set_xlabel('Samples')
    ax[0].set_ylabel('Magnitude')
    ax[0].set_title(f'Rolling Mean - {feature}')
    ax[0].grid()
    ax[0].legend()
    ax[1].plot(samples_var, var_list, label='Rolling Variance')
    ax[1].set_xlabel('Samples')
    ax[1].set_ylabel('Magnitude')
    ax[1].set_title(f'Rolling Variance - {feature}')
    ax[1].grid()
    ax[1].legend()
    plt.tight_layout()
    plt.show()

