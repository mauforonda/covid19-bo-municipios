#!/usr/bin/env bash
days=( $(ls -r data | head -n 10) )
echo -e "> Datos de casos de covid19 en Bolivia por municipio, reportados diariamente.\n\n" > readme.md

echo -e "\n\n- [Cambios en el último día](#cambios-en-el-último-día)\n\n- [Cambios en la última semana](#cambios-en-la-última-semana)\n\n- [Municipios más afectados](#municipios-más-afectados)\n\n" >> readme.md

echo -e "\n\n## Cambios en el último día\n\n" >> readme.md
daff --padding sparse --ignore "cod_ine" --context 0 --unordered --output-format html --fragment "data/${days[1]}" "data/${days[0]}" | sed 's/@@//g' | sed 's/→/ → /g' | sed 's/+++/ ➕ /g'>> readme.md

echo -e "\n\n## Cambios en la última semana\n\n" >> readme.md
python3 scripts/trend.py

echo -e "\n\n## Municipios más afectados\n\nLos 20 municipios con mayor proporción de su población infectada.\n\n" >> readme.md
python3 scripts/rank.py

echo -e "\n\n---\n\nLos datos se actualizan a medio día (GMT-4) para casos del día anterior.\n\n" >> readme.md
