#!/usr/bin/env python3

import pandas as pd
from datetime import datetime, timedelta

def make_matchlist(m, p):
  p['capital'] = p['capital'].apply(lambda x: x.title())
  matches = []
  for cod in m['cod_ine']:
    match = p[p['cod_ine'] == cod][['departamento', 'capital', 'poblacion']].values.tolist()
    if len(match) != 0:
      matches.append(match[0])
    else:
      matches.append(['','',0])
  return matches

def make_percetages(m):
  percent = []
  for i in m[['confirmados', 'poblacion']].values.tolist():
    if i[1] !=0:
      percent.append((i[0] / i[1]) * 100)
    else:
      percent.append(0)
  return percent
  
municipios = 'data/{}.csv'.format((datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'))
m = pd.read_csv(municipios)
p = pd.read_csv('scripts/poblacion.csv')

m[['departamento', 'capital', 'poblacion']] = pd.DataFrame(make_matchlist(m, p))
m['percent'] = pd.DataFrame(make_percetages(m))
with open('readme.md', 'a') as f:
  m[(m['cod_ine'] != 0) & (m['confirmados'] > 0)].sort_values('percent', ascending=False).head(20)[['municipio', 'confirmados', 'poblacion', 'percent']].to_markdown(f, headers=['Municipio', 'Confirmados', 'Población', '%'], tablefmt='github', showindex=False, floatfmt=".3f")
