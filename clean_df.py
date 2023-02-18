#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
clean_df = pd.read_csv('/Users/danielzagoury/PycharmProjects/pythonProject/hotels/hotels_df.csv')

clean_df=clean_df.drop_duplicates(ignore_index=True)

#replace all the NAN valeus with the mean of the column
mean_value = clean_df['rate_of_the_hotel'].mean()
clean_df['rate_of_the_hotel'].fillna(value=mean_value, inplace=True)

mean_value = clean_df['location_rating'].mean()
clean_df['location_rating'].fillna(value=mean_value, inplace=True)

mean_value = clean_df['comfort'].mean()
clean_df['comfort'].fillna(value=mean_value, inplace=True)

mean_value = clean_df['staff'].mean()
clean_df['staff'].fillna(value=mean_value, inplace=True)

mean_value = clean_df['rate_of_facilities'].mean()
clean_df['rate_of_facilities'].fillna(value=mean_value, inplace=True)

mean_value = clean_df['value_for_money'].mean()
clean_df['value_for_money'].fillna(value=mean_value, inplace=True)

mean_value = clean_df['Cleanliness'].mean()
clean_df['Cleanliness'].fillna(value=mean_value, inplace=True)
sum_array = []
#add new column that count the sum of the facilities of the hotel
for i in range(clean_df.shape[0]):
    sum= clean_df.loc[i,"bar"]+clean_df.loc[i,"swimming_pool"]+clean_df.loc[i,"parking"]+clean_df.loc[i,"Elevator"]+clean_df.loc[i,"Sauna"]+ clean_df.loc[i, "safe"]
    sum_array.append(sum)

# add new column that count the sum of the services of the hotel
sum_array_services = []
for i in range(clean_df.shape[0]):
    sum = clean_df.loc[i, "desk_24/7"]+clean_df.loc[i, "wifi"] + clean_df.loc[i, "Babysitting_Child_services"]+ clean_df.loc[i, "pets"]+clean_df.loc[i, "Wheelchair_accessible"]
    sum_array_services.append(sum)
#clean_df['sum of facilities'] = sum_array
clean_df.loc[:, 'sum of facilities'] = sum_array
clean_df.loc[:, 'sum of services'] = sum_array_services

#print (sum_array)
clean_df=clean_df.copy()

#compression_opts = dict(method='zip',archive_name='clean_df.csv')
clean_df.to_csv('hotels_clean_data.csv', index=False)

