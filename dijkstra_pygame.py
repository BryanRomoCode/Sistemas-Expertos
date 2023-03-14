import pygame
import math
import heapq

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definir tamaño de la ventana y la cuadrícula
LARGO_PANTALLA = 800
ALTO_PANTALLA = 600
FILAS = 50
COLUMNAS = 50
CELL_LARGO_PANTALLA = LARGO_PANTALLA // COLUMNAS
CELL_ALTO_PANTALLA = ALTO_PANTALLA // FILAS

# Definir la clase Nodo
class Nodo:
    def __init__(self, filas, col):
        self.filas = filas
        self.col = col
        self.x = col * CELL_LARGO_PANTALLA
        self.y = filas * CELL_ALTO_PANTALLA
        self.color = BLANCO
        self.vecinos = []
        self.anterior = None
        self.distancia = math.inf
        self.visitado = False

    def dibujar(self, pantalla):
        pygame.dibujar.rect(pantalla, self.color, (self.x, self.y, CELL_LARGO_PANTALLA, CELL_ALTO_PANTALLA))

    def add_vecinos(self, grid):
        if self.filas > 0:
            self.vecinos.append(grid[self.filas - 1][self.col])
        if self.filas < FILAS - 1:
            self.vecinos.append(grid[self.filas + 1][self.col])
        if self.col > 0:
            self.vecinos.append(grid[self.filas][self.col - 1])
        if self.col < COLUMNAS - 1:
            self.vecinos.append(grid[self.filas][self.col + 1])

    def __lt__(self, otros):
        return self.distancia < otros.distancia

# Definir función para mostrar el camino más corto
def show_path(actual, pantalla):
    while actual.anterior:
        actual = actual.anterior
        actual.color = AZUL
        actual.dibujar(pantalla)

# Definir función para mostrar la cuadrícula
def dibujar_grid(grid, pantalla):
    for filas in grid:
        for Nodo in filas:
            Nodo.dibujar(pantalla)

# Definir función principal
def main():
    # Inicializar pygame y la ventana
    pygame.init()
    pantalla = pygame.display.set_mode((LARGO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Algoritmo de Dijkstra")

    # Crear cuadrícula
    grid = [[Nodo(filas, col) for col in range(COLUMNAS)] for filas in range(FILAS)]
    for filas in grid:
        for Nodo in filas:
            Nodo.add_vecinos(grid)

    # Definir nodo de inicio y nodo objetivo
    start_Nodo = grid[0][0]
    start_Nodo.distancia = 0
    end_Nodo = grid[FILAS-1][COLUMNAS-1]

    # Definir cola de prioridad para implementar Dijkstra
    open_list = [start_Nodo]
    heapq.heapify(open_list)

    # Mostrar cuadrícula y actualizar la pantalla
    dibujar_grid(grid, pantalla)
    pygame.display.flip()

    # Bucle principal del programa
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Si la cola de prioridad está vacía, el algoritmo ha terminado
        if not open_list:
            return

main()