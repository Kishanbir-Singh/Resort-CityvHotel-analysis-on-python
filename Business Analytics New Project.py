#!/usr/bin/env python
# coding: utf-8

# Import Libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[4]:


df = pd.read_csv('hotel_bookings 2.csv')


# In[6]:


df.head(20)


# In[7]:


df.tail()


# In[9]:


df.shape


# In[11]:


df.info()


# In[12]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[13]:


df.info()


# In[14]:


df.describe(include = 'object')


# In[17]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[18]:


df.isnull().sum()


# In[21]:


df.drop(['company', 'agent'], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[22]:


df.isnull().sum()


# In[23]:


df.describe()


# In[24]:


df['adr'].plot(kind = 'box')


# In[25]:


df = df[df['adr']<5000]


# In[26]:


df.describe()


# Data Analysis & Visualisation

# In[32]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
cancelled_perc

plt.figure(figsize = (5,4))
plt.title('REservation status count')
plt.bar(['Not canceled', 'Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show


# In[42]:


plt.figure(figsize = (8,4))
ax1= sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[45]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[47]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[48]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[52]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Hotel', fontsize = 20)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'city Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[58]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (20,8))
ax1= sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels,_ =ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('number of resrvations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[69]:


df.describe()


# In[70]:


df['adr'].plot(kind = 'box')


# In[71]:


cancelled_data = df[df['is_canceled'] ==1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


# In[72]:


df['market_segment'].value_counts()


# In[73]:


df['market_segment'].value_counts(normalize = True)


# In[74]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[ ]:




