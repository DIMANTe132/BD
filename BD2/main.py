import pandas as pd
import matplotlib.pyplot as plt
import seaborn

data = pd.read_csv("CPI_NCYR_COI_RT_A.csv")
data = data[data.classif1 == 'COI_COICOP_CP01T12']
data = data[['ref_area', 'time', 'obs_value']]
print(data)

# 2.1.2
filter = (data.ref_area == 'USA') & (data.time >= 1967) & (data.time <= 1997)
data[filter].plot(x='time', y='obs_value', title='Динамика инфляции в США', kind='bar')
plt.show()

usa_data = data[filter]
usa_data['koef_byd'] = (usa_data.obs_value + 100) / 100
usa_data['koef_byd'] = usa_data.koef_byd.shift(fill_value=1.)
usa_data['koef_1967'] = usa_data.koef_byd.cumprod()
usa_data['million_1967'] = usa_data.koef_1967 * 1e6
usa_data.plot(x='time', y='million_1967')
print('Answer:', usa_data.million_1967.max())
plt.show()

usa_data = usa_data.sort_values(by='time', ascending=False)
usa_data['koef_byd'] = usa_data.koef_byd.shift(fill_value=1.)
usa_data['koef_pro'] = 1 / usa_data.koef_byd
usa_data['koef_1997'] = usa_data.koef_pro.cumprod()
usa_data['one_hundred_billion_1997'] = usa_data.koef_1997 * 1e11
print('Answer:', usa_data.one_hundred_billion_1997.min())
usa_data.plot(x='time', y='one_hundred_billion_1997')
plt.show()

filter = (data.ref_area == 'USA') & (data.time >= 1997) & (data.time <= 2019)

usa_data = data[filter]
usa_data['koef_byd'] = (usa_data.obs_value + 100) / 100
usa_data['koef_byd'] = usa_data.koef_byd.shift(fill_value=1.)
usa_data['koef_1967'] = usa_data.koef_byd.cumprod()
usa_data['one_hundred_billion_2019'] = usa_data.koef_1967 * 1e11
usa_data.plot(x='time', y='one_hundred_billion_2019')
print('Answer:', usa_data.one_hundred_billion_2019.max())
plt.show()

# 2.2
rosstat = pd.read_csv('rosstat.csv')
filter = (data.ref_area == 'RUS') & (data.time >= 1991) & (data.time <= 2020)
rosstat = pd.merge(rosstat, data[filter], on=['time'], how='left')[['time', 'obs_value_x', 'obs_value_y']]
rosstat = rosstat.rename(columns={'obs_value_x': 'Rosstat', 'obs_value_y': 'MOT'})
rosstat.Rosstat = rosstat.Rosstat / 100
rosstat.set_index('time').plot(title='Динамика инфляции в России', kind='bar', log=True)
plt.show()

# 2.1.1
data = data[(data.time >= 1997) & (data.time <= 2020)]
data['koef_byd'] = (data.obs_value + 100) / 100
data['sum'] = data.groupby(by='ref_area')['koef_byd'].cumprod()
data[data.ref_area == 'RUS'].plot(x='time', y='sum', kind='bar')
plt.show()

# 2.3
data = pd.read_csv('EIP_3WAP_SEX_AGE_GEO_RT_A.csv')
rus_data = data[(data.ref_area == 'RUS') & (data.time >= 2000) & (data.time <= 2020)]
seaborn.barplot(x='time', y='obs_value', hue='classif2', data=rus_data)
plt.legend(loc='upper left', bbox_to_anchor=(0, 1.15), shadow=True, ncol=2, borderaxespad=0.)
plt.show()
