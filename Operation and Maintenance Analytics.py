#!/usr/bin/env python
# coding: utf-8

# 
# # The Relation between Efficiency and Tempreture Degrees
# ## O & M Analytics
# ***

# ## Table of Contents
# ### Target
# ### Discovering and Manipulating the Data
# ### Calculating Efficiency
# ### Descriptive Statistics
# ### Visualizing the Data
# ### Conclusion

# ### Target

# Calculating Efficiency of the Internal Temperature Degrees for Medical Laboratories in The Regional Laboratory and Central Blood Bank. Finding a Relation between Temperature Degrees as 'Independent Variable', Efficiency Rates and Quality as 'Dependent Variable'.

# ### Discovering and Manipulating the Data

# #### Importing Libraries

# In[1]:


__author__ = "Abdulaziz Alsulami"
__date__ = '2020-Aug'
__email__ = "engaziz02@gmail.com"


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

get_ipython().run_line_magic('matplotlib', 'inline')


# #### Reading the Data

# In[3]:


lab_df = pd.read_csv('D:\own_project.csv', sep=';')

print('Data')
lab_df


# #### Checking count of Rows and Columns

# In[4]:


print('Rows Count:   ',lab_df.shape[0])
print('Columns Count: ',lab_df.shape[1])


# #### Checking types of data for each column

# In[5]:


print('Column_Name       ','Data_Type')
lab_df.dtypes


# #### Rearranging The  Columns

# In[6]:


lab_df = lab_df.reindex(columns = ['Lab Name','Room','Floor Name','No of Devices','Temperature Degree'])

print('Data after Rearrange the Columns:')
lab_df


# #### Renaming the Columns 

# In[7]:


lab_df = lab_df.rename(columns={
                                'Lab Name':'LabName',
                                'Room':'Room',
                                'Floor Name':'Floor',
                                'Temperature Degree':'TemperatureDegree',
                                'No of Devices':'DevicesNumber'
                                })

print('Data After Rename The Columns:')
lab_df


# ###  Calculating the Efficiency for each Temperature Degree

# Set Ideal, Actual and Breakdown Temperature Degrees as well as create a Formula for calculating Actual Efficiency

# In[8]:


# All Temperature Degree in Celsius.

# Ideal Tempreture Degree 
ideal_temp_deg = 22

# Actual Tempreture Degrees
actual_temp_deg = lab_df['TemperatureDegree']

# Ideal Efficincy percent
ideal_eff = 100

# one Temperature Degree Equal 10 percent from Efficiency 
one_deg = 10

# Actual Efficiency percent
actual_eff = ideal_eff -(actual_temp_deg -ideal_temp_deg)* one_deg

# Breakdown Tempreture Degree
Break_temp_deg = ideal_temp_deg + 10


# In[9]:


def calculating_actual_efficiency(x):
    '''returns to efficiency rate of x'''
    ideal_eff = 100
    ideal_temp_deg = 22
    one_deg = 10
    actual_temp_deg = x
    actual_eff = ideal_eff - (actual_temp_deg -ideal_temp_deg)* one_deg
    return round(actual_eff,2)


# #### Creating a new column called Efficiency

# In[10]:


lab_df['Efficiency'] = calculating_actual_efficiency(lab_df['TemperatureDegree'])
print('Data with Efficiency column: ')
lab_df


# #### Displaying the data according to  Laboratory Name column

# In[11]:


lab_name_index = lab_df.groupby(by=['LabName']).mean()
print('Indexing the data by Lab Name column: ')
round(lab_name_index,2)


# #### How many laboratories had Efficiency greater than or equal 70 ? Which Laboratory had higher Efficiency ?

# In[12]:


criteria_1 = lab_df['Efficiency'] >= 70
crit_1 = lab_df[criteria_1][['LabName','Efficiency','Room']].sort_values('Efficiency',ascending=False).reset_index(drop=True)

answer = '''{0} laboratories.
{1} laboratory has the highest Efficiency. '''

print(answer.format(len(crit_1),crit_1.LabName.iloc[0]))
crit_1


# #### How many laboratories had Efficiency less than 70 ?  Which Laboratory had lower Efficiency ?

# In[13]:


criteria_2 = lab_df['Efficiency'] < 70
crit_2 = lab_df[criteria_2][['LabName','Efficiency','Room']].sort_values('Efficiency').reset_index(drop=True)

answer = '''{0} laboratories.
Room {1} at {2} laboratory has the lowest Efficiency. '''

print(answer.format(len(crit_2), crit_2.Room[0],crit_2.LabName[0]))
crit_2


# #### How many laboratories had Temperature Degrees less than or equal 25 ?

# In[14]:


criteria_2 = lab_df['TemperatureDegree'] <= 25
crit_2 = lab_df[criteria_2][['LabName','TemperatureDegree']].sort_values(by='TemperatureDegree')

answer = '''{0} laboratories: '''

print(answer.format(len(crit_2)))
crit_2


# #### How many laboratories have Temperature Degrees greater than 25 ?

# In[15]:


criteria_3 = lab_df['TemperatureDegree'] > 25
crit_3 = lab_df[criteria_3][['LabName','TemperatureDegree']].sort_values(by='TemperatureDegree')

answer = '''{0} laboratories:'''

print(answer.format(len(crit_3)))
crit_3


# #### Creating a new column is called Quality which gives value 'good'  if Efficiency greater than or equal 70 otherwise 'bad'.

# In[16]:


lab_df['Quality'] = np.where(criteria_1, 'Good', 'Bad')
lab_df


# ### Descriptive Statistics

# #### Describing Statistics for Temperature Degree and Efficiency Columns

# In[17]:


stat_temp_eff = lab_df.describe()
stat_temp_eff = pd.DataFrame(round(stat_temp_eff,2)).transpose()
stat_temp_eff['IQR'] = stat_temp_eff['75%'] - stat_temp_eff['25%']
stat_temp_eff


# #### Describing Statistics for Categorical Columns

# In[18]:


lab_df.describe(include=['O']).transpose()


# #### The Average Value of Temperature Degrees and Efficiency

# In[19]:


def mean(x):
    '''returns to the average value'''
    return sum(x) / len(x)

print('The Temperature Degrees average: ', round(mean(lab_df['TemperatureDegree']), 2), 'C')
print('The Efficiecny average:          ', round(mean(lab_df['Efficiency']), 2), '%')


# #### The Middle Value of Temperature Degrees and Efficiency

# In[20]:


def median(x):
    '''returns to the middel value '''
    x = sorted(x)
    n = len(x)
    medpoint = n // 2
    if n % 2 ==1:
        return x[medpoint]
    else:
        low= medpoint -1
        high= medpoint
        return (x[high] + x[low]) // 2
    
print('The Middle value of Tempreture Degrees: ', median(lab_df['TemperatureDegree']), 'C')
print('The Middle value of Efficiency :        ', median(lab_df['Efficiency']), ' %')


# #### The Most Common Value of Temperature Degrees and Efficiency

# In[21]:


from collections import Counter

def mode(x):
    '''returns to the most common values'''
    counts = Counter(x)
    max_counts = max(counts.values())
    return [key for key, val in counts.items() 
            if val == max_counts][0]
     
print('The Most Common Temperature Degree: ', mode(lab_df['TemperatureDegree']), 'C')
print('The Most Common Efficiency        : ', mode(lab_df['Efficiency']), ' %')


# #### The Minimum and Maximumn values of Temperature Degrees and Efficiency

# In[22]:


def min_max(temp):
    '''returns to minmum and maximum values'''
    return min(temp), max(temp)
print('The Minmum and Maximum Temperature Degree: ', min_max(lab_df.TemperatureDegree), 'C')
print('The Minmum and Maximum Efficiency        : ', min_max(lab_df.Efficiency), '  %')


# ### Visualizing the Data

# #### Indexing the data according to Laboratory Name

# In[23]:


lab_df_avg = lab_df.groupby(by='LabName').mean()
lab_df_avg['Quality'] = np.where(lab_df_avg['Efficiency'] >=70, 'Good', 'Bad')
round(lab_df_avg,2)


# In[24]:


# Showing the Quality of Efficiency Rates for each Laboratory

plt.figure(figsize=(10,5))

