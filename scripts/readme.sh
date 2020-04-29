#!/usr/bin/env bash
days=( $(ls -r data | head -n 10) )
echo -e "> Datos de casos de covid19 en Bolivia por municipio, reportados diariamente.\n\n" > readme.md
echo -e "## Contenidos\n\n- [Cambios en el último día](#cambios-en-el-último-día)\n\n- [Municipios ordenados según el porcentaje de casos confirmados en la población](#municipios-ordenados-según-el-porcentaje-de-casos-confirmados-en-la-población)\n\n- [Cambios en la última semana](#cambios-en-la-última-semana)\n\n\n\n" >> readme.md
echo -e "## Cambios en el último día\n\n" >> readme.md
daff --padding sparse --context 0 --unordered --output-format html --fragment "data/${days[1]}" "data/${days[0]}">> readme.md
echo -e "\n\n+++ : nuevo municipio\n\n→ : nuevos casos\n\n" >> readme.md
echo -e "## Municipios ordenados según el porcentaje de casos confirmados en la población\n\n" >> readme.md
python3 scripts/rank.py
echo -e "\n\nEl ranking sólo considera municipios con Código INE.\n\n" >> readme.md
echo -e "## Cambios en la última semana\n\n" >> readme.md
daff --padding sparse --context 0 --unordered --output-format html --fragment "data/${days[7]}" "data/${days[0]}">> readme.md
echo -e "\n\n+++ : nuevo municipio\n\n→ : nuevos casos\n\n" >> readme.md
echo -e '\n\n---\n\nActualizo los datos a medio día (GMT-4) para el día anterior.' >> readme.md
