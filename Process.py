from unicodedata import name
from matplotlib.font_manager import json_dump
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import json

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

URL = 'https://us-central1-raccoon-bi.cloudfunctions.net/psel_de_ingressos'
URL2 = 'https://us-central1-raccoon-bi.cloudfunctions.net/psel_de_compras'
URL3 = 'https://us-central1-raccoon-bi.cloudfunctions.net/psel_de_shows'

df = pd.read_json(URL)
df = df.sort_values(by=['nome']) # to get a better way of visualizing the data

df2 = pd.read_csv(URL2, sep=',')
df3 = pd.read_json(URL3)
df4 = pd.merge(df, df2, how='inner', left_on='nome', right_on='nome')

df_track = df4.loc[(df4['tipo'] == 'Pista')]
df_traitor = df4.drop(df4[(df4['status'] == 'Concluido')].index, inplace = False).drop_duplicates(subset='nome')
df_day = df4[(df4['status'] != 'Concluido')]


#A
print(df_track['gastos'].mean())
print()


#B
print(df_traitor)
print()

#C
df_competitor = df4[['nome', 'gastos', 'status']].copy()
df_competitor = df_competitor.loc[(df_competitor['status'] != 'Concluido') & (df_competitor['gastos'] > 0)].drop_duplicates(subset='nome') # Through this, we see that many people didn't pay AT but went at any show, so the she/he bought with a competitor
print(df_competitor)
print()

more_expensiveDay = (df4[['dia', 'gastos', 'status']].groupby('dia')).sum().sort_values(by='gastos', ascending=False)
print(more_expensiveDay.iloc[[0]])
print()

# the graph helps us to verify that day 1 is the day where the people cast the biggest amount of money
fig = plt.figure()
x = np.array(["1", "2", "3"])
y = np.array([258179.72, 255496.88, 128937.37])
plt.title("Money spent in shows")
plt.ylabel("Amount of money spent")
plt.xlabel("Days")
plt.bar(x,y)
plt.show()

#E
show_list = [show for show in df_day['show']]
money_list = [money for money in df_day['gastos']]
names_list = [name for name in df_day['nome']]

core_titles = [{"nome": i, "gastos": j, "shows": k} for i, j, k in zip(names_list, money_list, show_list)]

print(json.dumps(core_titles))
