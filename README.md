# Análisis de Datos Climáticos - Mendoza 2015-2024

## Integrantes
| Rol | Nombre |
|-----|--------|
| P1 - Líder y Organizador (Hugo) | Agustín Stein |
| P2 - Desarrollador Técnico (Paco) | Agustín Stein |
| P3 - Revisor y QA (Luis) | Agustín Stein |

## Escenario elegido
Escenario A – Análisis de Datos Climáticos

## Descripción del dataset
Dataset simulado de registros mensuales de temperatura y precipitaciones
correspondientes a la ciudad de Mendoza, Argentina, para el período 2015-2024.
Contiene 120 registros con las siguientes columnas:
- `fecha`: mes y año del registro (formato YYYY-MM)
- `temperatura`: temperatura promedio mensual en °C
- `precipitacion`: precipitación mensual en mm

## Estructura del repositorio
tp-datos-climaticos/
├── datos/
│   └── dataset.csv
├── scripts/
│   └── analisis_datos.py
├── resultados/
│   └── grafico_temperatura.png
├── README.md
└── .gitignore
## Instrucciones para ejecutar el script

1. Abrí [Google Colab](https://colab.research.google.com)
2. Cloná el repositorio:
```bash
!git clone https://github.com/AgusStein99/tp-datos-climaticos.git
%cd tp-datos-climaticos
```
3. Ejecutá el script:
```bash
%run scripts/analisis_datos.py
```
4. El gráfico se guardará automáticamente en `/resultados`.

## Gestión del proyecto
Las tareas fueron gestionadas mediante Jira siguiendo el mandato de trazabilidad.
Cada commit referencia el Issue correspondiente con el formato `PROY-N: descripción`.
