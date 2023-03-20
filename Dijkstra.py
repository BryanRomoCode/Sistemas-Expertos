import math
import matplotlib.pyplot as plt
import networkx as nx

plt.ion()

def dijkstra(grafo, fuente, destino):

    # Se inicializa el grafo
    G = nx.Graph(grafo)
    pos = nx.spring_layout(G)
    
    # Distancias de la fuente hacia los nodos
    distancias = {nodo: math.inf for nodo in grafo}
    # Distancia de la fuente a sí misma 
    distancias[fuente] = 0
    # Nodos sin visitar
    nodos_sin_visitar = set(grafo.keys())
    # Diccionario de nodos visitados y sus predecesores
    visitados = {}
    # Inicializar el camino
    camino = []
    
    # Dibujar el grafo inicial
    nx.draw_networkx(G, pos, with_labels=True)
    plt.show()
    plt.pause(2)
    
    while nodos_sin_visitar:
        # Seleccionar el nodo con la distancia mínima de la fuente
        nodo_actual = min(nodos_sin_visitar, key=lambda nodo: distancias[nodo])
        nodos_sin_visitar.remove(nodo_actual)
        
        # Si se llegó al nodo de destino, salir del bucle
        if nodo_actual == destino:
            break
        
        # Actualizar las distancias de los vecinos no visitados
        for vecino, peso in grafo[nodo_actual].items():
            if vecino in nodos_sin_visitar:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    visitados[vecino] = nodo_actual
        
        # Agregar el nodo actual al camino
        camino.append(nodo_actual)
        # Dibujar el grafo con los nodos visitados en rojo y los nodos sin visitar en negro,
        # y el camino que se está siguiendo en verde
        colores = ['red' if nodo in visitados else 'black' for nodo in nodos_sin_visitar]
        colores += ['green'] * len(camino)
        nx.draw_networkx(G, pos, with_labels=True, node_color=colores)
        plt.show()
        plt.pause(2)
    
    # Agregar el destino al camino
    camino.append(destino)
    
    # Dibujar el grafo final con el camino en rojo
    nx.draw_networkx(G, pos, with_labels=True, node_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=[(camino[i], camino[i+1]) for i in range(len(camino)-1)], edge_color='red', width=5)
    plt.show()
    plt.pause(2)
    
    # Retornar la distancia más corta y el camino
    return distancias[destino], camino

# Se define el grafo
grafo = {
    'A': {'B':2, 'C': 3},
    'B': {'A':2, 'D':1},
    'C': {'A':3, 'D':4, 'E': 5},
    'D': {'B':1, 'C': 4, 'F': 3},
    'E': {'C':5, 'F': 2,},
    'F': {'D':3, 'E': 2,},
}

fuente = 'A'
destino = 'F'
dijkstra(grafo, fuente, destino)