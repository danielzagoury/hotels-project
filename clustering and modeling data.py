#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
clean_df = pd.read_csv('/Users/danielzagoury/src/github.com/danielzagoury/Hotels_project/.ipynb_checkpoints/hotels_clean_data.csv')


# In[2]:


plt.scatter(x=clean_df['sum of services'],y=clean_df['rate_of_the_hotel'],c='r',marker='s',label='sum of services')
plt.scatter(x=clean_df['sum of facilities'],y=clean_df['rate_of_the_hotel'],c='b',marker='o',label='sum of facilities')

plt.legend(numpoints=1,loc=4)
plt.xlabel('rate of the facilities and services' )
plt.ylabel('rate of the hotel')
plt.show()


# In[3]:


facilities_linear=linear_model.LinearRegression().fit(clean_df.iloc[:,20:21],clean_df.iloc[:,1:2])
services_linear=linear_model.LinearRegression().fit(clean_df.iloc[:,21:],clean_df.iloc[:,1:2])


# In[4]:


plt.scatter(x=clean_df['sum of services'],y=clean_df['rate_of_the_hotel'],c='k',marker='*',label='sum of services')
plt.plot(clean_df['sum of services'],services_linear.predict(clean_df.iloc[:,1:2]),'k',color='blue',linewidth=3)

plt.xlabel('sum of the services' )
plt.ylabel('rate of the hotel')
plt.show()

plt.scatter(x=clean_df['sum of facilities'],y=clean_df['rate_of_the_hotel'],c='k',marker='*',label='sum of services')
plt.plot(clean_df['sum of facilities'],facilities_linear.predict(clean_df.iloc[:,1:2]),'k',color='blue',linewidth=3)

plt.xlabel('sum of facilities' )
plt.ylabel('rate of the hotel')
plt.show()


# In[5]:


x=clean_df.drop(columns=["rate_of_the_hotel","name","location_rating","comfort","staff","rate_of_facilities","value_for_money","Cleanliness","city","sum of facilities","sum of services"])
y=clean_df["rate_of_the_hotel"]


# In[6]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)


# In[7]:


lr=linear_model.LinearRegression()
lr.fit(X_train,y_train)


# In[8]:


y_pred=lr.predict(X_test)


# In[9]:


r2_score(y_test,y_pred)


# In[10]:


mean_absolute_error(y_test,y_pred)


# In[11]:


mean_squared_error(y_test,y_pred)


# In[ ]:




