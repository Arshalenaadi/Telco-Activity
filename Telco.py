#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data=pd.read_excel('E:Telco-Customer-Churn.xlsx')
data.head()


# # Churn count to Gender

# In[39]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel('E:Telco-Customer-Churn.xlsx')
sns.countplot(data=data,x='gender',hue='Churn',palette=['#7DC383','#F8F627'])
plt.title("Churn count with respect  to gender")


# # Count of female senior citizens

# In[19]:


df=data[data.gender == 'Female']
df.loc[df.SeniorCitizen==1,'SeniorCitizen'] = "Yes"
df.loc[df.SeniorCitizen==0,'SeniorCitizen'] = "No"
sns.countplot(x='gender',hue="SeniorCitizen",data = df,palette='dark')
sns.despine()
plt.title("Female senior citizens in the dataset",fontsize=15)
plt.xlabel('')
plt.ylabel('Count',fontsize=13)


# # Tenure with Total Charge

# In[25]:


sns.lineplot(data=data,x="tenure",y="TotalCharges",color='black',linewidth=1.5)


# # Contract preferred by Senior Citizen

# In[29]:


sn=data[data["SeniorCitizen"]==1]
plt.figure(figsize=(6,6))
plt.title("Contract preferred by SeniorCitizens",fontsize=10)
sn.Contract.value_counts(sort=True).plot.pie(fontsize=12,autopct='%1.1f',colors= ['#ff9999','#66b3ff','#99ff99'])
centre_circle=plt.Circle((0,0),0.70,fc='white')
fig=plt.gcf()
fig.gca().add_artist(centre_circle)
plt.tight_layout()
plt.show()


# # Payment based on gender

# In[33]:


plt.figure(figsize=(10,8))
sns.countplot(data['PaymentMethod'],hue=data['gender'],palette='Set2')
sns.despine()
plt.title("Payment based on gender",fontsize=14)
plt.xlabel('Payment Method',fontsize=12)
plt.ylabel('Count',fontsize=12)


# In[ ]:




