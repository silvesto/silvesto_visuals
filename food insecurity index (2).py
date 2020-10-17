#!/usr/bin/env python
# coding: utf-8

# In[2]:


#A DATA VISUALISATION ANALYSING THE VARIENCE FROM YEAR 2015 TO 2019 OF THE UNDERLYING FACTORS AFFECTING FOOD INSECURITY(AS STATED BY THE GFSI) IN UGANDA 


# In[3]:


#IMPORTING DATA
#GFSI DATASETS FROM 2015 TO 2019
#THE COMBINED_DATA IS DATA COMBINED FOR SELECTED COUNTRIES(BENIN, BURUNDI,ETHIOPIA,MALAWI,MALI,MOZAMBIQUE,RWANDA, UGANDA) from 2015 to2019


# In[4]:


import pandas as pd


# In[5]:


data_fifteen=pd.read_csv('GFSI_2015_Dataset_Data.csv')
data_sixteen=pd.read_csv('GFSI_2016_Dataset_Data.csv')
datas_eventeen=pd.read_csv('GFSI_2017_Dataset_Data.csv')
data_eighteen=pd.read_csv('GFSI_2018_Dataset_Data.csv')
data_nineteen= pd.read_csv('GFSI_2019_Dataset_Data.csv')
combined_data=pd.read_csv('timeseries.csv')



# In[6]:


#CHOOSING DATA ABOUT UGANDA ONLY


# In[7]:


Uganda_data=combined_data[combined_data.Series=='Uganda']


# In[8]:


#IMPORTING NECESARY PACKAGES


# In[9]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[10]:


b=Uganda_data.Change_in_average_food_costs
c=Uganda_data.GDP
d=Uganda_data.Volatility_of_agricultural_production
a=Uganda_data.Food_loss
e=Uganda_data.Agricultural_import_tariffs


# In[13]:


plt.figure(figsize=(8,6))
plt.show()
import seaborn as sns
sns.set_style('darkgrid')


# In[20]:


plt.plot(Uganda_data.Year,a*10,'.-')
plt.xticks(Uganda_data.Year)
plt.plot(Uganda_data.Year,b,'b.-' )
plt.plot(Uganda_data.Year,c/10, 'r.-' )
plt.plot(Uganda_data.Year,e*10,'g.-')
plt.plot(Uganda_data.Year,d*1000,'.-')
plt.legend(['food loss per year','Change in average food costs','GDP','Agricultural import tariffs','Volatility of agricultural production'])
plt.ylabel('Food Loss')
plt.title('TREND OF FOOD INSECURITY INDEX OF UGANDA',fontdict={'fontweight':'bold', 'fontsize':20})
plt.xlabel('year')
plt.show()


# In[15]:


Uganda_data.plot.line(x='Year',y='Change_in_average_food_costs',color='b')
plt.xticks(Uganda_data.Year)
plt.show()


# In[16]:


Uganda_data.plot.line(x='Year',y='GDP',color='r')
plt.xticks(Uganda_data.Year)
plt.show()


# In[17]:


Uganda_data.plot.line(x='Year',y='Food_loss')
plt.xticks(Uganda_data.Year)
plt.show()


# In[18]:


Uganda_data.plot.line(x='Year',y='Agricultural_import_tariffs',color='g')
plt.xticks(Uganda_data.Year)
plt.show()


# In[19]:


Uganda_data.plot.line(x='Year',y='Volatility_of_agricultural_production',color='r')
plt.xticks(Uganda_data.Year)
plt.show()


# In[ ]:




