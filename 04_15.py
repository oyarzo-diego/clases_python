'''
Hoy veremos:
1. Libreria plotly
2. Presentacion del problema y grupo
3. Ejercicios
'''

# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('data.txt', sep='\t')
# print(df.head())

# fig = px.histogram(
#     df, # de donde se obtienen los datos
#     x = 'ley', # variable que quiero graficar
#     y = None, # contar diferente a frecuencia
#     color = None, # 'ley'
#     nbins = 50, # numero de barras
#     barmode = 'stack', # 'overlay' 'relative'
#     histnorm = 'percent', # normalizacion de la grafica 'probability'
#     marginal = 'box', # grafico adicional 'rug' 'violin'
#     title = ' Histograma de ley'
# )
# fig.show()

# df = df[(df['z'] >= 2900) & (df['z'] <= 3300)]
# df = df[(df['x'] >= 24250) & (df['x'] <= 24450)]
# df = df[(df['y'] >= 24550) & (df['y'] <= 24750)]
# df = df[df['ley'] > 0.8]

# import plotly.graph_objects as go

# fig2 = go.Figure(data = [go.Scatter3d(
#     x = df['x'],
#     y = df['y'],
#     z = df['z'],
#     mode = 'markers',
#     marker = dict(
#         size = 8,
#         color = df['ley'],
#         symbol = 'circle',
#         colorscale = 'jet',
#         colorbar = dict(title='Ley de Cu outlier', orientation='v'), 
#         showscale = True,
#         #text = ''
#         #hoverinfo = 'text'   
#     )
# )])

# fig2.update_layout(
#     scene=dict(
#         xaxis_title = 'Easting',
#         yaxis_title = 'Northing',
#         zaxis_title = 'Elevation',
#         aspectmode = 'data'
#     ),
#     margin = dict(l=10, r=10, b=10, t=10)
# )

# fig2.show()

##################################
##### generar los grupos #########
##################################

import numpy as np
#creacion de array con el numero de lista de cada alumno
lista_original = np.arange(1, 10)
print(lista_original)

#Ordenar la lista de forma aleatoria varias veces
#vamos a crear un bucle de "mezclado"

n_mezcla = 400
for _ in range(n_mezcla):
    np.random.shuffle(lista_original)
print (lista_original)

#reshape --> "matriciar"
resultado = lista_original.reshape(3, 3)
print(resultado)