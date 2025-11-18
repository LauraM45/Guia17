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
    """Extrae elementos de la cola y los procesa. Espera el SENTINEL para detenerse."""
    print(f"  [Cons {id_cons}] Iniciado.")
    
    while True:
        # Bloquea hasta que haya un elemento
        tarea = cola.get() 
        
        if tarea is SENTINEL:
            cola.task_done()       # Notifica que el SENTINEL fue procesado (necesario para cola.join())
            cola.put(SENTINEL)     # Vuelve a poner la señal para el próximo consumidor
            break # Sale del bucle While, terminando el hilo
            
        print(f"    [Cons {id_cons}] procesando {tarea}...")
        
        # Simula tiempo de procesamiento
        time.sleep(random.uniform(0.5, 1.5))
        
        # NOTIFICACIÓN CLAVE: Marca la tarea REAL como terminada
        cola.task_done() 
        print(f"    [Cons {id_cons}] completó {tarea}.")

    print(f"  [Cons {id_cons}] Finalizado.")

def main():
    """Crea productores, consumidores y mide el tiempo total."""
    print("--- Sistema Productor-Consumidor Iniciado ---")
    inicio = time.time()
    
    # 1. Inicialización de la cola (recurso compartido y sincronizado)
    cola = queue.Queue(maxsize=COLA_MAX_SIZE)
    
    # 2. Creación de hilos
    hilos_productores = [threading.Thread(target=productor, args=(i, cola), name=f"Prod-{i}") 
                         for i in range(1, NUM_PRODUCTORES + 1)]
    hilos_consumidores = [threading.Thread(target=consumidor, args=(i, cola), name=f"Cons-{i}") 
                          for i in range(1, NUM_CONSUMIDORES + 1)]
    
    # 3. Iniciar todos los hilos
    for h in hilos_consumidores + hilos_productores:
        h.start()

    # 4. Esperar a que TODOS los productores terminen su trabajo
    for h in hilos_productores:
        h.join()
    
    print("\n[INFO] Productores terminaron. Esperando a que la cola se vacíe (cola.join())...")

    # 5. SINCRONIZACIÓN CENTRAL: Esperar a que todos los elementos añadidos sean procesados (task_done llamado)
    cola.join() 
    
    print("[INFO] Todos los elementos originales han sido procesados. Enviando señales de parada (SENTINEL)...")

    # 6. ENVIAR SEÑAL DE PARADA: Poner el SENTINEL tantas veces como consumidores haya.
    for _ in range(NUM_CONSUMIDORES):
        cola.put(SENTINEL)
        
    # 7. Esperar a que los consumidores terminen (lean el SENTINEL y salgan)
    for h in hilos_consumidores:
        h.join()

    # 8. Métrica y finalización
    fin = time.time()
    
    print("\n--- Resultados ---")
    print(f"Tareas totales: {NUM_PRODUCTORES * TAREAS_POR_PRODUCTOR}")
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
    print("--- Sistema Productor-Consumidor Finalizado con éxito ---")
    
if __name__ == "__main__":
    main()