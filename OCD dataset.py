#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install mysql-connector-python')


# In[14]:


get_ipython().system(' pip install psycopg2-binary')


# In[2]:


import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[3]:


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Godisgood",
    database = "health_data"
)

mycursor = db.cursor()
print(db)


# In[4]:


mycursor.execute("select * from health_data.ocd_patient_dataset")

output = mycursor.fetchall()

for x in output:
    print(x)


# In[5]:


query = "select * from health_data.ocd_patient_dataset"

df = pd.read_sql(query, db)


# In[6]:


# view the dataset
df.head()


# # Exploratory Data Analysis

# In[41]:


df.shape


# In[42]:


df.columns


# In[43]:


df.info


# In[7]:


df.isna()


# In[8]:


df.loc[df.duplicated()]


# In[44]:


df.describe()


# In[45]:


#change decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[46]:


#missing values
df.isnull().sum()


# In[47]:


df.nunique()


# In[52]:


df.sort_values(by="Gender").head(20)


# In[51]:


df.sort_values(by="Y-BOCS Score (Obsessions)", ascending=False)


# # DATA CLEANING

# In[76]:


df.dtypes


# In[66]:


#changing datetype
pd.to_datetime(df['OCD Diagnosis Date'])


# In[67]:


df['OCD Diagnosis Date'] = pd.to_datetime(df['OCD Diagnosis Date'])


# In[ ]:





# In[68]:


# Reset our index so datetime_utc becomes a column
df.reset_index(inplace=True)

# Create new columns
df['day'] = df['OCD Diagnosis Date'].dt.day
df['month'] = df['OCD Diagnosis Date'].dt.month
df['year'] = df['OCD Diagnosis Date'].dt.year

print(df)


# In[ ]:





# In[69]:


df.head()


# In[ ]:





# In[73]:


df.drop(['level_0', 'index'], axis=1, inplace=True)


# In[ ]:





# In[89]:


df['month'] = pd.to_datetime(df['month'], format='%m').dt.month_name().str.slice(stop=3)


# In[ ]:





# In[91]:


df.head()


# In[ ]:





# In[ ]:


#if changing to numeric e.g.
pd.to_numeric(df['Age'])

#if renaming column name
df.rename(columns={'Medications':'Meds',
                  'Duration of Symtoms (months)' : 'Sx Duration'})


# In[ ]:





# In[ ]:





# In[92]:


# renaming column name
df.rename(columns={'month':'OCD MoM',
                  'year' : 'OCD YoY'})


# In[ ]:





# In[ ]:





# In[ ]:





# # Data Analysis

# ##### Question 1. - Number of patients (by Gender) that have OCD

# In[79]:


df['Gender'].value_counts()


# In[ ]:





# In[80]:


df['Gender'].value_counts()/df['Y-BOCS Score (Obsessions)'].mean()


# In[ ]:





# In[81]:


df['Gender'].value_counts().plot(kind='bar', figsize=(8, 6))
plt.xlabel('OCD Gender Count', labelpad=14)
plt.ylabel('Gender', labelpad=14)
plt.title("Count of Gender with OCD", y=1.02)


# In[ ]:





# #### Question 2. - Number of patients (by Ethnicities) that have OCD

# In[82]:


df['Ethnicity'].value_counts()


# In[ ]:





# In[83]:


df['Ethnicity'].value_counts()/df['Y-BOCS Score (Obsessions)'].mean()


# In[ ]:





# In[84]:


df['Ethnicity'].value_counts().plot(kind='barh', figsize=(8, 6))
plt.xlabel('OCD Count', labelpad=14)
plt.ylabel('Ethnic group', labelpad=14)
plt.title("Count of Ethnicity with OCD", y=1.02)


# In[ ]:





# #### Question 3. - Number of patients diagnosed with OCD by MoM

# In[94]:


df['month'].value_counts()


# In[118]:


df['month'].value_counts()/df['Y-BOCS Score (Obsessions)'].mean()


# In[ ]:





# In[113]:


df['month'].value_counts().plot(kind='bar', figsize=(8, 6))
plt.xlabel('Month Count', labelpad=14)
plt.ylabel('Month', labelpad=14)
plt.title("Count of People diagnosed OCD by Month", y=1.02)


# In[ ]:





# In[ ]:





# #### Question 4. - Count number of patients diagnosed with OCD by MoM per Gender

# In[115]:


df.groupby(['Gender', 'month'])[["Age"]].sum()


