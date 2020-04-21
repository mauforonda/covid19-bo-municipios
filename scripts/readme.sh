#!/usr/bin/env bash
days=( $(ls -r data | head -n 2) )
echo -e "Datos de casos de covid19 en Bolivia por municipio, reportados diariamente.\n\nCambios en el último día:\n\n" > readme.md
daff --padding sparse --context 0 --unordered --output-format html --fragment "data/${days[1]}" "data/${days[0]}">> readme.md
echo -e "\n+++ : nuevo municipio\n\n→ : nuevos casos" >> readme.md
