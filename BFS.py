from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.grafo:
            self.grafo[origem].append(destino)
        else:
            self.grafo[origem] = [destino]

    def bfs(self, vertice_inicial):
        visitados = set()
        fila = deque([vertice_inicial])

        while fila:
            vertice = fila.popleft()

            if vertice not in visitados:
                visitados.add(vertice)
                print(vertice, end=" ")

                if vertice in self.grafo:
                    for vizinho in self.grafo[vertice]:
                        fila.append(vizinho)

# Uso com entrada do usuário
grafo = Grafo()

n = int(input("Digite o número de vértices: "))

for i in range(n):
    vertice = int(input(f"Digite o valor do vértice {i+1}: "))
    grafo.adicionar_vertice(vertice)

m = int(input("Digite o número de arestas: "))

for i in range(m):
    origem = int(input(f"Digite o valor da origem da aresta {i+1}: "))
    destino = int(input(f"Digite o valor do destino da aresta {i+1}: "))
    grafo.adicionar_aresta(origem, destino)

vertice_inicial = int(input("Digite o valor do vértice inicial para a busca em profundidade: "))

print("Busca em Largura (BFS):")
grafo.bfs(vertice_inicial)