X = lab_df_avg.index
Y = lab_df_avg.Efficiency

ax = sns.barplot(X, Y, data=lab_df_avg, hue='Quality', alpha=0.6, palette=['red','blue'])
ax.set_xticklabels(ax.get_xticklabels(),rotation=45,fontsize=12)

plt.title('Efficiency vs Laboratory Name', fontsize=12)
plt.xlabel('Laboratory Name', fontsize=12)
plt.ylabel('Efficiency', fontsize=12)

plt.legend(loc=1, fontsize='x-small')
plt.grid(True)
plt.show()


# In the Regional Laboratory, there are **70%** of laboratories assort as _Bad Efficiency_ and **30%** as _Good Efficiency_.
# If _Efficiency_ less than **70%** the _Quality_ becomes __Bad otherwise Good__.

# #### Blood Bank Laboratory

# In[25]:


BB = lab_df[lab_df['LabName'] == 'Blood Bank'].sort_values(by='Quality', ascending=False, ignore_index=True)
BB


# In[26]:


# Showing the Quality of Efficiency Rates for Blood Bank Department

plt.figure(figsize=(8,5))

X = BB['Room']
Y = BB['Efficiency']

sns.barplot(X, Y, hue=BB['Quality'], alpha=0.6, palette=['red','blue'])

plt.title('Blood Bank Efficiency by Room', fontsize=12)
plt.xlabel('Room', fontsize=12)
plt.ylabel('Efficiency', fontsize=12)

plt.legend(loc=2,fontsize='x-small')
plt.grid(True)
plt.show()


# In Blood Bank , All Rooms assort as Bad Efficiency.

# #### Polymerase Chain Reaction Laboratory

# In[27]:


PCR = lab_df[lab_df['LabName'] == 'Polymerase Chain Reaction']
PCR


# In[28]:


# Showing the Quality of Efficiency Rates for Polymerase Chain Reaction

plt.figure(figsize=(8,5))

PCR = lab_df[lab_df['LabName'] == 'Polymerase Chain Reaction']
X = PCR['Room']
Y = PCR['Efficiency']

ax = sns.barplot(X, Y, hue=PCR['Quality'], alpha=0.6, palette=['red','blue'])

plt.title('Polymerase Chain Reaction Efficiency by Room', fontsize=12)
plt.xlabel('Room', fontsize=12)
plt.ylabel('Efficiency', fontsize=12)

plt.legend(loc= 1, fontsize='x-small')
plt.grid(True)
plt.show()


# In Ploymerase Chain Reaction Laboratory, there are five Rooms assort as Bad Efficiency and one as Good Efficiency.

# #### The Relation between Efficiency 'Dependent Variable' and Temperature Degree 'Independent Variable'

# In[29]:


# Encoding Quality Good value is 1 and Bad value is 0
quality_encoder = np.where(lab_df['Quality'] == 'Good', 1, 0)
quality_encoder = pd.Series(quality_encoder)

# plotting Temperature Degreee, Efficiency and quality_encoder to find the correlation between them.
data = lab_df.copy()                                        
data['QualityEnc'] = quality_encoder                    
cols = ['TemperatureDegree','Efficiency','QualityEnc']  

sns.pairplot(data[cols], height=2.5)  

plt.show()


# The graph proves the relation between Temperature Degrees and Efficiency Rates is __inversely proportional__ as well as most higher Degrees and lower Rates are within Bad Quality __'Zero value'__ while they are less within Good Quality __'One value'__.

# In[30]:


# Finding corellation for TemperatureDegree, Efficiency and QualityEnc

cm = data[cols].corr()

sns.set(font_scale=1)

sns.heatmap(data=cm,
           cbar=True,
           annot=True,
           square=True,
           fmt = '0.2f',
           annot_kws={'size':15},
           xticklabels=cols,
           yticklabels=cols)


plt.show()


# - A perfect negative correlation between Temperature Degree and Efficiency.
# - A strongly negative correlation between Temperature Degree and Quality.
# - A strongly positive correlation between Efficiency and Quality.

# #### Temperature Degrees vs Good or Bad Efficicney Rates

# In[31]:


