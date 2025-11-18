"""
Taller 4 - Patrones Concurrentes
Plantilla base para el sistema productor-consumidor.
Autor: (nombre del estudiante)
Fecha: (dd/mm/aaaa)
"""
import threading, queue, time, random
# --- Configuración Global ---
NUM_PRODUCTORES = 2
NUM_CONSUMIDORES = 3
TAREAS_POR_PRODUCTOR = 5
COLA_MAX_SIZE = 5

# Objeto 'Sentinel': valor especial para indicar a los consumidores que deben detenerse.
SENTINEL = object()

def productor(id_prod, cola):
    """Genera elementos y los coloca en la cola compartida."""
    print(f"[Prod {id_prod}] Iniciado. Producirá {TAREAS_POR_PRODUCTOR} tareas.")
    
    for i in range(TAREAS_POR_PRODUCTOR):
        # Simula tiempo de generación
        tiempo_espera = random.uniform(0.3, 1.0)
        time.sleep(tiempo_espera)
        
        tarea = f"Tarea-{id_prod}-{i}"
        
        # put() se bloquea si la cola está llena (sincronización automática)
        cola.put(tarea) 
        print(f"  [Prod {id_prod}] produjo {tarea}. (Cola: {cola.qsize()})")
        
    print(f"[Prod {id_prod}] Finalizó su producción.")
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