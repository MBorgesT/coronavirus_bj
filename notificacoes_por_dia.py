from tabela import sheet
import matplotlib.pyplot as plt
import numpy as np


bji_suspeitas = sheet.col_values(6)
del bji_suspeitas[0]

bji_descartados = sheet.col_values(7)
del bji_descartados[0]

bji_casos_conf = sheet.col_values(1)
del bji_casos_conf[0]

bji_novas_suspeitas = [0]
for i in range(1, len(bji_casos_conf)-4):
	aux = 0
	aux += bji_suspeitas[i] - bji_suspeitas[i-1]
	aux += int(bji_descartados[i]) - int(bji_descartados[i-1]) 
	aux += int(bji_casos_conf[i]) - int(bji_casos_conf[i-1])
	bji_novas_suspeitas.append(aux)


fig, ax = plt.subplots()
ax.plot(bji_novas_suspeitas)
ax.set(title='Novos casos suspeitos por dia em BJI', xlabel='Dias desde o primeiro caso confirmado', ylabel='Número de notificações do dia')
ax.grid()

plt.xticks(np.arange(0, len(bji_casos_conf), 7))
plt.savefig('grafico_notificações_por_dia.png')
