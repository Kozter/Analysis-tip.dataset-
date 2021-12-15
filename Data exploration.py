#%% md
# Project
#%% md

#### Importing libaries

#%%

import numpy as np
import pandas as pd #import panda library
from matplotlib import pyplot as plt #import matplotlib library
import seaborn as sns #import seaborn library

plt.style.use('seaborn-white') #setting the plt.style use

#%% md

## Load and read the data csv.file

#%%

df = pd.read_csv('/users/jorge/desktop/data.csv')
df.head() #data loaded as a dataframe / showing the first 5 rows as a header

#%% md

## Explore the data, and perform proper visualization

#%%

print('data shape:', df.shape) #as we can see we have 244 rows x 6 columns
print('data dim:', df.ndim) #checking dimension
print(type(df)) #veryfing data type

#%% md

### Data information

#%%

df.info() #concise summary of the dataframe such as:
          #index, data type, columns and non-null values

#%%

df.isnull().sum() #Checking for any "null" values

#%%

df.describe() #Summary of the dataset in detail

#%% md

### Co-relations

#%%

df.corr() #find the pairwise co-relations of the columns in the dataframe

#%% md

# summarise

#%% md

#### Total bill

#%%

sum = df['total_bill'].sum()
print('total_bill summary:', sum) #total summary
print('total bill (min) value :', df['total_bill'].min()) #min value
print('total bill mean :', df["total_bill"].mean()) #printing mean value of total_bill
print('total bill median :', df['total_bill'].quantile(q=0.5)) #median value
print('total bill (max) value :', df['total_bill'].max()) #max value

#%% md

#### Tip

#%%

sum1 = df['tip'].sum()
print('tip summary:', sum1) #total summary
print('tip (min) value :', df['tip'].min()) #min value
print('tip mean :', df["tip"].mean()) #printing mean value of tip
print('tip median :', df['tip'].quantile(q=0.5)) #median value
print('tip (max) value :', df['tip'].max()) #max value

#%% md

#### Size

#%%

sum2 = df['size'].sum()
print('size summary:', sum2) #total summary
print('size (min) value :', df['size'].min()) #min value
print('size mean :', df['size'].mean()) #mean value
print('size median :', df['size'].quantile(q=0.5)) #median value
print('size (max) value :', df['size'].max()) #max value

#%% md

#### smoker

#%%

y_smoke = (df['smoker']).value_counts()['Yes']
n_smoke = (df['smoker']).value_counts()['No']
print('yes:', y_smoke) #value count of people smoking
print('no :', n_smoke) #value count of people not smoking

#%%

sns.set_style('whitegrid') #seaborn whitegrid to see the results more exact
sns.set_context('talk') #seaborn setting for a better visualization

#%% md

### Pie chart / smoker vs non-smoker

#%%

plt.style.use('seaborn')
df.groupby(['smoker']).sum().plot(kind= 'pie', y= 'size',
                                  shadow = True,
                                  explode = (0, 0.1),
                                  colors = ['deepskyblue', 'steelblue'],
                                  autopct='%1.1f%%').set_title\
    ('Smokers present');
#pie chart visualizing: smokers vs non-smokers
#counted and sorted by size

#%% md

### Countplot / Daily table servings

#%%

sns.countplot(y='day', hue='time', palette=('mako'),
            saturation=0.8,
            data=df,
              alpha=0.8)
plt.title("Tables served by day");
#catplot visualizing: tables served by lunch & dinner
#counted and sorted by the: different days from friday-sunday

#%% md

### Catplot / Table servings by size

#%%

sns.catplot(x='day', hue='size', palette=('mako'),
            saturation=0.8,
            data=df, kind='count',
            height=8, aspect=.8,
            alpha=0.8)
plt.title("Tables served by size");
#Catplot visualizing: tables served by size
#counted and sorted by the: different days from friday-sunday

#%% md

## Perform data cleaning or transformation

#%% md

# Interesting subject:

#%% md

### We want to add a few new variables to show a interesting subject in the dataframe:

#%%

df['person_bill']=df['total_bill']/df['size'] # what is the total_bill by person?
df['person_tip']=df['tip']/df['size'] #what is the the tip by person?
df.head() #shows the top 5 rows in the set and our new values

#%% md

### Finding new co-relations

#%%

df.corr()

#%% md

#### Tip value by person

#%%

print('tip (min) value :', df['person_tip'].min()) #printing new (min) value of tip
print('tip mean :', df["person_tip"].mean()) #printing new mean value of tip
print('tip (max) value :', df['person_tip'].max()) #printing new (max) value of tip

#%% md

#### Bill value by person

#%%

print('total bill (min) value :', df['person_bill'].min()) #printing new (min) value of total_bill
print('total bill mean :', df["person_bill"].mean()) #printing new mean value of total_bill
print('total bill (max) value :', df['person_bill'].max()) #printing new (max) value of total_bill

#%% md

## Conclusion by visualization or analysis

#%% md

### Average tip by size and smoker

#%%

df.groupby(['smoker', 'size'])['tip'].mean().plot.bar(color='skyblue')
plt.show() #we can conclude that non-smokers size have a higher average tip rate

#%% md

### Tip by person which is less or equal to 1

#%%

df['person_tip'].apply(lambda x: 'true' if x >= 1 else 'false')
#lambda boolean / condition function checking if it meets  the set criteria: 'true' if it does, else 'false'

#%% md

### Differential total bill & bill by person

#%%

sns.distplot(df['total_bill'], color = 'skyblue', label="total_bill", bins = 10) #
sns.distplot(df['person_bill'], color= 'lightgreen', label="person_bill", bins = 7)
#Distplots visualizing: total bill differential by person bill
plt.title("Total Bill & Bill by person"); #setting a plt.title
plt.legend() #added a label to each axes of the plot
plt.xlim(0, 50) #setting the x-axes (min)-(max) value
plt.ylim(0, 0.17); #setting the y-axes (min)-(max) value

#%% md

### Scatterplot total bill and tip sorted by time

#%%

sns.scatterplot(data = df, x='person_bill', y='person_tip', hue='time', palette=('mako'));
#scatterplot visualizing: person bill differential by person tip
#we can conclude that the higher  bill = higher tip

#%% md

### Differential between tip and tip by person

#%%

tip = df.loc[:,['person_tip', 'person_bill']]
tip.plot(color = ['deepskyblue', 'steelblue'], alpha=0.8)
plt.xlim(0, 250) #setting the x-axes (min)-(max) value
plt.ylim(0, 20)
plt.show();

#%% md

#### Filtering

#%%

df.loc[(df.total_bill>25) & (df.person_tip > 2)]
#filtering out showing us who meets the conditions with total bill larger than 25 and also have a tip rate more than 2

#%% md

#### Tip differential subplot

#%%

tip.plot(subplots = True, color = ['deepskyblue', 'steelblue'], alpha=0.8)
plt.xlim(0, 245) #setting the x-axes (min)-(max) value
plt.ylim(0, 22)
plt.show();

#%% md

### Differential between tip and size

#%%

tip2 = sns.swarmplot(x="size", y="person_tip",
                     data=df,
                     palette='magma',dodge=True, alpha=0.8);
plt.show()
#we can easily see the comparison between size and tip
