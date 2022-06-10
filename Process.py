from unicodedata import name
from matplotlib.font_manager import json_dump
import matplotlib.pyplot as plt
import numpy as np
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
df_track_concluded = df4.loc[(df4['tipo'] == 'Pista') & (df4['status'] == 'Concluido')] # for analizing the difference beetween the mean of rows with 'pista' status and 'pista' and 'concluido' status

df_days = df4[(df4['status'] != 'Concluido')]
df_res = df_days.drop(df_days.columns[[0, 1, 2, 4, 5]], axis=1)


#1)
print('\nAmount cast without the concluded status: {:.2f}\nAmount cast with concluded status: {:.2f}'.format(df_track['gastos'].mean(), df_track_concluded['gastos'].mean()))
print()


#2)
 
 # -> all people went at any show 'cause everyone cast some money 

#3)
print('\nPeople that didnt buy tickets with AT: \n')
competitor_names = df4.loc[(df4['status'] != 'Concluido') & (df_res["gastos"] > 0), "nome"].drop_duplicates()
competitor_names = competitor_names.drop([18, 30, 83, 115, 162, 262, 282, 295, 324, 336]) # names with 'Concluido' and 'Nao Concluido' or 'Problema no pagamento' either
print(competitor_names)
print()

#4)
print('\nDay With biggest amount of casts: \n')
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

#5)
result = df_res.to_json(orient="records")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))
