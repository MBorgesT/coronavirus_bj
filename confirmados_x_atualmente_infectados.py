from tabela import sheet
import matplotlib.pyplot as plt
import numpy as np

from casos_confirmados import casos_somados as casos_confirmados
from atualmente_infectados import cidades_somado as atualmente_infec


fig, ax = plt.subplots()
ax.plot(casos_confirmados, label='Casos confirmados totais')
ax.plot(atualmente_infec, label='Atualmente infectados')
ax.set(title='Casos totais confirmados por atualmente infectados', xlabel='Dias desde o primeiro caso confirmado', ylabel='Número de casos')
ax.grid()

plt.xticks(np.arange(0, len(atualmente_infec), 7))
plt.legend(loc='upper left')
plt.savefig('grafico_confirmados_x_atualmente_infectados.png')