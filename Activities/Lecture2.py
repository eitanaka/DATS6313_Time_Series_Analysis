"""
Name: Ei Tanaka
Date: Wednesday, September 6, 2023
Purpose: Lecture 2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

path = "/Users/eitanaka/Documents/GW_Univ/FA2023/DATS6313_Time_Series_Analysis/DATS6313_Time_Series_Analysis/toolbox.py"
sys.path.append(path)

from toolbox import ADF_Cal, kpss_test, Cal_rolling_mean_var, plot_rolling_statistics

"""
Memo:
Visualize Statistic
- Rolling mean
- Rolling variance
- histogram
- ACF / PACF
- Boxplot

Statistical Test
- ADF test N0: non-stationary, N1: stationary
- KPSS test N0: stationary, N1: non-stationary

Error type
- Type I error: False positive (H0)
- Type II error: False negative (H1)
"""