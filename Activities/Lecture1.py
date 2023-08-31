import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Co2 Emission Data Set
path = '/Users/eitanaka/Documents/GW_Univ/FA2023/DATS6313_Time_Series_Analysis/CO2_1970-2015_dataset_of_CO2_report_2016.xls'
df = pd.read_excel(path, header = [11], index_col=0, squeeze = True)
print(df.head())

Co2_ge = df.loc['Germany']
Co2_ma = df.loc['Malaysia']
year = np.arange(1970, 2016)

plt.figure()
plt.plot(year, Co2_ge, label = 'Germany', lw = 3)
plt.plot(year,Co2_ma, label ='Manaysia', lw=3)
plt.xlabel('Date')
plt.ylabel('Co2 - emission level')
plt.title('Co2 emission')
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

Euro = ['Estonia', 'France', 'Germany', 'Hungary', 'Italy', 'Russian Federation', 'Spain', 'Sweden','United Kingdom']

Co2_EU = df.loc[Euro, :]
Co2_EU.loc['year'] = year
Co2_EU.T.plot(x = 'year', legend=None)
plt.legend(Euro)
plt.xlabel('Date')
plt.ylabel('Co2 - Emission Level')
plt.title('Co2 emission')
plt.tight_layout()
plt.show()

Asean = ["Brunei Darussalam", "Cambodia", "Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand"]
Co2_Asean = df.loc[Asean, :]
Co2_Asean.loc['year'] = year
Co2_Asean.T.plot(x = 'year', legend=None)
plt.legend(Asean)
plt.xlabel('Date')
plt.ylabel('Co2 - Emission Level')
plt.title('Co2 emission')
plt.show()

plt.tight_layout()