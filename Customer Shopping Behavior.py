import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/Anitta Joy/Downloads/customer_shopping_behavior.csv")
print(df)
print(df.shape)
print(df.dtypes)
print(df.describe(include='all'))
print(df.isna().sum())
#filling missing review (median)
df['Review Rating']=df.groupby('Category') ['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(df)
print(df.isna().sum())
#column headings are in mixed lower and uppercases and spaces are there
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
#rename
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
#create a column age group
labels=['Young Adult','Adult','Middle-Ages','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)

#create a column age_group
df1=df[['age','age_group']].head(10)
print(df1)


#create column purchase_frequency_days
frequency_mapping={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}

df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(10)
print(df.columns)



print(df[['discount_applied','promo_code_used']].head(10))
print(df['discount_applied']==df['promo_code_used'].all())


df2=df.drop('promo_code_used',axis=1)
print(df2.columns)


df3=df2.isna().sum()
print(df2.columns)


df2.to_csv('C:/Users/Anitta Joy/Documents/customer_shopping_behavior.csv',index=False)
