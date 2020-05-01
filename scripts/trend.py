#!/usr/bin/env python3

import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import rcParams
import time

def init():
  yesterday = last_week[0]
  df = pd.DataFrame()
  day_df = pd.read_csv(f'data/{yesterday}.csv')
  df['municipio'] = day_df['municipio']
  df[yesterday] = day_df['confirmados']
  return df

def make_df(last_week):
  df = init()
  for day in last_week[1:]:
    confirmados = []
    day_df = pd.read_csv(f'data/{day}.csv')
    for m in df['municipio']:
      day_m = day_df[day_df['municipio'] == m]
      if len(day_m) == 0:
        confirmados.append(0)
      else:
        confirmados.append(day_m['confirmados'].values[0])
    df[day] = pd.Series(confirmados)
  return df

def make_table(df):
  table = []
  for i in range(0,len(df)):
    m = df.iloc[i]
    path = make_plot(m[0], m[1:])
    table.append([m[0],m[1], m[1] - m[-1], '<img src="{}"/>'.format(path)])
  with open('readme.md', 'a') as f:
    pd.DataFrame(table, columns=['Municipio', 'Confirmados', 'Nuevos', 'Tendencia']).sort_values('Confirmados', ascending=False).to_markdown(f, tablefmt='github', showindex=False)

def make_plot(name, series):
  output = 'scripts/plots/{}.png'.format(name.strip().lower().replace(" ", "-"))
  fig = series.sort_index().plot(figsize=(1,0.3), rot=0, legend=False, color='#e23e57', linewidth=2).get_figure()
  plt.box(False)
  plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
  plt.grid(False)
  plt.savefig(output, bbox_inches='tight')
  plt.close()
  return output

last_week = [(datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1,8)]
df = make_df(last_week)
make_table(df)