lab_df[['TemperatureDegree','Efficiency']].transpose()


# In[32]:


# Showing The Relation between Temperature Degrees and Efficiency Rates

plt.figure(figsize=(15,5))

X = lab_df['TemperatureDegree']
Y = lab_df['Efficiency']

sns.pointplot(data=lab_df, x=X, y=Y, hue='Quality',scale=0.6, color='b', palette=['red','blue'])

plt.title('Efficiency vs Temperature Degrees', fontsize=15)
plt.xlabel('Temperature Degrees', fontsize=15)
plt.ylabel('Efficiency', fontsize=15)

plt.legend(loc= 1, fontsize='small')
plt.grid(True)
plt.show()


# Overall, the Efficiency Rates are decreased with increasing the Temperature Degrees and when a Degree exceeds 25 C the Efficiency Rates are within Bad Rates.

# #### Temperature Degrees and Efficiency Distribution

# In[33]:


# Showing distribution of Temperature Degrees and Efficiency Rates

f, axes = plt.subplots(ncols=2, figsize=(15,6))

X_0 = lab_df.TemperatureDegree
X_1 = lab_df.Efficiency

sns.distplot(X_0, bins=4, kde=False, color='b', ax=axes[0]).set_title('Temperature Degree Distribution', fontsize=15)
axes[0].set_ylabel('Temperature Degree Count', fontsize=15)
axes[0].set_xlabel('Temperature Degree',fontsize=15)

sns.distplot(X_1 ,bins=4, kde=False, color='g', ax=axes[1]).set_title('Efficiency Distribution', fontsize=15)
axes[1].set_ylabel('Efficiency Count', fontsize=15)
axes[1].set_xlabel('Efficiency', fontsize=15)


plt.grid(True)
plt.show()


# The _Blue Graph_ is represented as __Temperature Degree Distribution__ and the _Green Graph_ is represented as __Efficiency Distribution__. Each Temperature Degree is identified with a certain Efficiency Rate. The highest frequency Degrees are in range **27.35 to 29.15** with Efficiency in range **28.50 to 45.00** and the lowest frequency Efficiency in range **22. to 23.95** with Efficiency in range **81.00 to 98.20**.

# #### What is the Quality Rate of Degrees?

# In[34]:


quality_percent = lab_df['Quality'].value_counts(normalize=True)
quality_percent


# In[35]:


# Showing percent for Bad Quality and Good 

plt.figure(figsize=(8,5))
plt.axis([0,2,0,0.85])

X = quality_percent.index
Y = quality_percent
sns.barplot(X, Y, alpha=0.6,palette=['red','blue'])

plt.title('Quality Rate', fontsize=15)
plt.xlabel('Quality', fontsize=15)
plt.ylabel('Rate', fontsize=15)

plt.grid(True)
plt.show()


# There are 79% of Laboratories assort as Bad Quality and 21% as Good Quality.

# #### How many laboratories locate in ground and the first Floor?

# In[36]:


lab_df_floor = lab_df['Floor'].value_counts()
lab_df_floor


# In[37]:


# Showing number of Laboratories for each Floor

plt.figure(figsize=(8,5))
plt.axis([0,2,0,13.5])

X = lab_df_floor.index
Y = lab_df_floor

sns.barplot(X, Y , alpha=0.6, palette=['g','b'])

plt.title('Laboratoies Destribution by Floor', fontsize=15)
plt.xlabel('Floor', fontsize=15)
plt.ylabel('Number of Laboratories', fontsize=15)

plt.grid(True)
plt.show()


# There are **13** laboratories located in First Floor a and **6** laboratories in **Ground Floor**.

# ### Conclusion

# There is an **inversely relational** between Efficiency rates and Temperature Degrees. Good Efficiency Rates when Temperature Degrees are less than or equal **25 C**. There are **13** laboratories have bad Efficiency Rates and **6** Laboratories have good Efficiency Rates. **68%** of laboratories are located on First Floor and **32%** in Ground Floor. The Temperature Degrees average is about **26.42 C** with Efficiency Rate of **54.24%**, this refers to a Bad Rate.

# In[38]:


pd.DataFrame.to_csv(lab_df,'My_Own_Project.csv')

