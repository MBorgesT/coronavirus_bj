from tabela import sheet, wb
import xlrd, datetime
import matplotlib.pyplot as plt
import numpy as np

float_dates = sheet.col_values(0)
del float_dates[0]
dates = []
for cell in float_dates:
	aux = datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode))
	dates.append(aux.strftime('%d/%m'))


bji_casos_conf = sheet.col_values(1)
del bji_casos_conf[0]


bjn_casos_conf = sheet.col_values(8)
del bjn_casos_conf[0]
ant = 0
for i in range(len(bjn_casos_conf)):
	if bjn_casos_conf[i] == '':
		bjn_casos_conf[i] = ant
	else:
		ant = bjn_casos_conf[i]

casos_somados = []
for i in range(len(bji_casos_conf)):
	casos_somados.append(bjn_casos_conf[i] + bji_casos_conf[i])

fig, ax = plt.subplots()
ax.plot(bji_casos_conf, label='BJI')
ax.plot(bjn_casos_conf, label='BJN')
ax.plot(casos_somados, label='Casos somados')
ax.set(title='Casos de COVID-19 nas cidades de BJI e BJN', xlabel='Dias desde o primeiro caso confirmado', ylabel='Número de casos')
ax.grid()

plt.xticks(np.arange(0, len(bjn_casos_conf), 7))
plt.legend(loc='upper left')
plt.savefig('grafico_casos_confirmados.png')