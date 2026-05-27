
# Bank Marketing Campaign Analysis

## 1. Introducción

Las campañas de marketing bancario representan una de las principales herramientas utilizadas por las entidades financieras para promocionar productos y servicios entre sus clientes. Sin embargo, la efectividad de estas campañas depende de múltiples factores relacionados con el comportamiento del cliente, la estrategia comercial utilizada y el contexto económico.

El presente proyecto desarrolla un análisis exploratorio de datos (EDA) sobre un conjunto de datos de campañas de marketing directo de una institución bancaria portuguesa, con el objetivo de identificar patrones, tendencias y variables relacionadas con la suscripción de un producto financiero.

A través de técnicas de limpieza, transformación y análisis de datos, se busca extraer insights de negocio que permitan comprender mejor qué factores influyen en la conversión de clientes y cómo podrían optimizarse futuras campañas comerciales.

---

# 2. Objetivos del proyecto

El objetivo principal del proyecto es analizar el comportamiento de los clientes durante campañas de marketing bancario para identificar factores relacionados con la suscripción del producto ofrecido.

Los objetivos específicos del análisis son:

- Realizar una exploración inicial del dataset.
- Limpiar y transformar los datos para garantizar su calidad.
- Identificar patrones de comportamiento de los clientes.
- Analizar variables demográficas, económicas y comerciales.
- Detectar factores asociados a una mayor probabilidad de conversión.
- Extraer insights de negocio orientados a la optimización de campañas comerciales.
- Generar una base sólida para futuros modelos predictivos de clasificación.

---

# 3. Descripción del dataset

El dataset utilizado contiene información relacionada con campañas de marketing realizadas por una entidad bancaria.

El conjunto de datos incluye variables relacionadas con:

- Características demográficas y comportamiento de compra del cliente.
- Historial financiero.
- Información sobre campañas de marketing.
- Variables macroeconómicas.
- Variables temporales y geográficas.

La variable objetivo del análisis es y

que indica si el cliente suscribió (yes) o no (no) el producto financiero ofrecido durante la campaña.

El dataset final utilizado en el análisis contiene aproximadamente:

Más de 42.000 registros.
38 variables.

---

# 4. Tecnologías utilizadas

- Python
- pandas
- numpy
- matplotlib
- seaborn
- Jupyter Notebook
- Git
- GitHub

---

# 5. Estructura del proyecto

El proyecto se organizó en distintos notebooks siguiendo un flujo estructurado de análisis de datos.

```text
│
├── datos/
│   ├── datos_brutos/
│   └── datos_transformados/
│
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   ├── 03_eda.ipynb
│  
│
├── informes/
│   └── informe_analisis.md
│
├── src/
│   ├── cleaning.py
│   ├── utils.py
│   
│
├── README.md
│ 
├── DataProject_ Proyecto EDA con Python.docx
│ 
├── .gitignore
│
└── requirements.txt
```
---

# 6. Proceso de limpieza de datos

El proceso de limpieza permitió transformar el dataset original en un conjunto de datos consistente y preparado para el análisis exploratorio.

Las principales tareas realizadas fueron:

# 6.1 Revisión de tipos de datos

Se revisaron y ajustaron los tipos de variables:

- numéricas,
- categóricas,
- binarias,
- y temporales.

# 6.2 Limpieza de columnas numéricas

Se verificaron:

- formatos
- coherencia
- valores atípicos y posibles inconsistencias
 

# 6.3 Conversión de variables binarias

Variables como:

- default
- housing
- loan

Fueron convertidas a formatos categóricos más interpretables (yes / no).

# 6.4 Limpieza de fechas

La variable date fue transformada a formato datetime para permitir análisis temporales.

# 6.5 Tratamiento de valores nulos

Se identificaron variables con valores faltantes y se aplicaron distintas estrategias de imputación:

- 1.Variables numéricas

    - 1.1 Imputación mediante mediana.

- 2. Variables categóricas
 
  - 2.1 Imputación mediante la categoría: Unknown
   
- 3. Variables binarias (housing y loan)
 
  - 3.1. Imputación mediante la moda.

Esta estrategia permitió:

- conservar registros
- minimizar pérdida de información
- mantener consistencia analítica.
 

# 6.6 Eliminación de registros inconsistentes

Se eliminaron registros con fechas inválidas o inconsistencias críticas que podían afectar al análisis.

---

# 7. Feature engineering

Se crearon nuevas variables derivadas para enriquecer el análisis y facilitar la interpretación de resultados.

Las principales variables generadas fueron:

| Variable                 | Descripción                                          |
| ------------------------ | ---------------------------------------------------- |
| duration_min             | Duración de llamada en minutos                       |
| contact_year             | Año de contacto                                      |
| contact_month            | Mes de contacto                                      |
| age_group                | Grupo de edad                                        |
| previous_contact         | Indicador de contacto previo                         |
| customer_seniority_days  | Antigüedad del cliente en días                       |
| customer_seniority_years | Antigüedad del cliente en años                       |
| customer_year            | Año de alta del cliente                              |
| customer_month           | Mes de alta del cliente                              |



---

# 8. Análisis exploratorio

El análisis exploratorio permitió identificar patrones relevantes relacionados con la suscripción del producto financiero.

# 8.1 Variable objetivo

La variable objetivo presenta un fuerte desbalanceo:

- Aproximadamente el 89% de los clientes no suscribieron el producto, mientras que solo alrededor del 11% sí realizaron la contratación.
 

# 8.2 Variables comerciales

Las variables relacionadas con la interacción comercial mostraron gran influencia sobre la conversión.

Especialmente:

- duration
- campaign
- previous
- poutcome
 

# 8.3 Variables sociodemográficas

Se observaron diferencias relevantes según:

- ocupación
- nivel educativo
- antigüedad del cliente
 

# 8.4 Variables macroeconómicas

Variables como:

- euribor3m
- emp.var.rate
- nr.employed

presentaron relación con el comportamiento de contratación.

# 8.5 Análisis temporal

El análisis temporal mostró:

- estabilidad relativa de campañas
- diferencias de conversión según antigüedad del cliente
 

# 8.6 Análisis geográfico

No se identificaron patrones geográficos relevantes relacionados con la conversión.

# 8.7 Correlaciones

Las correlaciones más relevantes se observaron en:

- duration
- pdays
- previous
- variables macroeconómicas.
 

# 8.8 Outliers

Los principales outliers aparecieron en:

- duration
- campaign
- previous
- pdays

Sin embargo, la mayoría parecían reflejar comportamientos reales del negocio y no errores de calidad de datos.

---

# 9. Principales insights de negocio

# 9.1 Las llamadas más largas aumentan significativamente la conversión

La duración de la llamada fue la variable más correlacionada positivamente con la suscripción.

Esto sugiere que:

- conversaciones más extensas
- reflejan mayor interés o engagement del cliente
 

# 9.2 El exceso de contactos reduce la efectividad comercial

Clientes altamente contactados:

- no presentan mayores tasas de conversión e incluso muestran menor efectividad comercial.

Esto podría indicar:

- fatiga comercial
- estrategias de contacto poco eficientes
 

# 9.3 Los clientes con campañas previas exitosas convierten mucho más

El historial positivo de campañas anteriores fue uno de los factores más relevantes de conversión.

Los clientes con:

poutcome = success

presentaron una probabilidad significativamente mayor de suscripción.

# 9.4 Los clientes recientes convierten mejor

La conversión disminuye conforme aumenta la antigüedad del cliente.

Esto sugiere que:

Los clientes más nuevos son más receptivos a nuevas ofertas comerciales.
 

# 9.5 El canal móvil resulta más efectivo

El contacto mediante:

cellular

presentó mejores resultados que el contacto telefónico tradicional.

# 9.6 Las variables geográficas tienen baja relevancia

No se identificaron patrones territoriales relevantes relacionados con la conversión.

---

# 10. Conclusiones finales

El análisis exploratorio realizado permitió identificar múltiples factores relacionados con el éxito de las campañas de marketing bancario.

Los resultados muestran que:

La conversión depende principalmente de variables comerciales, del historial previo del cliente y de ciertos factores económicos y demográficos.

Entre las variables más relevantes destacan:

- la duración de la llamada
- el número de contactos
- la antigüedad del cliente
- los resultados de campañas anteriores.

Además:

Se observó que estrategias comerciales excesivamente insistentes
pueden reducir la efectividad de la campaña.

El proyecto también permitió comprobar que:

No todos los outliers representan errores, y que muchos contienen información valiosa sobre el comportamiento real de los clientes.

Finalmente, el análisis proporciona una base sólida para:

- futuros modelos predictivos
- segmentación de clientes
- optimización de campañas comerciales

---

# 11. Recomendaciones estratégicas

A partir de los resultados obtenidos, se proponen las siguientes recomendaciones:

- Optimizar el número de contactos comerciales

- Reducir campañas excesivamente repetitivas y priorizar contactos más eficientes.

- Priorizar clientes con historial positivo

- Clientes con campañas previas exitosas presentan mayor probabilidad de conversión.

- Reforzar estrategias para clientes recientes

- Los clientes nuevos muestran mayor predisposición a contratar productos financieros.

- Potenciar canales móviles

- El contacto mediante dispositivos móviles parece generar mejores resultados comerciales.

- Aplicar segmentación avanzada

- Personalizar campañas según: perfil educativo, ocupación, historial comercial, y comportamiento previo.

---

# 12. Próximos pasos

Como posibles mejoras futuras del proyecto se plantean las siguientes líneas de trabajo:

- Desarrollo de modelos predictivos de clasificación.
- Aplicación de técnicas de Machine Learning.
- Evaluación de importancia de variables.
- Implementación de modelos de scoring de clientes.
- Generación de dashboards interactivos.
- Incorporación de nuevas fuentes de datos.
- Optimización automática de campañas comerciales.