# In[ ]:





# In[117]:


df.groupby(['Gender'])[["Y-BOCS Score (Obsessions)"]].sum()


# In[ ]:





# In[119]:


df.groupby(['Gender'])[["Y-BOCS Score (Compulsions)"]].sum()


# In[ ]:





# #### Question 5. - The most common type of OCD

# In[64]:


df['Obsession Type'].value_counts()


# In[ ]:





# In[ ]:





# #### Question 6. - The most common type of medications prescribed for OCD

# In[110]:


df['Medications'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# ### Correlation Analysis

# #### Using charts

# In[124]:


df['Age'].plot(kind='hist', bins=20)


# In[120]:


df.plot(kind='scatter', x='month',
       y='Medications')


# In[ ]:





# In[121]:


df.plot(kind='scatter', x='year',
       y='Medications')


# In[ ]:





# In[99]:


df


# In[100]:


sns.regplot(x="Age", y ="Y-BOCS Score (Obsessions)", data=df)


# In[101]:


sns.regplot(x="Age", y ="Duration of Symptoms (months)", data=df)


# In[102]:


sns.regplot(x="Y-BOCS Score (Compulsions)", y ="Duration of Symptoms (months)", data=df)


# In[ ]:


# Correlation Matrix between all numeric columns
df.corr(method ='spearman')
df.corr(method ='pearson')
df.corr(method ='kendall')
#No Correlation found - Produced errors


# In[ ]:





# In[ ]:





# In[ ]:


# Plotting Heatmap if there was a correlation
correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Age")

plt.ylabel("Duration of Symptoms (months)")

plt.show()


# In[ ]:





# In[ ]:





# ### Using factorise - this assigns a random numeric value for each unique categorical value

# In[103]:


df.apply(lambda x: x.factorize()[0]).corr(method='pearson')


# In[ ]:





# In[104]:


# adjust size using = "plt.rcParams['figure.figsize'] = (20,7)""


correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix exploring OCD Data")

plt.xlabel("Categories")

plt.ylabel("Categories 2")

plt.show()


# In[ ]:





# In[105]:


correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[106]:


sorted_pairs = corr_pairs.sort_values(kind="quicksort")

print(sorted_pairs)


# In[ ]:





# In[107]:


# We can now take a look at the ones that have a high correlation (> 0.5)

strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

print(strong_pairs)


# In[ ]:





# In[124]:


# Looking at the number of Y-BOCS Score (Obsessions)

TypeofmedSum = df.groupby(['Gender', 'Age'])[["Y-BOCS Score (Obsessions)"]].sum()

TypeofmedSumSorted = TypeofmedSum.sort_values('Y-BOCS Score (Obsessions)', ascending = False)

TypeofmedSumSorted = TypeofmedSumSorted['Y-BOCS Score (Obsessions)'].astype('int64') 

TypeofmedSumSorted


# In[125]:


df.plot()


# In[126]:


plt.scatter(x=df['Patient ID'], y=df['Y-BOCS Score (Obsessions)'], alpha=0.5)
plt.title('# of Patient vs Y-BOCS Score (Obsessions)')
plt.xlabel('Y-BOCS Score (Obsessions)')
plt.ylabel('# of Patient')
plt.show()


# In[ ]:





# #### Using Numerised values

# In[150]:


for col_name in df_numerised.columns:
    if(df_numerised[col_name].dtype == 'object'):
        df_numerised[col_name]= df_numerised[col_name].astype('category')
        df_numerised[col_name] = df_numerised[col_name].cat.codes
        
df_numerised


# In[ ]:


##Medication number codes

Benzodiazepam - 0
None - 1
SNRI - 2
SSRI - 3


# In[131]:


df_numerised.corr(method='pearson')


# In[ ]:





# In[146]:


correlation_matrix = df_numerised.corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix with OCD Data")

plt.xlabel("Category")

plt.ylabel("Category 2")

plt.show()


# In[ ]:





# In[142]:


for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes


# In[ ]:





# In[149]:


##MedtypeCodes
Benzodiazepam - 0
None - 1
SNRI - 2
SSRI - 3


sns.swarmplot(x="Medications", y="Y-BOCS Score (Obsessions)", data=df)


# In[ ]:





# In[152]:


sns.stripplot(x="month", y="Y-BOCS Score (Compulsions)", data=df)


# In[ ]:





# In[163]:


df.boxplot()


# In[ ]:




