import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## Samuel Martinez NC 0096

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de dispositivos con 4 elementos por lista
chr = ['Chromecast HD', 29.99, True, 1.5]
frt = ['Fire TV Stick 4K', 49.99, True, 2.0]
rku = ['Roku Express', 24.99, True, 1.0]
app = ['Apple TV 4K', 129.00, True, 4.0]
nvd = ['Nvidia Shield', 199.99, True, 3.0]

# Creamos una lista de listas ( conformando la tabla)
lista_dispositivos = [chr, frt, rku, app, nvd]
#print(lista_dispositivos)

# Utilizar panda para organizar la tabla (DataFrame o marco de datos)
# a cada columna le ponemos nombre
df_dispositivos = pd.DataFrame(lista_dispositivos, columns=["Modelo", "Precio_USD", "Incluye_Control", "RAM_GB"])
print(df_dispositivos)

# creamos el archivo CSV y lo guardamos en CSV
df_dispositivos.to_csv("dispositivos.csv", index=False)

# crear grafica de lineas
# donde X es Modelo en el eje horizontal
# donde Y es Precio_USD en el eje vertical
plt.plot(df_dispositivos["Modelo"], df_dispositivos["Precio_USD"])
plt.title("Grafica dispositivos 0096")
plt.xlabel("Modelo de los dispositivos")
plt.ylabel("Precio en USD")
plt.show()

# Creamos una grafica de puntos
plt.scatter(df_dispositivos["Modelo"], df_dispositivos["Precio_USD"])
plt.show()

# Grafica de barras
plt.bar(df_dispositivos["Modelo"], df_dispositivos["Precio_USD"])
#Etiquetas y titulo
plt.title("Grafica dispositivos 0096")
plt.xlabel("Modelo de los dispositivos")
plt.ylabel("Precio en USD")
#Mostrar la grafica
plt.show()

# ordenar la grafica de barras de manera descendente
# de la mas grande a la mas pequeña
df_disp_ordenar = df_dispositivos.sort_values("Precio_USD", ascending=False)
plt.bar(df_disp_ordenar["Modelo"], df_disp_ordenar["Precio_USD"])
plt.show()

# coloreando la grafica
df_disp_ordenar = df_dispositivos.sort_values("Precio_USD", ascending=False)
plt.bar(df_disp_ordenar["Modelo"], df_disp_ordenar["Precio_USD"],
        color=["b", "g", "c", "m", "y"])
plt.show()

## grafica de pastel
plt.pie(df_dispositivos["Precio_USD"], labels=df_dispositivos["Modelo"])
plt.show()
print("Samuel Martinez NC 0096")