# 🚀 ETL de Datos Financieros con Airflow y Docker  

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** para analizar gastos financieros personales, utilizando **Apache Airflow** dentro de contenedores Docker.  

El objetivo es mostrar habilidades en:  
- Construcción de pipelines de datos reproducibles  
- Orquestación con Airflow  
- Limpieza, transformación y carga de datos  
- Visualización y análisis financiero

⚙️ Requisitos Previos

Docker Desktop
 instalado y corriendo

WSL2
 habilitado (en Windows)

Verifica instalación con:

docker --version
docker compose version

▶️ Instrucciones de Uso

Clonar el repositorio

Levantar los servicios de Airflow

docker compose up -d


Abrir la interfaz de Airflow
👉 http://localhost:8080

Usuario: admin

Contraseña: admin

Activar y ejecutar el DAG

Entra al DAG etl_finanzas

Actívalo (switch ON)

Haz clic en Trigger DAG para ejecutarlo manualmente

Ver resultados
El pipeline generará un archivo:

data/resumen_gastos_mensual.csv

con el gasto total agrupado por mes y categoría.



📊 Funcionalidades del Pipeline

Extracción (Extract): lectura de transacciones desde CSV

Transformación (Transform):

Conversión de fechas

Agrupación por mes y categoría

Cálculo de totales

Carga (Load): exporta los resultados en un CSV listo para análisis

Orquestación: Airflow gestiona la secuencia ETL y programaciones



🧰 Tecnologías Utilizadas

Apache Airflow (orquestación de workflows)

Docker & Docker Compose (contenedores)

Python 3.12

Pandas (procesamiento de datos)



👤 Autor

Proyecto desarrollado por mi persona Freddy De la cruz , como parte de un portafolio en Ingeniería de Datos.



🚀 Nota 

Este proyecto demuestra la capacidad de:

Diseñar un pipeline ETL realista y automatizado

Integrar herramientas de orquestación modernas (Airflow)

Manejar entornos reproducibles con Docker

Documentar de manera clara para su despliegue inmediato

---

## 📂 Estructura del Proyecto  

```text
etl_finanzas_airflow/
├── dags/
│   └── etl_finanzas_dag.py      # DAG principal de Airflow
├── etl/
│   ├── extract.py                # Extracción de datos desde CSV
│   ├── transform.py              # Transformaciones con pandas
│   └── load.py                   # Carga de resultados en CSV
├── data/
│   └── transacciones_financieras.csv   # Dataset de ejemplo
├── logs/                         # Logs generados por Airflow (ignorado en git)
├── docker-compose.yaml           # Orquestación de servicios con Docker
├── Dockerfile (opcional)         # Para instalar dependencias extra (ej. pandas)
└── README.md                     # Este documento


