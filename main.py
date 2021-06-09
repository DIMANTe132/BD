import pandas

data = pandas.read_csv('EIP_3WAP_SEX_AGE_GEO_RT_A.csv')

print("Row count: " + str(len(data)))
print("------------------------------------------------")
print(data[4:10])
print("------------------------------------------------")
print(data['ref_area'].value_counts())
print("------------------------------------------------")
print(data[data.ref_area == 'USA'])
print("------------------------------------------------")
data = data[['ref_area', 'sex', 'classif1',
             'classif2', 'time', 'obs_value']]

print(data[data.ref_area == 'RUS'].time.value_counts().sort_index())
print("------------------------------------------------")
print(data[(data.ref_area == 'USA') & (data.time == 2005)])
print("------------------------------------------------")
print(data[
          (data.ref_area == 'USA') &
          (data.classif1 == 'AGE_YTHBANDS_Y15-29') &
          ((data.time >= 2013) & (data.time <= 2015))
          ])
print("------------------------------------------------")
print(data[
          (data.classif1 == 'AGE_YTHBANDS_Y15-29') &
          (data.sex == 'SEX_T') &
          (data.classif2 == 'GEO_COV_RUR')
          ].sort_values(by='obs_value', ascending=False)[:50])
print("------------------------------------------------")
print("Max obs_value: " + str(data[
                                  (data.classif1 == 'AGE_YTHBANDS_Y15-29') &
                                  (data.sex == 'SEX_T') &
                                  (data.classif2 == 'GEO_COV_RUR')
                                  ].obs_value.max()))
