#!/usr/bin/env python
# coding: utf-8

# In[1]:


#the ratio of the facilities and services in hotels
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

clean_df = pd.read_csv('/Users/danielzagoury/PycharmProjects/pythonProject/clean_df.csv')


sum_of_columns = clean_df.sum(axis=0)
df = pd.DataFrame({'number of facilities': [sum_of_columns["bar"],sum_of_columns["swimming_pool"] ,sum_of_columns["parking"],sum_of_columns["Elevator"],sum_of_columns["Sauna"],sum_of_columns["safe"] ]},index=["bar","swimming_pool" ,"parking","Elevator","Sauna", "safe"])
plot = df.plot.pie(y='number of facilities', figsize=(6, 6))
df3 = pd.DataFrame({'number of services': [sum_of_columns["desk_24/7"],sum_of_columns["wifi"] ,sum_of_columns["Babysitting_Child_services"],sum_of_columns["pets"],sum_of_columns["Wheelchair_accessible"]]},index=["desk 24/7","wifi" ,"Babysitting Child services","pets","Wheelchair accessible"])
plot2 = df3.plot.pie(y='number of services', figsize=(6, 6))
print(plot)
print(plot2)


# In[2]:


#see if the numbers of the facilities and services help for high rate
l=[]
k=[]
for i in range (3000):
    x=clean_df.iloc[i]['sum of services']
    y=clean_df.iloc[i]['rate_of_the_hotel']
    z=clean_df.iloc[i]['sum of facilities']
    item1=[x,y]
    item2=[z,y]
    l.append(item1)
    k.append(item2)

df = pd.DataFrame(l,columns=['sum of services', 'rate_of_the_hotel'])
plot1 = df.plot.scatter(x='sum of services',y='rate_of_the_hotel', figsize=(4, 4))
df1 = pd.DataFrame(k,columns=['sum of facilities', 'rate of the hotel'])
plot2 = df1.plot.scatter(x='sum of facilities',y='rate of the hotel', figsize=(4, 4))
print(plot1)
print(plot2)


# In[3]:


rome_sum=0
london_sum=0
Barcelona_sum=0
rome_val=0
london_val=0
Barcelona_val=0
for i in range (3000):
    if(clean_df.iloc[i]['city']=="Rome"):
        rome_sum+=clean_df.iloc[i]['rate_of_the_hotel']
        rome_val+=clean_df.iloc[i]['value_for_money']
    if(clean_df.iloc[i]['city']=="London"):
        london_sum+=clean_df.iloc[i]['rate_of_the_hotel']
        london_val+=clean_df.iloc[i]['value_for_money']
    if(clean_df.iloc[i]['city']=="Barcelona"):
        Barcelona_sum+=clean_df.iloc[i]['rate_of_the_hotel']
        Barcelona_val+=clean_df.iloc[i]['value_for_money']


rome_avr=rome_sum/1000
london_avr=london_sum/1000
Barcelona_avr=Barcelona_sum/1000
rome_avr_val=rome_val/1000
london_avr_val=london_val/1000
Barcelona_avr_val=Barcelona_val/1000
#comparison between major cities the average
df1 = pd.DataFrame({'cities':['rome',"london","barcelona"], 'average':[rome_avr,london_avr,Barcelona_avr]})
ax = df1.plot.bar(x='cities', y='average', rot=0)
#comparison between major cities the value for money
df2 = pd.DataFrame({'cities':['rome',"london","barcelona"], 'value_for_money':[rome_avr_val,london_avr_val,Barcelona_avr_val]})
ax = df2.plot.bar(x='cities', y='value_for_money', rot=0)


# In[4]:


#see if the numbers of the facilities and services help for high rate
l=[]
k=[]
for i in range (3000):
    x=clean_df.iloc[i]['sum of services']
    y=clean_df.iloc[i]['rate_of_the_hotel']
    item1=[x,y]
    l.append(item1)
np.random.seed(1234)
df = pd.DataFrame(np.random.rand(10,3),columns=['sum of services', 'rate_of_the_hotel','sum of facilities'])
plot1 = df.boxplot(column=['sum of services', 'rate_of_the_hotel','sum of facilities'])

print(plot1)


# In[5]:


clean_df.corr()


# In[6]:


plt.imshow(clean_df.corr(),cmap='hot',interpolation='nearest')


# In[7]:


import seaborn as sns

Var_Corr = clean_df.corr()
# plot the heatmap and annotation on it
sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=False)


# In[ ]:




