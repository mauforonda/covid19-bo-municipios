#!/usr/bin/env python3

import requests
import pandas as pd
from io import StringIO
from datetime import datetime, timedelta

def update():
  url = 'https://juliael.carto.com/api/v2/sql?filename=capital_municipios_covid19&q=SELECT+*+FROM+(select+*+from+public.capital_municipios_covid19)+as+subq+&format=csv&bounds=&api_key=&skipfields=the_geom_webmercator'
  yesterday = (datetime.today()-timedelta(days=1)).strftime('%Y-%m-%d')
  filename = 'data/{}.csv'.format(yesterday)
  response = requests.get(url).content
  df = pd.read_csv(StringIO(response.decode('utf-8')))
  df[['cod_ut', 'positivos', 'recuperados', 'decesos']] = df[['cod_ut', 'positivos', 'recuperados', 'decesos']].fillna(0).apply(lambda x: pd.to_numeric(x, downcast='integer'))
  df[['municipio', 'cod_ut', 'positivos', 'recuperados','decesos']].to_csv(filename, index=False, header=['municipio', 'cod_ine', 'confirmados', 'recuperados', 'decesos'])
  print(yesterday)

update()
