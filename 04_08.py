'''
Clase miercoles 08 de abril
Lo que vamos a ver en este script:
-Terminar pandas
- Ver libreria numpy
- Ver libreria matplotlib
'''
import pandas as pd

# #* Tabajar con modelos de bloques
# df = pd.read_csv('data.txt', sep='\t')
# #sep = ','   ';'    '|'   '\s+'
# print(df.head())


# #Ejercicio cortar el modelo de bloques desde el punto central en (x, y) + 100m hacia los laterales
# x_median = df['x'].median()
# y_median = df['y'].median()

# df = df[(df['x'] >= x_median - 100) & (df['x'] <= x_median + 100)]
# df = df[(df['y'] >= y_median - 100) & (df['y'] <= y_median + 100)]

# #Ejercico crear una columna de 'Valor_Bloque'
# df['Valor_Bloque'] = 0

# p_cu = 5.5 # [USD/lb]
# c_v = 1.2  # [USD/lb]
# c_m = 20 # [USD/ton] 
# c_p = 21 # [USD/ton]
# rec = 0.85 # [%]
# den = 2.7 # [ton/m3]
# ton = 1000 * den
# cte = 2204.62 

# df['Valor_Bloque'] = ton*(((p_cu - c_v) * rec * (df['ley']/100) * cte) - (c_m + c_p))


# df['state'] = 0
# # Estado de bloques (si son rentables o no)
# #ej 1
# for i in range(0, len(df)):
#     if df.iloc[i]['Valor_Bloque'] >= 0:
#         df.iat[i, 5] = 1

# #ej 2
# for indice, fila in df.iterrows():
#     if fila['Valor_Bloque'] > 0:
#         fila['state'] == 1

# print(df.head())
# print(df.describe())

#tarea contar los bloques con state 0 y 1

#   LIBRERIA NUMPY
import numpy as np

#   LIBRERIA MATPLOTLIB
import matplotlib.pyplot as plt

# #Datos del ejemplo
# tiempo = np.arange(0, 20, 0.5)
# temperatura = 20 + 5 * np.sin(tiempo/2)
# presion = 100 + 50 * np.exp(tiempo/10)

# fig, ax1 = plt.subplots(figsize=(10,5))

# #Eje Vertical
# ax1.set_xlabel('Tiempo [hrs]')
# ax1.set_ylabel('Temperatura [ºC]', color = 'tab:red')
# ax1.plot(tiempo, temperatura, color='tab:red', label='Temp', linewidth=2)
# ax1.tick_params(axis='y', labelcolor='tab:red')

# #Segundo eje Vertical
# ax2 = ax1.twinx()
# ax2.set_ylabel('Presion [hPa]', color = 'tab:blue')
# ax2.plot(tiempo, presion, color='tab:blue', label='Presion', linestyle='--')
# ax2.tick_params(axis='y', labelcolor='tab:blue')

# plt.title('Monitoreo de Sistema: Temperatura vs Presion')
# fig.tight_layout()
# plt.show()

#Ejemplo 2
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8,4))
plt.plot(x, y, label='Seno(x)', color='blue')
plt.title('Funsion sen()')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()