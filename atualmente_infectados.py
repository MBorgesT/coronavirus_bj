from tabela import sheet
import matplotlib.pyplot as plt
import numpy as np


bji_casos_conf = sheet.col_values(1)
del bji_casos_conf[0]

bji_curados = sheet.col_values(3)
del bji_curados[0]

bji_atualmente_infectados = []
for a, b in zip(bji_casos_conf, bji_curados):
	bji_atualmente_infectados.append(a-b)


# já preenchido as células vazias
from casos_confirmados import bjn_casos_conf

bjn_curados = sheet.col_values(10)
del bjn_curados[0]
ant = 0
for i in range(len(bjn_curados)):
	if bjn_curados[i] == '':
		bjn_curados[i] = ant
	else:
		ant = bjn_curados[i]

bjn_atualmente_infectados = []
for a, b in zip(bjn_casos_conf, bjn_curados):
	bjn_atualmente_infectados.append(a-b)



cidades_somado = []
for a, b in zip(bji_atualmente_infectados, bjn_atualmente_infectados):
	cidades_somado.append(a+b)



fig, ax = plt.subplots()
ax.plot(bji_atualmente_infectados, label='BJI')
ax.plot(bjn_atualmente_infectados, label='BJN')
ax.plot(cidades_somado, label='Soma das cidades')
ax.set(title='Pessoas atualmente infectadas', xlabel='Dias desde o primeiro caso confirmado', ylabel='Número de pessoas infectadas e ainda não curadas')
ax.grid()

plt.xticks(np.arange(0, len(bji_curados), 7))
plt.legend(loc='upper left')
plt.savefig('grafico_atualmente_infectados.png')