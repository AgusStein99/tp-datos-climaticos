
# analisis_datos.py
# Análisis de datos climáticos históricos - Mendoza 2015-2024
# Autor: Agustín Stein | Rol: Paco (Desarrollador Técnico)

import pandas as pd
import matplotlib.pyplot as plt

# --- Carga de datos ---
# Ruta relativa para garantizar reproducibilidad en Colab
df = pd.read_csv("datos/dataset.csv")

# --- Indicadores básicos ---
# Calculamos estadísticas descriptivas de temperatura
temp_promedio = df["temperatura"].mean()
temp_max = df["temperatura"].max()
temp_min = df["temperatura"].min()
precip_promedio = df["precipitacion"].mean()

print("=== INDICADORES CLIMÁTICOS ===")
print(f"Temperatura promedio: {temp_promedio:.2f}°C")
print(f"Temperatura máxima:   {temp_max:.2f}°C")
print(f"Temperatura mínima:   {temp_min:.2f}°C")
print(f"Precipitación promedio: {precip_promedio:.2f}mm")

# --- Generación del gráfico ---
# Visualizamos la evolución de temperatura en el tiempo
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df["fecha"], df["temperatura"], color="tomato", linewidth=1.5, label="Temperatura (°C)")
ax.set_title("Evolución de la Temperatura - Mendoza 2015-2024")
ax.set_xlabel("Fecha")
ax.set_ylabel("Temperatura (°C)")

# Mostramos solo algunas fechas en el eje X para no saturarlo
step = len(df) // 10
ax.set_xticks(range(0, len(df), step))
ax.set_xticklabels(df["fecha"].iloc[::step], rotation=45, ha="right")

ax.legend()
plt.tight_layout()

# Guardamos en /resultados para cumplir con la estructura del proyecto
plt.savefig("resultados/grafico_temperatura.png", dpi=150)
plt.show()
print("Gráfico guardado en /resultados")
