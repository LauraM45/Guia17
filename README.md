# Guia17

Laura Sofia Moreno Suarez  20242020160
Este proyecto implementa dos patrones de concurrencia basados en la Guía 17:

Productor-Consumidor (taller4_productor_consumidor.py):

Utiliza el módulo threading y la clase queue.Queue como recurso compartido seguro.

Demuestra la sincronización de capacidad y acceso a través de los métodos bloqueantes (put y get).

La finalización segura se logra mediante el control estricto de hilos (h.join()), la confirmación total de tareas procesadas (cola.join()) y el uso de la señal SENTINEL para detener los consumidores.

Pool de Hilos (taller4_threadpoolexecutor.py):

Utiliza el módulo concurrent.futures (patrón Pool de Hilos) como alternativa moderna para la gestión automatizada de la concurrencia en un conjunto finito de tareas.

Indicaciones de Ejecución

Ambos programas están diseñados para ejecutarse de forma independiente en un entorno Python 3.

Requisitos

El código solo requiere módulos estándar de Python, por lo que no es necesario instalar librerías externas.

Ejecución

Asegúrese de tener el entorno virtual activo (source .venv/bin/activate).

Ejecute cada archivo por separado desde la terminal para obtener las métricas y la trazabilidad de la consola:

# 1. Ejecutar el patrón Productor-Consumidor (Énfasis del taller)
python taller4_productor_consumidor.py

# 2. Ejecutar el patrón Pool de Hilos (Métrica de comparación)
python taller4_threadpoolexecutor.py


Métricas

El registro de tiempos se encuentra en la salida de consola de cada script.
