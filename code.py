# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state'] = df['state'].apply(lambda x: x.lower())
df['Total'] = df['Jan'] + df['Feb'] + df['Mar']
sum_row_1 = df['Jan'].sum(axis=0,skipna=True) , df['Feb'].sum(axis=0,skipna=True) , df['Mar'].sum(axis=0,skipna=True)
sum_row_2 = [list(sum_row_1)]
sum_row = pd.DataFrame(sum_row_2,columns=['Jan','Feb','Mar'])
print(sum_row)
df_final = df.append(sum_row,ignore_index=True)
print(df_final)
#print(df.head())
# Code ends here


# --------------
import requests

# Code starts here
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
#df1 = df1.iloc[11:]
#df1 = df1.pivot(index=df1.iloc[11],columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'])
header = df1.iloc[11]
df1 = df1[12:]
df1.columns = header
df1['United States of America'] = df1.rename(columns={"United States of America":"United_States_of_America"})
print(df1['United States of America'].head(11))


# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = {}
for i in range(len(df1['US'])):
    mapping[df1['United States of America'].iloc[i]] = df1['US'].iloc[i]
df_final['abbr'] = map(mapping,df_final['state'])
clist = ['Feb','Jan','Mar','Total','account','city','abbr','name','postal-code','state','street']
df_final = df_final[clist]
print(df_final.head())
# Code ends here


# --------------
# Code stars here

df3 = df_final['abbr']


df_final['abbr'] = np.where(df_final['state']=='mississipi','MS',np.where(df_final['state']=='tenessee','TN',df3))


# Code ends here


# --------------
# Code starts here
df_sub = df_final.groupby('abbr')[['abbr','Jan','Feb','Mar','Total']].sum()
print(df_sub)
formatted_df = df_sub.applymap(lambda x: '$'+str(x))
print(formatted_df.head())
print(df_final.head(20))
# Code ends here


# --------------
# Code starts here

sum_row = pd.DataFrame(df[['Jan','Feb','Mar','Total']].sum())
print(sum_row)
df_sub_sum = sum_row.transpose()
df_sub_sum = df_sub_sum.applymap(lambda x: '$'+str(x))
print(df_sub_sum)
final_table = formatted_df.append(df_sub_sum)
print(final_table)
final_table.rename(index={'0':'Total'},inplace=True)
# Code ends here


# --------------
# Code starts here
df_sub.rename(columns={'Total':'total'},inplace=True)
print(df_sub)
df_sub['total'].value_counts().plot(kind='pie')
# Code ends here


