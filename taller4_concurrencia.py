"""
Taller 4 - Patrones Concurrentes
Plantilla base para el sistema productor-consumidor.
Autor: (nombre del estudiante)
Fecha: (dd/mm/aaaa)
"""
import threading, queue, time, random

def productor(id_prod, cola):
    """Genera elementos y los coloca en la cola compartida."""
    pass # TODO: completar implementación

def consumidor(id_cons, cola):
    """Extrae elementos de la cola y los procesa."""
    pass # TODO: completar implementación

def main():
    """Crea productores, consumidores y mide el tiempo total."""
    inicio = time.time()
    
    # 1. Inicialización de la cola (recurso compartido y sincronizado)
    cola = queue.Queue(maxsize=5)
    
    # 2. Listas para almacenar los objetos Thread
    productores = []
    consumidores = []
    
    # TODO: crear hilos productores y consumidores
    # TODO: iniciar, unir y medir tiempos
    
    fin = time.time()
    print(f"Tiempo total: {fin - inicio:.2f} segundos")

if __name__ == "__main__":
    main()