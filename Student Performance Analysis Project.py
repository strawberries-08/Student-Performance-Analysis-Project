#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#load the dataset 
data=pd.read_csv('StudentsPerformance.csv')
#display the first 5 rows
data.head()

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Display summary statistics for numerical features
summary_statistics = data.describe()
print("Summary Statistics:\n", summary_statistics)

# Convert categorical variables to 'category' dtype
categorical_cols = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
data[categorical_cols] = data[categorical_cols].astype('category')

# Confirm data types after conversion
print("Data types after conversion:\n", data.dtypes)

# Create histograms for math, reading, and writing scores
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
sns.histplot(data['math score'], kde=True, color='green')
plt.title('Math Score Distribution')

plt.subplot(1, 3, 2)
sns.histplot(data['reading score'], kde=True, color='blue')
plt.title('Reading Score Distribution')

plt.subplot(1, 3, 3)
sns.histplot(data['writing score'], kde=True, color='red')
plt.title('Writing Score Distribution')

plt.tight_layout()
plt.show()


#Create bar plots for comparing scores based on gender
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
sns.barplot(x='gender', y='math score', data=data, palette='Set1')
plt.title('Math Score by Gender')

plt.subplot(1, 3, 2)
sns.barplot(x='gender', y='reading score', data=data, palette='Set2')
plt.title('Reading Score by Gender')

plt.subplot(1, 3, 3)
sns.barplot(x='gender', y='writing score', data=data, palette='Set3')
plt.title('Writing Score by Gender')

plt.tight_layout()
plt.show()

# Create bar plots for comparing scores based on race/ethnicity
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
sns.barplot(x='race/ethnicity', y='math score', data=data, palette='Set1')
plt.title('Math Score by Race/Ethnicity')

plt.subplot(1, 3, 2)
sns.barplot(x='race/ethnicity', y='reading score', data=data, palette='Set2')
plt.title('Reading Score by Race/Ethnicity')

plt.subplot(1, 3, 3)
sns.barplot(x='race/ethnicity', y='writing score', data=data, palette='Set3')
plt.title('Writing Score by Race/Ethnicity')

plt.tight_layout()
plt.show()


# In[ ]:




