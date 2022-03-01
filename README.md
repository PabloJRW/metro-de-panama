# Metro de Panamá
<img src="https://github.com/PabloJRW/metro-de-panama/blob/main/img/Metro_de_Panama_Logo.svg" width="120" height="120"/>


El Metro de Panamá es el ferrocarril metropolitano cuya red cubre parte de Ciudad de Panamá, capital de la República de Panamá. Este sistema de transporte es administrado por la empresa de capitales estatales Metro de Panamá S.A. Es el primer sistema de ferrocarriles metropolitanos panameño y el primer sistema de metro de Centroamérica. 

Este proyecto consiste de tomar datos de la demanda de usuarios e ingresos tarifarios correspondientes a los años 2019 hasta 2021, realizar transformaciones y aplicar feature engineering para obtener como resultado final un formato de serie temporal que nos facilite un posterior análisis de los mismos.

### Demanda de usuarios
Los datos de la demanda de usuarios consiste de, la cantidad de usuarios que hicieron uso del servicio de transporte del metro mensualmente. Estos están registrados en 3 tipos de demanda: laborable, sábados y feriados.  

Los datos originales de la demanda de usuarios tenían el siguiente formato:
<img src="https://github.com/PabloJRW/metro-de-panama/blob/main/img/demanda_datos_originales.png"/>

Una vez transformados, obtenemos el siguiente resultado:
<img src="https://github.com/PabloJRW/metro-de-panama/blob/main/img/demanda_datos_transformados.png"/>

### Ingresos tarifarios
Los ingresos tarifarios consiste de la recaudación monetario mensual, de la siguiente manera: ingreso monedero, estudiantes, jubilados y discapacitados.

Estos estaban registrados de la siguiente manera:
<img src="https://github.com/PabloJRW/metro-de-panama/blob/main/img/ingresos_datos_originales.png"/>


El resultado obtenido luego de la transformación, es un conjunto de datos ordenados por un índice de tipo datetime, el cual, es apropiado para el análisis de series temporales. El análisis de series de tiempom, nos permite comparar los cambios o fluctuaciones de la variable objeto contra los mismos períodos en años anteriores, identificar tendencias, realizar pronósticos. 
