import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append(r'C:\GW\Time series Analysis\toolbox')
from toolbox import Plot_Rolling_Mean_Var, ADF_Cal, kpss_test, difference

name = 'CO2_1970-2015_dataset_of_CO2_report_2016.xls'
df = pd.read_excel(name, header = [0],
                   index_col = 0,
                   squeeze = True)
print(df.head())
Co2_ge = df.loc['Germany']
Co2_ma = df.loc['Malaysia']
year = np.arange(1970, 2016)

plt.figure()
plt.plot(year,Co2_ge, label = 'Germany', lw = 3)
plt.plot(year,Co2_ma, label = 'Malaysia', lw = 3)
plt.xlabel('Date')
plt.ylabel('Co2- emission level')
plt.title('co2 emission')
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()
Euro = ['Estonia','France', 'Germany', 'Hungary',
        'Italy', 'Russian Federation', 'Spain',
        'Sweden','United Kingdom']
CO2 = df.loc[Euro, :]
CO2.loc['year'] = year
CO2.T.plot(x = 'year', legend = None)
plt.legend(Euro)
plt.xlabel('Date')
plt.ylabel('Co2- emission level')
plt.title('Euro co2 emission')
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

ASEAN = ['Brunei Darussalam','Cambodia',
         'Lao People s Democratic Republic',
         'Malaysia', 'Myanmar', 'Singapore',
         'Thailand', 'Viet Nam']
CO2 = df.loc[ASEAN, :]
CO2.loc['year'] = year
CO2.T.plot(x = 'year', legend = None)
plt.legend(ASEAN)
plt.xlabel('Date')
plt.ylabel('Co2- emission level')
plt.title('ASEAN co2 emission')
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()


Plot_Rolling_Mean_Var(Co2_ma, 'Malaysia')
ADF_Cal(Co2_ma)

Co2_ma_diff = difference(Co2_ma)
ADF_Cal(Co2_ma_diff)
Co2_ma_diff_diff = difference(Co2_ma_diff)
ADF_Cal(Co2_ma_diff_diff)

import numpy as np
x = np.random.normal(0,1,1000)
plt.figure()
plt.plot(x)
plt.show()