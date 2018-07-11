# Lista de SICs brasileiros

Data package com lista de SICs brasileiros extraídos do
http://www.acessoainformacao.gov.br/lai-para-sic/sic-apoio-orientacoes/lista-de-sics

## Dados

Os dados foram extraídos de http://www.acessoainformacao.gov.br/lai-para-sic/sic-apoio-orientacoes/lista-de-sics, com as seguintes modificações:

* Conversão para CSV
* Retirada de acentos, troca de espaços por underscores (\_), e colocados em
  minúsculas
* Retirada de espaços em branco no começo ou fim de cada célula

Essas modificações são feitas pelo script em
[scripts/clean_csv.py](scripts/clean_csv.py), sendo a conversão para CSV feita
pelo LibreOffice em [Makefile](Makefile).
