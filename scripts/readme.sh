#!/usr/bin/env bash
days=( $(ls -r data | head -n 10) )
echo -e "> Datos de casos de covid19 en Bolivia por municipio, reportados diariamente.\n\n" > readme.md

echo -e "\n\n- [Cambios en el último día](#cambios-en-el-último-día)\n\n- [Cambios en la última semana](#cambios-en-la-última-semana)\n\n- [Municipios más afectados](#municipios-más-afectados)\n\n\n\n" >> readme.md

echo -e "## Cambios en el último día\n\n" >> readme.md
daff --padding sparse --context 0 --unordered --output-format html --fragment "data/${days[1]}" "data/${days[0]}">> readme.md
echo -e "\n\n+++ : nuevo municipio\n\n→ : nuevos casos\n\n" >> readme.md

echo -e "## Cambios en la última semana\n\n" >> readme.md
python3 scripts/trend.py

echo -e "\n\n## Municipios más afectados\n\nLos 20 municipios con mayor proporción de su población infectada.\n\n" >> readme.md
python3 scripts/rank.py
