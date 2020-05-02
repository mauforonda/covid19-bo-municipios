#!/usr/bin/env python3

import pandas as pd
from datetime import datetime, timedelta

municipios = 'data/{}.csv'.format((datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'))
ayer = pd.read_csv(municipios)
vulnerabilidad = pd.read_csv('scripts/vulnerabilidad.csv')
vulnerabilidad = vulnerabilidad.set_index('cod_ine')

df = ayer[ayer['cod_ine'] != 0][['cod_ine', 'municipio', 'confirmados', 'decesos']]
df = df.set_index('cod_ine')
df2 = df.merge(vulnerabilidad, left_index=True, right_index=True)

with open('readme.md', 'a') as f:
  df2[['municipio', 'confirmados', 'decesos', 'establecimientos', 'poblacion_mayor']].sort_values('confirmados', ascending=False).head(20).to_markdown(f, headers=['Municipio', 'Confirmados', 'Decesos', 'Establecimientos de Salud', 'Población mayor a 65 años (%)'], tablefmt='github', showindex=False, floatfmt=".3f")
