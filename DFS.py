# Classe que reprsenta o grafo em que está sendo realizado a busca:
class Grafo:
    def __init__(self):
        self.grafo = {}

# adicionar vértices ao grafo

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

# adicionar aresta aos vertices do grafo

    def adicionar_aresta(self, origem, destino):
        if origem in self.grafo:
            self.grafo[origem].append(destino)
        else:
            self.grafo[origem] = [destino]

# A busca em profundidade em implementada na função dfs e criando a pilha contendo o vértice inicial

    def dfs(self, vertice_inicial):
        visitados = set()
        pilha = [vertice_inicial]
# loop enquanto a pilha não estiver vazia. 
# A cada iteração, removemos o vértice do topo da pilha
# verificamos se ele já foi visitado
# Se não tiver sido visitado, marcamos o vértice como visitado, imprimimos seu valor e adicionamos seus vizinhos à pilha.
        while pilha:
            vertice = pilha.pop()

            if vertice not in visitados:
                visitados.add(vertice)
                print(vertice, end=" ")

                if vertice in self.grafo:
                    for vizinho in self.grafo[vertice]:
                        pilha.append(vizinho)



# Exemplo de uso com entrada do usuário
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

print("Resultado da busca em profundidade:")
grafo.dfs(vertice_inicial)